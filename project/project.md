# ReadMe

### Installation
- nach dem Pullen des Codes in das Hauptverzeichnis des Logins im project-Ordner navigieren (project/Login)
- Dann starten wir eine virtuelle Umgebung:
```sh
python -m venv env
```
Hier durch wir ein neuer Ordner erstellt
- Danach falls nicht automatisch, müssen wir die virtuelle Umgebung noch starten:
```sh
env/Scripts/activate
```
- Jetzt die benötigten Pakete installieren:
```sh
pip install -r requirements.txt
```
- Jetzt die Datenbank aufbauen:
```sh
python  manage.py  makemigrations
python  manage.py  migrate
```

- Um das Porjekt zu starten einfach
```sh
python manage.py runserver 0.0.0.0:8000
```
-Und dann auf folgende Seite
[Webiste](https://127.0.0.1/Login)
