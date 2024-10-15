### SOLID-Prinzipien in Python

Die SOLID-Prinzipien sind eine Sammlung von Designprinzipien, die darauf abzielen, Software leicht wartbar, erweiterbar und stabil zu machen. Sie sind besonders nützlich in größeren Projekten, bei denen es auf sauberen Code und modulare Architektur ankommt. Im Kontext des Einzelhandels – zum Beispiel zur Verwaltung von Verkaufsprozessen, Produkten oder Kunden – helfen sie uns, flexible und erweiterbare Systeme zu bauen.

Die SOLID-Prinzipien sind:
1. **Single Responsibility Principle (SRP)** – Eine Klasse sollte nur eine Verantwortung haben.
2. **Open/Closed Principle (OCP)** – Eine Klasse sollte offen für Erweiterungen, aber geschlossen für Modifikationen sein.
3. **Liskov Substitution Principle (LSP)** – Subklassen sollten ihre Basisklassen ohne Veränderung des Verhaltens ersetzen können.
4. **Interface Segregation Principle (ISP)** – Schnittstellen (Interfaces) sollten klein und spezifisch sein.
5. **Dependency Inversion Principle (DIP)** – Höherwertige Module sollten nicht von niedrigeren Modulen abhängig sein. Beide sollten von Abstraktionen abhängen.



#### 1. Single Responsibility Principle (SRP)

Das SRP besagt, dass jede Klasse nur für eine Aufgabe verantwortlich sein sollte. Dies macht den Code einfacher zu warten und zu erweitern, da Änderungen in einem Bereich nicht zu Nebeneffekten in einem anderen führen.

**Beispiel:**

```python
class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

class ProduktDatenbank:
    def speichere_produkt(self, produkt):
        print(f"{produkt.name} wurde in der Datenbank gespeichert.")
```

Hier hat die Klasse `Produkt` nur die Verantwortung, ein Produkt zu beschreiben. Die Verantwortung für das Speichern in der Datenbank liegt bei der Klasse `ProduktDatenbank`.

**Aufgabe:**  
Ändere den folgenden Code so, dass er das SRP beachtet:

```python
class BestellSystem:
    def verarbeite_bestellung(self, produkt, kunde):
        print(f"{produkt.name} wurde an {kunde.name} verkauft.")
        print(f"Rechnung für {produkt.preis}€ an {kunde.email} gesendet.")
```



#### 2. Open/Closed Principle (OCP)

Das OCP besagt, dass Klassen offen für Erweiterungen, aber geschlossen für Änderungen sein sollten. Das bedeutet, dass wir das Verhalten einer Klasse erweitern können, ohne den bestehenden Code zu verändern.

**Beispiel:**

```python
class Rabatt:
    def berechne_rabatt(self, preis):
        return preis  # Keine Rabatte standardmäßig

class MitgliederRabatt(Rabatt):
    def berechne_rabatt(self, preis):
        return preis * 0.9  # 10% Rabatt für Mitglieder
```

Hier können wir die Rabattlogik erweitern, indem wir neue Rabattarten hinzufügen, ohne den bestehenden Code zu ändern.

**Aufgabe:**  
Erweitere den folgenden Code, um einen "SommerRabatt" zu implementieren, ohne den bestehenden Code zu ändern:

```python
class Rabatt:
    def berechne_rabatt(self, preis):
        return preis
```



#### 3. Liskov Substitution Principle (LSP)

Das LSP besagt, dass Objekte einer Subklasse durch Objekte ihrer Basisklasse ersetzt werden können, ohne das Verhalten zu verändern. Eine Subklasse sollte sich also immer wie ihre Basisklasse verhalten.

**Beispiel:**

```python
class Kunde:
    def zahle(self, betrag):
        print(f"Zahle {betrag}€")

class VIPKunde(Kunde):
    def zahle(self, betrag):
        print(f"Zahle {betrag * 0.8}€ (VIP-Rabatt)")
```

Hier kann ein `VIPKunde` ohne Anpassung der Logik überall dort verwendet werden, wo auch ein `Kunde` verwendet wird.

**Aufgabe:**  
Schreibe eine Klasse `OnlineKunde`, die sich wie `Kunde` verhält, aber zusätzlich eine Liefergebühr berechnet, ohne das LSP zu verletzen.



#### 4. Interface Segregation Principle (ISP)

Das ISP besagt, dass Schnittstellen (Interfaces) klein und spezifisch sein sollten, damit Klassen nur die Methoden implementieren müssen, die sie wirklich benötigen.

**Beispiel:**

```python
class LieferbareProdukte:
    def lieferung_berechnen(self, produkt):
        pass

class AbholbareProdukte:
    def abholung_organisieren(self, produkt):
        pass
```

Hier gibt es separate Schnittstellen für Produkte, die geliefert werden, und solche, die abgeholt werden. Eine Klasse muss also nur die Methoden implementieren, die sie wirklich benötigt.

**Aufgabe:**  
Passe den folgenden Code an, sodass nicht alle Produkte beide Methoden implementieren müssen:

```python
class Produkt:
    def lieferung_berechnen(self):
        pass
    
    def abholung_organisieren(self):
        pass
```



#### 5. Dependency Inversion Principle (DIP)

Das DIP besagt, dass höherwertige Module nicht von spezifischen Implementierungen niedrigerer Module abhängig sein sollten, sondern beide von Abstraktionen abhängen sollten. Dies fördert die Flexibilität und Austauschbarkeit von Komponenten.

**Beispiel:**

```python
class Datenbank:
    def speichere(self, daten):
        pass

class ProduktVerwaltung:
    def __init__(self, datenbank: Datenbank):
        self.datenbank = datenbank

    def speichere_produkt(self, produkt):
        self.datenbank.speichere(produkt)
```

Hier hängt die `ProduktVerwaltung` nur von der abstrakten `Datenbank` ab, sodass die tatsächliche Implementierung (z.B. SQL-Datenbank, In-Memory-Datenbank) leicht austauschbar ist.

**Aufgabe:**  
Ändere den folgenden Code so, dass er das DIP beachtet:

```python
class SQLDatenbank:
    def speichere(self, daten):
        print("Speichern in SQL-Datenbank")

class ProduktVerwaltung:
    def speichere_produkt(self, produkt):
        datenbank = SQLDatenbank()
        datenbank.speichere(produkt)
```
