# Optimierung von Python-Code

Die Effizienz unseres Python-Codes hat einen direkten Einfluss auf die Leistung unserer Anwendungen. Durch die Auswahl geeigneter Algorithmen und Datenstrukturen können wir nicht nur die Ausführungsgeschwindigkeit unserer Programme verbessern, sondern auch deren Lesbarkeit und Wartbarkeit erhöhen. Lass uns einige Beispiele für sowohl ineffizienten als auch effizienten Code betrachten.

## Verwendung von `lru_cache`

Der `lru_cache`-Dekorator aus dem `functools`-Modul ist ein Tools, mit dem wir die Leistung von Funktionen zu steigern, die häufig mit denselben Argumenten aufgerufen werden. Er speichert die Ergebnisse von Funktionsaufrufen und gibt sie zurück, wenn die Funktion erneut mit denselben Argumenten aufgerufen wird, wodurch unnötige Berechnungen vermieden und die Ausführungszeit reduziert wird.

### Beispiel

Unten siehst du ein Beispiel zur Berechnung von Fibonacci-Zahlen. Ohne `lru_cache` wird die Fibonacci-Sequenz rekursiv berechnet, was zu einer exponentiellen Laufzeit führt. Mit `lru_cache` werden die Ergebnisse zwischengespeichert, was die Berechnungen erheblich beschleunigt.

```python
from functools import lru_cache

# Fibonacci-Zahlen ohne lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Ausgabe: 55

# Fibonacci-Zahlen mit lru_cache
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

print(fibonacci_cached(10))  # Ausgabe: 55
```

Dieses Beispiel verdeutlicht den Unterschied zwischen der Berechnung von Fibonacci-Zahlen mit und ohne `lru_cache`. Die zwischengespeicherte Version ist aufgrund der Wiederverwendung zuvor berechneter Ergebnisse wesentlich schneller.

### 1. Beispiele für ineffizienten und effizienten Code

#### Beispiel 1: Ineffiziente Schleifen

**Ineffizienter Code**:

Hier wird eine Schleife verwendet, um die Summe aller geraden Zahlen in einer Liste mit einer Methode zu berechnen, die unnötige Überprüfungen durchführt.

```python
def sum_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

# Beispielaufruf
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(zahlen))  # Ausgabe: 30
```

**Effizienter Code**:

Mit List Comprehensions können wir die Summe der geraden Zahlen effizienter und übersichtlicher berechnen.

```python
def sum_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)

# Beispielaufruf
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(zahlen))  # Ausgabe: 30
```

### 2. Beispiel 2: Verwendung von Datenstrukturen

**Ineffizienter Code**:

Dieses Beispiel verwendet eine Liste, um doppelte Werte zu finden, was eine hohe Zeitkomplexität aufweist, da die Liste mehrfach durchlaufen werden muss.

```python
def find_duplicates(values):
    duplicates = []
    for value in values:
        if values.count(value) > 1 and value not in duplicates:
            duplicates.append(value)
    return duplicates

# Beispielaufruf
werte = [1, 2, 3, 1, 2, 4, 5]
print(find_duplicates(werte))  # Ausgabe: [1, 2]
```

**Effizienter Code**:

Hier nutzen wir ein Set, um Duplikate effizient zu finden, da Sets schnelle Mitgliedschaftstests bieten.

```python
def find_duplicates(values):
    seen = set()
    duplicates = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    return list(duplicates)

# Beispielaufruf
werte = [1, 2, 3, 1, 2, 4, 5]
print(find_duplicates(werte))  # Ausgabe: [1, 2]
```

### 3. Aufgaben

Jetzt sind wir an der Reihe! In den folgenden Aufgaben bitten wir dich, den schlechten Code zu verbessern, um die Effizienz und Lesbarkeit zu steigern.

#### Aufgabe 1: Schleifenoptimierung

Hier ist ein ineffizienter Code, der die Summe aller Zahlen in einer Liste berechnet. Verbessere ihn, indem du die Schleife optimierst.

```python
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Beispielaufruf
zahlen = [1, 2, 3, 4, 5]
print(sum_numbers(zahlen))  # Ausgabe: 15
```

