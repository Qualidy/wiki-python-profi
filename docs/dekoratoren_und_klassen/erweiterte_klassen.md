
### Erweiterte Konzepte in Python-Klassen

Nachdem wir die Grundlagen von Klassen besprochen haben, wenden wir uns nun einigen fortgeschrittenen Themen zu. Diese Konzepte ermöglichen eine noch effektivere Strukturierung und Wiederverwendbarkeit unseres Codes.

#### Classmethods

Classmethods bieten uns die Möglichkeit, Methoden zu erstellen, die auf die Klasse selbst anstatt auf eine Instanz angewendet werden. Dies ist nützlich, wenn wir Konstruktoren oder alternative Initialisierungsmethoden benötigen.

**Beispiele:**

1. **Produkt aus String erstellen:**

   ```python
   class Produkt:
       produktzaehler = 0

       def __init__(self, name, preis):
           self.name = name
           self.preis = preis
           Produkt.produktzaehler += 1

       @classmethod
       def erstelle_aus_string(cls, produkt_string):
           name, preis = produkt_string.split(',')
           return cls(name, float(preis))

   neues_produkt = Produkt.erstelle_aus_string("Kaffee,3.99")
   ```

   Hier verwenden wir eine Classmethod, um ein `Produkt` aus einer kommagetrennten Zeichenkette zu erstellen.

2. **Zähler für erstellte Instanzen:**

   ```python
   class Produkt:
       instanz_zaehler = 0

       def __init__(self, name, preis):
           self.name = name
           self.preis = preis
           Produkt.instanz_zaehler += 1

       @classmethod
       def gib_anzahl_erstellt(cls):
           return cls.instanz_zaehler

   produkt1 = Produkt("Brot", 1.50)
   produkt2 = Produkt("Milch", 0.99)
   print(Produkt.gib_anzahl_erstellt())
   ```

   Diese Methode zählt die Anzahl der erstellten Instanzen der Klasse.

#### Abstrakte Klassen

Abstrakte Klassen dienen als Blaupause für andere Klassen. Sie enthalten abstrakte Methoden, die in abgeleiteten Klassen implementiert werden müssen.

**Beispiele:**

1. **Rabattstrategie Implementierung:**

   ```python
   from abc import ABC, abstractmethod

   class RabattStrategie(ABC):
       
       @abstractmethod
       def berechne_rabatt(self, betrag):
           pass

   class ProzentualerRabatt(RabattStrategie):
       def berechne_rabatt(self, betrag):
           return betrag * 0.90  # 10% Rabatt
   ```

   Hier definieren wir eine abstrakte Klasse `RabattStrategie` und implementieren eine prozentuale Rabattstrategie.

2. **Zahlungsmethoden-Plattform:**

   ```python
   class Zahlungsplattform(ABC):
       
       @abstractmethod
       def verarbeite_zahlung(self, betrag):
           pass

   class Kreditkarte(Zahlungsplattform):
       def verarbeite_zahlung(self, betrag):
           print(f"Zahlung von {betrag} per Kreditkarte verarbeitet.")
   ```

   Diese abstrakte Klasse definiert eine `Zahlungsplattform`, die von spezifischen Zahlungsarten wie `Kreditkarte` abgeleitet wird.

#### Mixins

Mixins sind Klassen, die kleine Funktionen bereitstellen, die von verschiedenen Klassen geteilt werden können. Sie sind nützlich, um wiederverwendbaren Code zu erstellen, ohne komplexe Erbstrukturen.

**Beispiele:**

1. **LogMixin für verschiedene Klassen:**

   ```python
   class LogMixin:
       def log(self, nachricht):
           print(f"Log: {nachricht}")

   class Bestandsverwaltung(LogMixin):
       def aktualisiere_bestand(self, menge):
           # Bestandslogik
           self.log(f"Bestand um {menge} Einheiten aktualisiert.")
   ```

   `LogMixin` ermöglicht das Hinzufügen von Logging-Funktionen zu jeder Klasse.

2. **Benachrichtigungs-Mixin:**

   ```python
   class BenachrichtigungMixin:
       def sende_benachrichtigung(self, nachricht):
           print(f"Benachrichtigung: {nachricht}")

   class Bestellung(BenachrichtigungMixin):
       def abschliessen(self):
           # Bestellung abschließen
           self.sende_benachrichtigung("Bestellung erfolgreich abgeschlossen.")
   ```

   Dieses Mixin bietet eine Benachrichtigungsfunktion, die in mehreren Klassen verwendet werden kann.

#### Dataclasses

Dataclasses vereinfachen die Erstellung von Klassen, die hauptsächlich der Datenhaltung dienen, indem sie automatisch Methoden wie `__init__`, `__repr__` und `__eq__` generieren.

**Beispiele:**

1. **Einfache Produkt-Dataclass:**

   ```python
   from dataclasses import dataclass

   @dataclass
   class Produkt:
       name: str
       preis: float
       lagerbestand: int

   produkt1 = Produkt("Tee", 2.99, 100)
   ```

   Hier nutzen wir eine Dataclass, um schnell eine `Produkt`-Klasse zu erstellen, ohne Boilerplate-Code zu schreiben.

2. **Erweiterte Dataclass mit Methode:**

   ```python
   @dataclass
   class Kunde:
       name: str
       einkaufsverhalten: list

       def gesamtumsatz(self) -> float:
           return sum(self.einkaufsverhalten)

   kunde1 = Kunde("Anna", [10.99, 20.50, 5.99])
   print(kunde1.gesamtumsatz())
   ```

   Diese Dataclass enthält eine Methode zur Berechnung des Gesamtumsatzes.

#### Aufgaben

1. **Implementierung einer Klassmethoden-Fabrik:**
   Erstellen wir eine Classmethod in der `Produkt`-Klasse, die eine Liste von Produkten aus einer Liste von Strings initialisiert.

2. **Entwicklung eines Rabattsystems:**
   Implementieren wir eine weitere `RabattStrategie`, die einen prozentualen Rabatt gewährt und testen diese in einer Einkaufsumgebung.

3. **Logik mit Mixins erweitern:**
   Fügen wir einem bestehenden System ein Mixin hinzu, das erweiterte Protokollierungsfunktionen bietet, und verwenden es in mehreren Klassen.

