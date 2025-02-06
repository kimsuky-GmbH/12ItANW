# ReadMe

### Installation
- nach dem Pullen des Codes in das Hauptverzeichnis navigieren
- Dann starten wir eine virtuelle Umgebung:
`python -m venv env`
Hier durch wir ein neuer Ordner erstellt
- Danach falls nicht automatisch, müssen wir die virtuelle Umgebung noch starten:
`enc/Scripts/activate`
- Jetzt die benötigten Pakete installieren:
`pip install -r requirements.txt`
- Jetzt die Datenbank aufbauen:
```sh
python  manage.py  makemigrations
python  manage.py  migrate
```
