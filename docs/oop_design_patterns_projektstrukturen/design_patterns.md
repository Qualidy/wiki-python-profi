# Design Patterns in Data Science Projekten

Design Patterns sind wiederkehrende Lösungsansätze für häufig auftretende Entwurfsprobleme in der Softwareentwicklung. In Data Science Projekten, die oft komplexe und sich wiederholende Prozesse beinhalten, können Design Patterns dabei helfen, Code wartbarer, flexibler und effizienter zu gestalten. Der Einsatz von Design Patterns ermöglicht eine klare Strukturierung von Projekten, die das Verständnis und die Zusammenarbeit im Team erleichtert. Im Folgenden gehen wir auf einige wichtige Design Patterns ein, die in Data Science Projekten nützlich sein können.




## Vorteile der Nutzung von Design Patterns in Data Science Projekten

1. **Wartbarkeit**: Muster sorgen für einen strukturierten und modularen Code, der leichter zu pflegen ist.
2. **Wiederverwendbarkeit**: Einmal implementierte Design Patterns können in anderen Projekten oder Szenarien wiederverwendet werden.
3. **Erweiterbarkeit**: Mit Patterns wird es einfacher, neuen Code hinzuzufügen, ohne den bestehenden Code zu ändern oder zu brechen.
4. **Teamarbeit**: Klar definierte Muster erleichtern es Teams, sich in bestehende Codebasen einzuarbeiten und an einem Projekt zu arbeiten.
5. **Effizienz**: Durch die Verwendung optimierter Lösungen lassen sich häufige Probleme schneller und eleganter lösen.



## Creational Patterns

Diese Muster befassen sich mit der Erzeugung von Objekten. Im Kontext von Data Science helfen sie, Objekte wie Datenquellen oder Datenverarbeitungsmodelle auf flexible Weise zu erzeugen.

### **Factory Pattern: Erzeugen von Datenverarbeitungsobjekten**

Das Factory Pattern wird verwendet, um Objekte zu erstellen, ohne die genauen Klassen anzugeben. In Data Science können wir es verwenden, um unterschiedliche Datenquellen (z.B. CSV, SQL, API) mit einer einheitlichen Methode zu erstellen.

**Beispiel: Factory Pattern für Datenquellen**

```python
class DatenQuelleFactory:
    def erstelle_datenquelle(self, typ, **kwargs):
        if typ == 'csv':
            return CSVQuelle(kwargs['dateipfad'])
        elif typ == 'sql':
            return SQLQuelle(kwargs['verbindungsstring'], kwargs['query'])
        elif typ == 'api':
            return APIQuelle(kwargs['url'])

# Verwendung
factory = DatenQuelleFactory()
datenquelle = factory.erstelle_datenquelle('csv', dateipfad='daten.csv')
```

### **Singleton Pattern: Sicherstellen, dass nur eine Datenbankverbindung existiert**

Das Singleton Pattern wird verwendet, um sicherzustellen, dass eine Klasse nur eine einzige Instanz hat. Bei der Verbindung zu Datenbanken ist es oft sinnvoll, nur eine Verbindung offen zu halten, um Ressourcen zu schonen.

**Beispiel: Singleton Pattern für Datenbankverbindung**

```python
class Datenbankverbindung:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Datenbankverbindung, cls).__new__(cls)
            # Simulierte Verbindung
            cls._instance.verbindung = "SQL Datenbank Verbindung"
        return cls._instance

# Verwendung
verbindung1 = Datenbankverbindung()
verbindung2 = Datenbankverbindung()

print(verbindung1 is verbindung2)  # True
```



## Structural Patterns

Diese Muster befassen sich mit der Strukturierung von Klassen und Objekten und deren Zusammensetzung.

### **Adapter Pattern: Anpassung verschiedener Datenquellen an eine einheitliche API**

Das Adapter Pattern hilft, Schnittstellen inkompatibler Klassen anzupassen, ohne die Klassen selbst zu verändern. In Data Science können wir dieses Muster nutzen, um verschiedene Datenquellen (z.B. CSV, SQL, APIs) so anzupassen, dass sie alle mit derselben API angesprochen werden können.

**Beispiel: Adapter Pattern für Datenquellen**

```python
class CSVAdapter:
    def __init__(self, csv_quelle):
        self.csv_quelle = csv_quelle

    def lade_daten(self):
        return self.csv_quelle.lade_daten()

class SQLAdapter:
    def __init__(self, sql_quelle):
        self.sql_quelle = sql_quelle

    def lade_daten(self):
        return self.sql_quelle.lade_daten()

# Jetzt können beide Quellen mit der gleichen Methode verwendet werden
```

