# Abstrakte Klassen und Schnittstellen

In der objektorientierten Programmierung bieten abstrakte Klassen und Schnittstellen (Interfaces) ein mächtiges Werkzeug, um wiederverwendbare und strukturierte Software-Architekturen zu gestalten. Sie ermöglichen es uns, generische Verarbeitungslogiken zu definieren, die dann von spezialisierteren Klassen erweitert und angepasst werden können. Insbesondere in Data Science Projekten, in denen oft mehrere unterschiedliche Datenquellen oder Verarbeitungsschritte zu verwalten sind, erleichtern abstrakte Klassen und Schnittstellen die Erstellung flexibler Pipelines.

## Was ist eine abstrakte Klasse?

Eine abstrakte Klasse dient als Vorlage für andere Klassen und kann nicht direkt instanziiert werden. Sie enthält in der Regel abstrakte Methoden, die von den abgeleiteten Klassen implementiert werden müssen. Abstrakte Klassen bieten uns die Möglichkeit, allgemeine Funktionalitäten zu definieren, die von den spezialisierten Klassen konkretisiert werden.

Im Data Science Kontext kann man sich eine abstrakte Klasse als allgemeine Beschreibung eines Verarbeitungsschrittes oder einer Datenquelle vorstellen. Zum Beispiel könnten alle Datenquellen (CSV-Dateien, SQL-Datenbanken, APIs) eine gemeinsame Methode zur Datenbeschaffung haben, die in der abstrakten Klasse definiert, aber in den abgeleiteten Klassen unterschiedlich implementiert wird.



**Beispiel: Abstrakte Klasse für Datenquellen**

```python
from abc import ABC, abstractmethod
import pandas as pd

class DatenQuelle(ABC):
    @abstractmethod
    def lade_daten(self):
        pass

class CSVQuelle(DatenQuelle):
    def __init__(self, dateipfad):
        self.dateipfad = dateipfad
    
    def lade_daten(self):
        return pd.read_csv(self.dateipfad)

class SQLQuelle(DatenQuelle):
    def __init__(self, verbindungsstring, query):
        self.verbindungsstring = verbindungsstring
        self.query = query
    
    def lade_daten(self):
        # Simuliert den SQL-Datenabruf
        return pd.DataFrame({"Spalte1": [1, 2], "Spalte2": [3, 4]})
```

In diesem Beispiel haben wir eine abstrakte Klasse `DatenQuelle` definiert, die die abstrakte Methode `lade_daten()` enthält. Diese Methode wird in den spezialisierten Klassen `CSVQuelle` und `SQLQuelle` implementiert, die die konkrete Logik zum Laden der Daten aus der jeweiligen Quelle bereitstellen.



## Schnittstellen in Python

Während Python keine echten "Interfaces" wie andere Sprachen (z.B. Java) hat, können wir durch den Einsatz abstrakter Klassen und Methoden ähnliche Strukturen schaffen. Schnittstellen definieren lediglich die Methoden, die eine Klasse implementieren muss, ohne dabei Logik vorzugeben. Sie fördern lose Kopplung und machen Code flexibler und einfacher erweiterbar.

Nehmen wir ein Data Science Pipeline Szenario: Unterschiedliche Schritte wie "Vorverarbeitung", "Feature Engineering" und "Modellierung" können durch Schnittstellen abstrahiert werden, um sicherzustellen, dass jede Klasse die gleichen Methoden implementiert, während die Details unterschiedlich sind.



**Beispiel: Abstrakte Klasse für eine Pipeline**

```python
class Verarbeitungsschritt(ABC):
    @abstractmethod
    def verarbeite(self, daten: pd.DataFrame) -> pd.DataFrame:
        pass

class Skalierung(Verarbeitungsschritt):
    def verarbeite(self, daten: pd.DataFrame) -> pd.DataFrame:
        return (daten - daten.mean()) / daten.std()

class KategorischeKodierung(Verarbeitungsschritt):
    def verarbeite(self, daten: pd.DataFrame) -> pd.DataFrame:
        return pd.get_dummies(daten)
```

Hier definiert die abstrakte Klasse `Verarbeitungsschritt` die Methode `verarbeite()`, die für jeden Schritt der Datenverarbeitung implementiert werden muss. Die spezialisierte Klasse `Skalierung` führt z.B. eine Standardisierung der Daten durch, während `KategorischeKodierung` eine One-Hot-Encoding-Transformation anwendet.



## Verwendung von abstrakten Klassen in Data Science Pipelines

In komplexen Data Science Projekten können abstrakte Klassen dazu beitragen, einzelne Verarbeitungsschritte und Datenquellen standardisiert zu behandeln. Dadurch wird es einfacher, neue Schritte oder Datenquellen hinzuzufügen, ohne den bestehenden Code ändern zu müssen. Diese Flexibilität ist besonders nützlich, wenn man mit verschiedenen Datensätzen oder Modellen arbeitet.



**Beispiel: Flexible Pipeline mit abstrakten Klassen**

```python
class Pipeline:
    def __init__(self):
        self.schritte = []
    
    def hinzufuegen_schritt(self, schritt: Verarbeitungsschritt):
        self.schritte.append(schritt)
    
    def ausfuehren(self, daten: pd.DataFrame) -> pd.DataFrame:
        for schritt in self.schritte:
            daten = schritt.verarbeite(daten)
        return daten

# Pipeline erstellen
pipeline = Pipeline()
#pipeline.hinzufuegen_schritt(Skalierung()) #Funktioniert nur bei numerischen Daten
pipeline.hinzufuegen_schritt(KategorischeKodierung())

# Beispiel-Daten
daten = pd.DataFrame({
    'Alter': [25, 32, 47],
    'Geschlecht': ['männlich', 'weiblich', 'männlich']
})

# Pipeline ausführen
verarbeitete_daten = pipeline.ausfuehren(daten)
print(verarbeitete_daten)
```

Hier fügen wir verschiedene Verarbeitungsschritte zur Pipeline hinzu und führen sie auf die Daten aus. Dies zeigt die Stärke der Abstraktion: Wir können leicht neue Schritte zur Pipeline hinzufügen, ohne den Rest des Codes ändern zu müssen.



## Aufgaben

1. **Abstrakte Klassen erweitern**:  
   Implementiere eine weitere Klasse `APIZugriff`, die von `DatenQuelle` erbt und Daten aus einer API lädt (du kannst den API-Zugriff simulieren, indem du ein statisches DataFrame zurückgibst).

2. **Neue Verarbeitungsschritte**:  
   Erstelle einen neuen Verarbeitungsschritt `Normalisierung`, der eine Min-Max-Normalisierung auf numerische Daten anwendet und ihn zur bestehenden Pipeline hinzufügt.

3. **Verwende die Pipeline mit verschiedenen Datenquellen**:  
   Implementiere die Pipeline so, dass sie mit Daten aus verschiedenen Quellen (`CSVQuelle`, `SQLQuelle`) flexibel arbeiten kann.

