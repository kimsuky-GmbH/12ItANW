from django.shortcuts import render

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings
from .models import User
from django.http import JsonResponse
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature

# Create your views here.

def login(request):
    message = ""
    timestamp_signer = TimestampSigner()

    if request.method == 'POST':
        match request.POST['todo']:
            case 'register':
                email = request.POST['email']
                password = User.password_hash(request.POST['password'])

                if not User.objects.filter(email=email).exists(): # Kucken ob nicht schon jemand diese E-Mail hat
                    User.objects.create(email = email, password = password, status = 0) # Objekt erstellen

                    # Registercode erstellen und speichern
                    user = User.objects.get(email=email)

                    registerCode = timestamp_signer.sign(str(user.id))

                    user.registerCode = registerCode
                    user.save()

                    try:
                        subject = 'Urban Climate Email Bestätigung'
                        
                        # HTML-Inhalt erstellen
                        html_message = render_to_string('mail_template.html', {
                            'context': f'<a href="http://127.0.0.1:8000/login?registerCode={user.registerCode}">Hier Klicken</a>'
                        })
                        plain_message = strip_tags(html_message)
                        
                        from_email = settings.EMAIL_HOST_USER
                        to = [email]
                        
                        # E-Mail senden
                        send_mail(
                            subject,
                            plain_message,  # Plaintext-Version
                            from_email,
                            to,
                            html_message=html_message  # HTML-Version
                        )
                        print("E-Mail erfolgreich gesendet!")
                    except Exception as e:
                        print(f"Fehler beim Senden der E-Mail: {e}")
                    return JsonResponse({'success': True})
                
                else:
                    return JsonResponse({'error': 'emailVorhanden'})

    elif request.method == 'GET':
        match list(request.GET.keys()):
            case ['registerCode']:
                registerCode = request.GET.get("registerCode")
                
                try:
                    userId = timestamp_signer.unsign(registerCode, max_age=36000)  # 36000 Sekunden = 10 Stunden

                    if User.objects.filter(id=userId, status = 0).exists():
                        user = User.objects.get(id=userId, status = 0)
                        user.status = 1
                        user.save()
                        message = "userConfirmed"
                    else:
                        print("User bereits bestätigt")
                        message = "userAlreadyConfirmed"
                except SignatureExpired:
                    print("Signatur ist abgelaufen!")
                    message = "toLate"
                except BadSignature:
                    print("Ungültige Signatur oder Manipulation erkannt!")
                    message = "notFound"
            
    
    return render(request, 'register.html', { 'message': message })