#### Aufgabe 2: Nutzung von Sets

In diesem Beispiel wird eine Liste verwendet, um die einzigartigen Werte aus einer anderen Liste zu extrahieren. Optimiere den Code, indem du Sets verwendest.

```python
def unique_values(values):
    unique = []
    for value in values:
        if value not in unique:
            unique.append(value)
    return unique

# Beispielaufruf
werte = [1, 2, 2, 3, 4, 4, 5]
print(unique_values(werte))  # Ausgabe: [1, 2, 3, 4, 5]
```

### Ineffiziente und effiziente Pandas-Codes

#### Beispiel 1: Ineffiziente Nutzung von Schleifen

**Ineffizienter Code**:

Diese Schleife berechnet die Quadratwerte einer Spalte, was ineffizient ist, da Pandas die Vektorisierung unterstützt.

```python
import pandas as pd

# Beispiel-DataFrame erstellen
df = pd.DataFrame({'Zahlen': [1, 2, 3, 4, 5]})

# Schleife zur Berechnung der Quadratwerte
squares = []
for i in range(len(df)):
    squares.append(df['Zahlen'][i] ** 2)

df['Quadrate'] = squares
print(df)
```

**Effizienter Code**:

Hier verwenden wir die Vektorisierung von Pandas, um die Quadratwerte effizient und übersichtlich zu berechnen.

```python
# Vektorisierung zur Berechnung der Quadratwerte
df['Quadrate'] = df['Zahlen'] ** 2
print(df)
```

### Beispiel 2: Mehrfache Berechnungen in einer Schleife

**Ineffizienter Code**:

Diese Schleife berechnet die durchschnittlichen Punktzahlen, was ineffizient ist, da die Berechnungen wiederholt werden.

```python
# Beispiel-DataFrame erstellen
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Punkte1': [10, 20, 30],
                   'Punkte2': [15, 25, 35]})

# Durchschnittliche Punktzahlen berechnen
averages = []
for i in range(len(df)):
    avg = (df['Punkte1'][i] + df['Punkte2'][i]) / 2
    averages.append(avg)

df['Durchschnitt'] = averages
print(df)
```

**Effizienter Code**:

Wir berechnen die durchschnittlichen Punktzahlen effizient, indem wir die Vektorisierung nutzen.

```python
# Vektorisierung zur Berechnung der durchschnittlichen Punktzahlen
df['Durchschnitt'] = (df['Punkte1'] + df['Punkte2']) / 2
print(df)
```

### Beispiel 3: Unnötige Verwendung von `reset_index()`

**Ineffizienter Code**:

Hier wird `reset_index()` mehrfach unnötig verwendet, was die Performance beeinträchtigt.

```python
# Beispiel-DataFrame erstellen
df = pd.DataFrame({'Abteilung': ['A', 'B', 'A', 'B'],
                   'Gehalt': [50000, 60000, 70000, 80000]})

# Gruppierung und reset_index() mehrmals aufrufen
grouped = df.groupby('Abteilung')['Gehalt'].mean()
grouped_reset = grouped.reset_index()
print(grouped_reset)
```

**Effizienter Code**:

Vermeiden wir das unnötige Zurücksetzen des Index, indem wir die Aggregation direkt im DataFrame durchführen.

```python
# Gruppierung ohne unnötige reset_index()
grouped = df.groupby('Abteilung')['Gehalt'].mean().reset_index()
print(grouped)
```
### Aufgabe
### Aufgabe 3: Ineffiziente Filterung von DataFrames

**Ineffizienter Code**:

Dieser Code verwendet `apply()`, um Daten zu filtern, was ineffizient ist, da es eine Schleife über alle Zeilen erfordert.

```python
# Beispiel-DataFrame erstellen
df = pd.DataFrame({'Alter': [25, 30, 35, 40, 45]})

# Schleifenbasierte Filterung
filtered = df[df.apply(lambda row: row['Alter'] > 30, axis=1)]
print(filtered)
```

Optimiere den Code, indem du die Vektorisierung nutzt.