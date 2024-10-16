# Effizienter Code und Arbeitsspeicherressourcen

In unserer täglichen Arbeit mit Daten ist Effizienz von entscheidender Bedeutung. Egal, ob wir große Datensätze analysieren, Modelle trainieren oder interaktive Dashboards erstellen – effizienter Code und der sparsame Umgang mit Arbeitsspeicherressourcen machen den Unterschied zwischen einem reibungslosen Workflow und Performance-Problemen aus. In diesem Kapitel betrachten wir Python-Optimierungen, die uns helfen, sowohl schneller als auch ressourcenschonender zu arbeiten.

Effizienter Code bedeutet nicht nur Geschwindigkeit, sondern auch Klarheit und Wartbarkeit. Besonders in der Datenanalyse und beim maschinellen Lernen, wo riesige Datenmengen verarbeitet werden, ist es wichtig, den Arbeitsspeicher nicht unnötig zu belasten. Zwei Hauptfaktoren sind entscheidend: die Algorithmen, die wir verwenden, und die Datenstrukturen, die wir wählen. Dieses Kapitel zeigt, wie wir diese Ressourcen optimal nutzen können.

## Stellschrauben zur Erhöhung der Effizienz

Um die Effizienz unserer Python-Programme zu steigern, gibt es mehrere Ansatzpunkte:

### Algorithmische Effizienz

Die Wahl des richtigen Algorithmus hat den größten Einfluss auf die Effizienz eines Programms.

- **Analyse der Zeitkomplexität**: Wir sollten die Zeitkomplexität von Algorithmen überprüfen und solche mit niedrigerer Komplexität (z. B. O(n log n) statt O(n²)) bevorzugen.

- **Geeignete Algorithmen verwenden**: Oft bieten spezialisierte Bibliotheken optimierte Algorithmen an. Zum Beispiel ist die `sorted()`-Funktion in Python meist schneller als eigene Sortierfunktionen.

```python
zahlen = [5, 2, 9, 1, 5, 6]
sortierte_zahlen = sorted(zahlen)
print(sortierte_zahlen)  # Ausgabe: [1, 2, 5, 5, 6, 9]
```

### Effiziente Datenstrukturen

Die Wahl der richtigen Datenstruktur kann die Effizienz erheblich beeinflussen.

- **Listen vs. Sets vs. Dictionaries**: Sets eignen sich gut, um Duplikate zu vermeiden und schnelle Mitgliedschaftstests durchzuführen. Dictionaries bieten schnellen Zugriff auf Werte über Schlüssel.

```python
preise = {"Apfel": 1.20, "Banane": 0.50, "Orange": 0.80}
print(preise["Banane"])  # Ausgabe: 0.50
```

- **Arrays für große Datenmengen**: Bei großen numerischen Datensätzen sollten wir Bibliotheken wie `numpy`, `polars` oder `spark` nutzen, die für numerische Berechnungen optimiert sind.

### Minimierung von Kopien

Das Erstellen von Kopien großer Datenstrukturen kann viel Arbeitsspeicher beanspruchen. Wir sollten Kopien vermeiden und stattdessen Referenzen verwenden, wenn möglich.

```python
liste1 = [1, 2, 3]
liste2 = liste1  # liste2 ist eine Referenz auf liste1

liste2[0] = 99
print(liste1)  # Ausgabe: [99, 2, 3]
```

### Profiling und Optimierung

Profiling-Tools helfen uns, Engpässe im Code zu identifizieren. Das `cProfile`-Modul ermöglicht es uns, die Laufzeit von Funktionen zu analysieren und zu optimieren.

```python
import cProfile

def lange_berechnung():
    # Simulierte lange Berechnung
    summe = 0
    for i in range(1000000):
        summe += i
    return summe

cProfile.run('lange_berechnung()')
```

Die Ausgabe von `cProfile` gibt detaillierte Informationen über die Ausführung von Funktionen:

- `ncalls`: Anzahl der Funktionsaufrufe
- `tottime`: Gesamtzeit in der Funktion (ohne Unterfunktionen)
- `percall`: Zeit pro Aufruf
- `cumtime`: Gesamtzeit in der Funktion und ihren Unterfunktionen
- `filename:lineno(function)`: Funktion und ihre Position im Code
