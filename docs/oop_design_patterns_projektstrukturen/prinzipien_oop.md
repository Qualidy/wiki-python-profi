# Grundprinzipien der OOP

Die objektorientierte Programmierung (OOP) basiert auf vier zentralen Prinzipien, die den Umgang mit komplexen Datenstrukturen und Prozessen effizienter gestalten: Abstraktion, Kapselung, Vererbung und Polymorphismus. Diese Prinzipien ermöglichen es uns, sauberen, wiederverwendbaren und leicht wartbaren Code zu schreiben.



## Abstraktion

Abstraktion bedeutet, dass nur die wesentlichen Informationen eines Objekts dargestellt werden, während unnötige Details verborgen bleiben. In der Praxis ermöglicht Abstraktion die Reduzierung von Komplexität, indem wir uns auf die wichtigen Eigenschaften und Funktionen eines Objekts konzentrieren.

**Beispiel:**

```python
from abc import ABC, abstractmethod

class ZahlungsMethode(ABC):
    @abstractmethod
    def zahlen(self, betrag):
        pass

class Kreditkarte(ZahlungsMethode):
    def zahlen(self, betrag):
        print(f"Bezahlung von {betrag}€ mit Kreditkarte")

class PayPal(ZahlungsMethode):
    def zahlen(self, betrag):
        print(f"Bezahlung von {betrag}€ mit PayPal")
```

Hier stellt die abstrakte Klasse `ZahlungsMethode` die allgemeine Idee der Zahlung dar, ohne auf spezifische Implementierungen einzugehen. Die konkreten Zahlungsarten wie Kreditkarte und PayPal werden von ihr abgeleitet und implementieren die `zahlen`-Methode auf unterschiedliche Weise.

**Aufgabe:**
Erstelle eine abstrakte Klasse `Fahrzeug` mit der abstrakten Methode `fahren()`. Implementiere zwei konkrete Klassen, `Auto` und `Fahrrad`, die jeweils `fahren()` spezifisch umsetzen.



## Kapselung

Kapselung bezieht sich auf das Verbergen von Daten und die Einschränkung des Zugriffs auf bestimmte Teile eines Objekts. Dies schützt die internen Zustände und verhindert unbeabsichtigte Änderungen.

**Beispiel:**

```python
class Konto:
    def __init__(self, saldo):
        self.__saldo = saldo  # private Variable

    def einzahlen(self, betrag):
        self.__saldo += betrag

    def get_saldo(self):
        return self.__saldo

konto = Konto(1000)
konto.einzahlen(500)
print(konto.get_saldo())  # Ausgabe: 1500
```

In diesem Beispiel ist das Attribut `__saldo` privat und kann nicht direkt von außen verändert werden. Der Zugriff erfolgt über die Methode `get_saldo()`.

**Aufgabe:**
Erstelle eine Klasse `Benutzer`, die den Namen und das Passwort eines Benutzers kapselt. Das Passwort soll nur innerhalb der Klasse sichtbar sein, aber durch eine Methode geändert werden können.



## Vererbung

Vererbung erlaubt es uns, eine Klasse von einer anderen abzuleiten, sodass die abgeleitete Klasse die Eigenschaften und Methoden der Basisklasse erbt. Dies fördert die Wiederverwendbarkeit von Code.

**Beispiel:**

```python
class Fahrzeug:
    def __init__(self, marke):
        self.marke = marke

    def fahren(self):
        print(f"{self.marke} fährt los")

class Auto(Fahrzeug):
    def hupen(self):
        print(f"{self.marke} hupt")

auto = Auto("BMW")
auto.fahren()  # Ausgabe: BMW fährt los
auto.hupen()   # Ausgabe: BMW hupt
```

Hier erbt die Klasse `Auto` die Methode `fahren` von der Basisklasse `Fahrzeug` und erweitert sie um eine eigene Methode `hupen`.

**Aufgabe:**
Erstelle eine Basisklasse `Mitarbeiter` mit der Methode `arbeiten()`. Leite von dieser Klasse `Manager` und `Verkäufer` ab, die beide die Methode `arbeiten()` spezifisch umsetzen.



## Polymorphismus

Polymorphismus ermöglicht es uns, auf unterschiedliche Arten auf dieselbe Methode zuzugreifen, abhängig davon, welches Objekt diese Methode aufruft. Dies erlaubt uns, flexible und austauschbare Code-Strukturen zu schaffen.

**Beispiel:**

```python
class Tier:
    def laut(self):
        pass

class Hund(Tier):
    def laut(self):
        print("Wuff")

class Katze(Tier):
    def laut(self):
        print("Miau")

def tier_geraeusch(tier):
    tier.laut()

hund = Hund()
katze = Katze()

tier_geraeusch(hund)  # Ausgabe: Wuff
tier_geraeusch(katze)  # Ausgabe: Miau
```

In diesem Beispiel rufen sowohl `Hund` als auch `Katze` die Methode `laut()` auf, aber mit unterschiedlichen Implementierungen.

**Aufgabe:**
Erstelle eine Funktion `rechnen()`, die mit verschiedenen Objekten von Rechenklassen (z.B. `Addition`, `Subtraktion`) arbeitet, die jeweils eine Methode `berechnen()` besitzen. Implementiere zwei Klassen, die jeweils die Berechnung spezifisch umsetzen.
