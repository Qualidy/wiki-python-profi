## Best Practices für Git

### Best Practices für Commit-Nachrichten

- Schreibe Commit-Nachrichten in der Befehlsform, z. B. "Fügt eine neue Spalte hinzu" anstelle von "Neue Spalte wurde hinzugefügt".
- Vermeide generische Nachrichten wie "Fix" oder "Update", da sie keine sinnvolle Information über die Änderung geben.
- Gruppiere kleine Änderungen in einem Commit, anstatt viele winzige Commits zu machen.


### Best Practices mit Branches in Git

Branching ist eine der mächtigsten Funktionen von Git und ermöglicht es uns, parallel an verschiedenen Features, Bugfixes oder Experimenten zu arbeiten, ohne den Hauptzweig des Projekts zu beeinträchtigen. Ein disziplinierter Umgang mit Branches sorgt für eine saubere Projektstruktur und erleichtert die Zusammenarbeit im Team. In diesem Abschnitt besprechen wir einige Best Practices für den effizienten Umgang mit Branches.

#### 1. Verwende eine konsistente Branch-Namenskonvention

Eine klare und einheitliche Namenskonvention für Branches hilft dabei, den Zweck eines Branches sofort zu verstehen und Missverständnisse im Team zu vermeiden. Hier einige gängige Konventionen:

- **Feature-Branches:** `feature/<beschreibung>`
    - Beispiel: `feature/benutzer-login`
- **Bugfix-Branches:** `bugfix/<beschreibung>`
    - Beispiel: `bugfix/csv-import-error`
- **Hotfix-Branches (für kritische Fehler):** `hotfix/<beschreibung>`
    - Beispiel: `hotfix/sicherheitslücke`
- **Release-Branches:** `release/<version>`
    - Beispiel: `release/1.0.0`

Eine klare Struktur und Beschreibung im Branch-Namen erleichtert es jedem im Team, den Zweck des Branches zu erkennen.



#### 2. Isoliere Features und Bugfixes in eigene Branches

Jedem neuen Feature oder Bugfix sollte ein eigener Branch zugewiesen werden. Dies ermöglicht:

- **Isolation von Änderungen:** Features und Fixes können unabhängig voneinander entwickelt, getestet und integriert werden, ohne den Hauptbranch zu stören.
- **Parallelität:** Mehrere Teammitglieder können gleichzeitig an unterschiedlichen Features arbeiten, ohne in Konflikt zu geraten.
- **Rückverfolgbarkeit:** Änderungen sind leichter nachvollziehbar und jeder Branch repräsentiert eine klar definierte Aufgabe.

**Beispiel:**

```bash
git checkout -b feature/benutzer-authentifizierung
```

Nach dem Fertigstellen des Features oder Fixes wird der Branch in den Hauptbranch (meist `main` oder `develop`) gemerged.



#### 3. Regelmäßig rebasen oder den Hauptbranch mergen

Wenn du über längere Zeit an einem Feature-Branch arbeitest, ist es wichtig, den Branch regelmäßig mit dem Hauptbranch zu synchronisieren. Dies kann durch **Merge** oder **Rebase** geschehen:

- **Merge:** Führt Änderungen des Hauptbranches in den Feature-Branch ein, behält jedoch alle Historien bei.
  
  ```bash
  git checkout feature/benutzer-login
  git merge main
  ```

- **Rebase:** Setzt den Feature-Branch auf den aktuellen Stand des Hauptbranches und erzeugt eine linearere Historie, da er "so tut", als ob die Arbeit immer auf dem neuesten Stand des Hauptbranches stattfand.

  ```bash
  git checkout feature/benutzer-login
  git rebase main
  ```

Durch regelmäßiges Rebasen oder Mergen vermeiden wir Konflikte und stellen sicher, dass unsere Änderungen mit der aktuellen Version kompatibel sind.



#### 4. Kleine, fokussierte Branches erstellen

Branches sollten spezifische Aufgaben isolieren und nicht zu viele Änderungen auf einmal umfassen. Ein kleiner Branch ist einfacher zu testen, zu überprüfen und zu integrieren. Dies gilt besonders in Data-Science-Projekten, in denen Datenpipelines und Modelle oft schrittweise entwickelt werden. Ein paar Vorteile dieser Praxis sind:

