# Git für Data Scientists

Git ist ein Versionskontrollsystem, das es uns ermöglicht, Änderungen an Code über die Zeit zu verfolgen und mit Teams effizient zusammenzuarbeiten. In diesem Kapitel wiederholen wir kurz die Grundlagen und vertiefen uns dann in fortgeschrittene Themen wie **Rebase**, **Cherry Picking** und **Commit-Konventionen**.

## 1. Grundlagen von Git

Bevor wir in fortgeschrittenere Themen eintauchen, wiederholen wir die wichtigsten Konzepte von Git:

- **Repository (Repo):** Ein Ordner, der die gesamte Historie der Änderungen eines Projekts speichert.
- **Commit:** Eine Momentaufnahme des aktuellen Zustands der Dateien. Jeder Commit hat eine eindeutige ID.
- **Branch:** Ein Zweig in der Versionsgeschichte, der es uns erlaubt, parallel an verschiedenen Features oder Fixes zu arbeiten.
- **Merge:** Das Zusammenführen von zwei Branches.
- **Remote:** Die Online-Version eines Git-Repositories (z.B. auf GitHub oder GitLab).

### Wichtige Befehle

- **Initialisieren eines neuen Repos:**
    ```bash
    git init
    ```

- **Änderungen zum Staging hinzufügen:**
    ```bash
    git add <datei>
    ```

- **Einen Commit erstellen:**
    ```bash
    git commit -m "Beschreibung der Änderung"
    ```

- **Änderungen auf einen Remote-Branch pushen:**
    ```bash
    git push origin <branch-name>
    ```

---

## 2. Fortgeschrittene Themen

### 2.1 Git Rebase

Mit **Rebase** können wir eine saubere Versionsgeschichte zu erstellen, indem wir Änderungen aus einem Branch auf einem anderen neu anwenden, anstatt sie zu mergen. Während ein **Merge** alle Commits aus beiden Branches beibehält und einen "Merge-Commit" erstellt, ordnet Rebase die Commits neu an, sodass sie auf der Spitze des Ziel-Branches erscheinen, als ob sie von Anfang an dort gewesen wären.

#### Wann sollte Rebase verwendet werden?

- Um eine saubere, lineare Historie zu erhalten.
- Wenn wir auf einem Feature-Branch gearbeitet haben und die Änderungen auf den aktuellen Stand des Haupt-Branches bringen wollen, ohne die Historie zu verkomplizieren.

#### Beispiel: Rebase eines Feature-Branches auf `main`

```bash
# Wir befinden uns auf dem Feature-Branch
git checkout feature-branch

# Rebase den Feature-Branch auf den aktuellen Stand von main
git rebase main
```

#### Konflikte während des Rebasing lösen

Während eines Rebase-Vorgangs können Konflikte auftreten, wenn Änderungen auf den gleichen Zeilen einer Datei gemacht wurden. In diesem Fall wird Git den Rebase-Prozess anhalten, bis der Konflikt gelöst ist. Nach dem Lösen des Konflikts:

```bash
# Konflikte manuell lösen und Dateien zum Staging hinzufügen
git add <datei>

# Rebase fortsetzen
git rebase --continue
```

### 2.2 Git Cherry Picking

**Cherry Picking** erlaubt es uns, einen spezifischen Commit von einem Branch zu nehmen und ihn auf einen anderen Branch anzuwenden, ohne alle anderen Änderungen aus dem ursprünglichen Branch mitzunehmen. Dies ist nützlich, wenn wir einen bestimmten Fix oder ein Feature aus einem Branch isoliert in einen anderen einfügen wollen.

#### Wann sollte Cherry Picking verwendet werden?

- Wenn ein Bugfix bereits in einem Feature-Branch existiert und wir ihn schnell in den Haupt-Branch übernehmen müssen, ohne den ganzen Branch zu mergen.
- Um spezifische Commits zwischen verschiedenen Branches zu übertragen.

#### Beispiel: Cherry Picking eines Commits

1. Finde die Commit-ID, die du übernehmen möchtest:
    ```bash
    git log
    ```

2. Führe den Cherry Pick-Vorgang durch:
    ```bash
    git checkout main
    git cherry-pick <commit-id>
    ```

Falls Konflikte auftreten, müssen diese manuell gelöst und der Cherry-Pick-Vorgang fortgesetzt werden:

```bash
git add <datei>
git cherry-pick --continue
```

### 2.3 Commit-Konventionen (Form)

Eine konsistente Commit-Message-Struktur hilft nicht nur bei der Lesbarkeit des Codes, sondern verbessert auch die Zusammenarbeit im Team und die Wartbarkeit des Projekts. Wir sollten eine klare Struktur für unsere Commit-Nachrichten einhalten.

#### Eine sinnvolle Commit-Nachricht besteht aus:
1. **Header:** Eine kurze, prägnante Zusammenfassung (max. 50 Zeichen), die beschreibt, was geändert wurde.
2. **Body (optional):** Ein detaillierterer Text, der erklärt, warum die Änderung vorgenommen wurde, welche Auswirkungen sie hat und ggf. wie sie implementiert wurde.
3. **Footer (optional):** Zusätzliche Informationen wie Referenzen zu Tickets oder Issues.

#### Beispiel einer guten Commit-Nachricht:

```plaintext
fix(bug): Behebt das Problem beim Einlesen der CSV-Datei

Das Problem wurde durch falsche Datentypen verursacht. Die Änderung
stellt sicher, dass die korrekten Typen verwendet werden, wenn die Datei
eingelesen wird.

Fixes #123
```