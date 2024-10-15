# Umgang mit `.gitignore`

Die `.gitignore`-Datei ist ein essentielles Werkzeug, um unnötige oder sensible Dateien von der Versionskontrolle auszuschließen. In Data Science Projekten entstehen häufig temporäre Dateien, große Datenbestände und Arbeitsprodukte wie Modelle oder Checkpoints, die nicht in Git gespeichert werden sollten. Eine saubere `.gitignore` sorgt dafür, dass nur relevante Code- und Konfigurationsdateien versioniert werden, während Zwischenergebnisse und private Daten geschützt bleiben.



## Typische Dateien, die in Data Science Projekten ignoriert werden sollten:
- **Daten**: CSV, Excel, Parquet-Dateien und andere große Datenbestände
- **Modelle**: Zwischengespeicherte Modelle und Checkpoints
- **Notebooks**: Checkpoints und temporäre Dateien
- **Virtuelle Umgebungen**: Paketinstallationen und virtuelle Environments (z.B. `venv`, `conda`)
- **Logdateien und temporäre Ausgaben**: Alles, was nur für temporäre Berechnungen gebraucht wird (z.B. Logs, Cache)


### Beispiel `.gitignore`-Template für Data Science Projekte

Hier ist ein Beispiel für eine `.gitignore`-Datei, die für Data Science Projekte nützlich sein kann:

```gitignore
# Python Standard
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
*.so

# Jupyter Notebook Checkpoints
.ipynb_checkpoints/

# Virtual Environments
env/
venv/
.venv/
ENV/
env.bak/
venv.bak/

# Conda Environments
.conda/
*.conda
*.env
*.yml

# Data files
*.csv
*.tsv
*.xls
*.xlsx
*.parquet
*.feather
*.h5
*.hdf5
*.db

# Model files
*.pkl
*.joblib
*.h5
*.pb
*.onnx

# Logs und temporäre Dateien
*.log
*.out
*.tmp
*.cache
*.pid
*.tar.gz
*.zip

# IDEs und Editoren
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# DVC (falls verwendet)
.dvc/

# Docker und andere Umgebungen
.dockerignore
docker-compose.yml
```