Repository klonen:

```commandline
git clone https://github.com/Qualidy/wiki-stochastik.git
```

Virtuelle Umgebung anlegen:

```commandline
python -m venv .venv
```

Virtuelle Umgebung aktivieren:

Auf Windows:

```commandline
.\.venv\Scripts\Activate.ps1
```

Abhängigkeiten installieren:

```commandline
pip install -r requirements.txt
```

Lokal Webseite ausführen:

```commandline
mkdocs serve
```

Webseite veröffentlichen:

```commandline
mkdocs gh-deploy
```