- **Schnellere Code-Reviews:** Kleinere Änderungen sind schneller zu überprüfen.
- **Weniger Konflikte:** Je kleiner der Branch, desto weniger ist die Wahrscheinlichkeit, dass es zu Merge-Konflikten kommt.
- **Bessere Nachvollziehbarkeit:** Es ist leichter, spezifische Änderungen zu finden und rückgängig zu machen.



#### 5. Lösche Branches nach dem Merge

Nach erfolgreichem Merge eines Branches in den Hauptbranch sollte der Branch gelöscht werden, um Verwirrung und überflüssige Branches zu vermeiden. Dies sorgt für eine saubere Git-Historie und vermeidet das Ansammeln von "toten" Branches.

```bash
# Branch lokal löschen
git branch -d feature/benutzer-login

# Branch vom Remote löschen
git push origin --delete feature/benutzer-login
```



#### 6. Trenne Entwicklungs- und Hauptbranch

Es empfiehlt sich, separate Branches für Entwicklung und Produktion zu haben:

- **Main-Branch (z.B. `main` oder `master`):** Dieser Branch enthält die stabile und produktionsbereite Version des Projekts. Hier sollten nur geprüfte und getestete Features gemerged werden.
  
- **Entwicklungsbranch (z.B. `develop`):** Der `develop`-Branch enthält die neusten, aber möglicherweise noch nicht vollständig stabilen Features. Neue Features und Fixes werden zuerst in `develop` gemerged, bevor sie nach umfassendem Testen in `main` überführt werden.



#### 7. Nutze Pull Requests für Branch-Merges

Ein guter Workflow ist, den Merge eines Branches über einen **Pull Request (PR)** durchzuführen. Pull Requests ermöglichen eine formale Code-Überprüfung durch Teammitglieder, bevor der Code in den Hauptbranch integriert wird. Das sorgt für eine bessere Qualitätssicherung und stellt sicher, dass alle Änderungen nachvollziehbar sind.


## Umgang mit Jupyter Notebooks in Git für Data Science Projekte

Jupyter Notebooks sind in Data-Science-Projekten weit verbreitet, können jedoch in der Versionskontrolle einige Herausforderungen mit sich bringen. Da Notebooks nicht nur Code, sondern auch Metadaten und Ausgaben speichern, können sie bei mehreren Änderungen schwer lesbar und konfliktanfällig werden. Hier sind einige Best Practices, um effizient mit Jupyter Notebooks in Git umzugehen:



#### 1. **Trenne Code und Ausgaben**
Speichere keine Ausgaben (Plots, Tabellen, etc.) in den Notebooks, bevor du sie in Git commitest. Du kannst alle Ausgaben löschen, indem du in Jupyter die Option **"Kernel > Restart & Clear Output"** wählst. Dadurch bleibt die Versionshistorie sauberer und reduziert Konflikte.

```bash
# Beispiel: Notebook ohne Ausgaben speichern
jupyter nbconvert --clear-output --inplace <notebook.ipynb>
```

#### 2. **Nutze `.gitignore` für temporäre Dateien**
Vermeide, dass unnötige temporäre Dateien wie Checkpoints oder Cache-Dateien ins Git-Repo gelangen, indem du sie in der `.gitignore`-Datei ausschließt:

```bash
# .gitignore
.ipynb_checkpoints/
```

#### 3. **Verwende `nbdime` für besseres Diffing und Merging**
Standard-Git-Diffs für Jupyter Notebooks sind oft schwer lesbar. Das Tool [`nbdime`](https://github.com/jupyter/nbdime) bietet eine spezialisierte Möglichkeit, Diffs von Notebooks klar darzustellen und Merge-Konflikte leichter zu lösen:

```bash
# Installation
pip install nbdime

# Notebook-Diffs in Git einrichten
nbdime config-git --enable
```

#### 4. **Teile Code als Python-Module**
Während der Entwicklung ist es oft sinnvoll, wiederverwendbare Funktionen und Pipelines in Python-Skripte auszulagern. Das hält die Notebooks leichtgewichtig und erleichtert die Wiederverwendbarkeit und Versionierung des Codes.

```bash
# Beispiel: Funktionen in einem separaten Modul auslagern
project/
│
├── notebooks/
│   └── analysis.ipynb
└── src/
    └── data_processing.py
```