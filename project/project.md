# ReadMe

### Installation
- **nach dem Pullen des Codes** in das Hauptverzeichnis des Logins im project-Ordner navigieren
```
12ItANW   
│
└───project
│   │   project.md
│   │   .gitignore
│   │
│   └───Login
│       │   ...
```

- Dann starten wir eine virtuelle Umgebung:
```sh
python -m venv env
```

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

- Um einen Adminuser zu erstellen, damit man in das Admininterface kann, diesen Code ausführen:
```sh
python manage.py createsuperuser
```

- Um das Porjekt zu starten einfach
```sh
python manage.py runserver 0.0.0.0:8000
```
-Und dann auf folgende <a href="http://127.0.0.1:8000/login" target="_blank">->Webiste<-</a>