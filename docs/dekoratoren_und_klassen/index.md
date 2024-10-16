# Dekoratoren und Klassen

## Klassen in Python – Eine Wiederholung

Klassen bieten uns eine strukturierte Methode, um Daten und Funktionen zu organisieren und zu kapseln, was insbesondere bei größeren Projekten von Vorteil ist.

#### Anwendung von Klassen im Projektrahmen

Klassen ermöglichen es uns, verschiedene Aspekte eines Projekts logisch zu strukturieren. Nehmen wir als Beispiel einen Discounter: Hier können Klassen genutzt werden, um Kundenprofile, Produktinformationen oder Verkaufsdaten systematisch zu organisieren. Das sorgt für einen übersichtlichen und wiederverwendbaren Code.

**Beispiele:**

1. **Kunde-Klasse zur Verwaltung von Kundendaten:**

```python
class Kunde:
    def __init__(self, kunden_id, name, einkaufsverhalten):
        self.kunden_id = kunden_id
        self.name = name
        self.einkaufsverhalten = einkaufsverhalten
    
    def berechne_gesamtumsatz(self):
        return sum(self.einkaufsverhalten)

kunde1 = Kunde(101, "Max Mustermann", [23.50, 15.75, 9.99])
print(kunde1.berechne_gesamtumsatz())
```

Diese Klasse verwaltet Kundendaten und berechnet den Gesamtumsatz eines Kunden. Dies hilft, Kundenprofile effizient zu analysieren.

2. **Produkt-Klasse zur Verwaltung von Produktinformationen:**

```python
class Produkt:
    def __init__(self, produkt_id, name, preis, lagerbestand):
        self.produkt_id = produkt_id
        self.name = name
        self.preis = preis
        self.lagerbestand = lagerbestand
    
    def aktualisiere_lagerbestand(self, verkaufte_menge):
        self.lagerbestand -= verkaufte_menge
```

Mit dieser Klasse können wir Informationen über Produkte verwalten und den Lagerbestand nach Verkäufen aktualisieren.

3. **Verkauf-Klasse für Transaktionsmanagement:**

```python
class Verkauf:
    def __init__(self):
        self.transaktionen = []
    
    def fuege_transaktion_hinzu(self, produkt, menge, preis):
        self.transaktionen.append({'produkt': produkt, 'menge': menge, 'preis': preis})
    
    def berechne_gesamtumsatz(self):
        return sum(t['menge'] * t['preis'] for t in self.transaktionen)
```

Diese Klasse speichert Verkaufsdaten und berechnet den Gesamtumsatz aller Transaktionen, was für die Zusammenstellung von Verkaufsberichten nützlich ist.

#### Aufgaben zum Vertiefen des Verständnisses

1. **Erweitern der Produktklasse:**
   Ergänzen wir die `Produkt`-Klasse um eine Methode, die den Lagerbestand nach einer Rückgabe aktualisiert.

2. **Analyse des Einkaufsverhaltens:**
   Modifizieren wir die `Kunde`-Klasse, um eine Methode zu implementieren, die eine Liste der am häufigsten gekauften Produkte ausgibt.

3. **Entwicklung eines Rabatt-Systems:**
   Erstellen wir eine neue Klasse `Rabatt`, die verschiedene Rabattstrategien für Produkte implementiert und auf den Gesamtumsatz angewendet werden kann.