### **Decorator Pattern: Erweiterung von Datenverarbeitungsfunktionen (z.B. Logging)**

Mit dem Decorator Pattern können wir bestehenden Funktionen zusätzliche Funktionalitäten hinzufügen, ohne sie zu verändern. Beispielsweise könnten wir eine Datenverarbeitungsfunktion erweitern, um automatisch Log-Einträge zu erstellen.

**Beispiel: Decorator für Logging in Pandas**

```python
def log_verarbeitung(funktion):
    def wrapper(*args, **kwargs):
        print(f"Start der Verarbeitung: {funktion.__name__}")
        ergebnis = funktion(*args, **kwargs)
        print(f"Ende der Verarbeitung: {funktion.__name__}")
        return ergebnis
    return wrapper

@log_verarbeitung
def bereinige_daten(daten):
    # Simulierte Bereinigung
    return daten.dropna()

# Verwendung
daten = pd.DataFrame({"Alter": [25, None, 47], "Geschlecht": ['männlich', 'weiblich', None]})
bereinige_daten(daten)
```



## Behavioral Patterns

Behavioral Patterns befassen sich mit der Interaktion zwischen Objekten und der Zuweisung von Verantwortlichkeiten.

### **Observer Pattern: Ereignisgesteuerte Updates für große Datenverarbeitungen**

Das Observer Pattern ermöglicht es Objekten, auf Änderungen oder Ereignisse zu reagieren. In Data Science Projekten können wir dieses Muster verwenden, um bestimmte Aktionen automatisch auszuführen, wenn Daten sich ändern, z.B. bei Live-Datenverarbeitungen oder Dashboards.

**Beispiel: Observer Pattern für Datenverarbeitung**

```python
class Beobachter:
    def update(self, daten):
        pass

class LoggingBeobachter(Beobachter):
    def update(self, daten):
        print(f"Neue Daten verarbeitet: {daten}")

class DatenVerarbeiter:
    def __init__(self):
        self.beobachter = []

    def hinzufuegen_beobachter(self, beobachter):
        self.beobachter.append(beobachter)

    def verarbeite(self, daten):
        # Simulierte Datenverarbeitung
        for beobachter in self.beobachter:
            beobachter.update(daten)

# Verwendung
verarbeiter = DatenVerarbeiter()
verarbeiter.hinzufuegen_beobachter(LoggingBeobachter())
verarbeiter.verarbeite(pd.DataFrame({"Alter": [25, 32, 47]}))
```

### **Strategy Pattern: Austauschbare Algorithmen für die Datenanalyse**

Das Strategy Pattern ermöglicht es, Algorithmen zur Laufzeit auszutauschen, ohne den restlichen Code zu ändern. In Data Science Projekten kann dies verwendet werden, um unterschiedliche Machine Learning Modelle dynamisch zu laden und anzuwenden.

**Beispiel: Strategy Pattern für Machine Learning Modelle**

```python
class ModellStrategie:
    def trainiere(self, daten):
        pass

class LineareRegression(ModellStrategie):
    def trainiere(self, daten):
        print("Training mit Linearer Regression")

class Entscheidungsbaum(ModellStrategie):
    def trainiere(self, daten):
        print("Training mit Entscheidungsbaum")

class ModellTrainer:
    def __init__(self, strategie: ModellStrategie):
        self.strategie = strategie

    def setze_strategie(self, strategie: ModellStrategie):
        self.strategie = strategie

    def trainiere(self, daten):
        self.strategie.trainiere(daten)

# Verwendung
trainer = ModellTrainer(LineareRegression())
trainer.trainiere(pd.DataFrame({"Feature1": [1, 2, 3], "Ziel": [1, 0, 1]}))

# Strategie ändern
trainer.setze_strategie(Entscheidungsbaum())
trainer.trainiere(pd.DataFrame({"Feature1": [1, 2, 3], "Ziel": [1, 0, 1]}))
```



## Praktische Implementierung von Design Patterns in Python

Python bietet durch seine dynamische Natur und flexiblen Sprachfeatures viele Möglichkeiten, Design Patterns einfach zu implementieren. Eine Herausforderung dabei ist, dass Python weniger strikte Typensysteme als andere Sprachen hat, was zu weniger offensichtlichen Fehlern führen kann. Die konsequente Verwendung von Patterns kann hier helfen, Struktur und Sicherheit in Projekte zu bringen.
