# Dekoratoren in Python

Mithilfe von Dekoratoren können wir Funktionen oder Klassen flexibel erweitern, ohne deren ursprünglichen Code zu verändern. Sie erlauben es uns, zusätzliche Funktionalitäten hinzuzufügen, was besonders hilfreich ist, um den Quellcode sauberer und modularer zu gestalten.

#### Grundlagen der Dekoratoren

Ein Dekorator ist im Wesentlichen eine Funktion, die eine andere Funktion als Argument akzeptiert und eine neue Funktion zurückgibt. Diese neue Funktion kann den ursprünglichen Funktionsaufruf erweitern oder modifizieren. Dekoratoren werden häufig für Logging, Zugriffskontrolle oder zur Verifikation von Eingabedaten verwendet.

**Beispiel:**

```python
def log_decorator(funktion):
    def wrapper(*args, **kwargs):
        print(f"Ausführen von: {funktion.__name__}")
        ergebnis = funktion(*args, **kwargs)
        print(f"Beendet: {funktion.__name__}")
        return ergebnis
    return wrapper

@log_decorator
def berechne_rabatt(preis, rabatt):
    return preis * (1 - rabatt)

print(berechne_rabatt(100, 0.1))
```

In diesem Beispiel verwenden wir den `log_decorator`, um die Ausführung der Funktion `berechne_rabatt` zu protokollieren.

#### Praktische Anwendungen

Dekoratoren können wir verwenden, um beispielsweise Berechnungen zu überwachen, indem wir Protokollierungs- oder Sicherheitsmechanismen einführen.

**Beispiel:**

```python
def zugriffs_kontrolle(funktion):
    def wrapper(*args, **kwargs):
        benutzer = kwargs.get('benutzer', None)
        if benutzer == 'admin':
            return funktion(*args, **kwargs)
        else:
            print("Zugriff verweigert.")
    return wrapper

@zugriffs_kontrolle
def aktualisiere_preise(produkt_id, neuer_preis, benutzer=None):
    # Logik zur Preisaktualisierung
    print(f"Preis für Produkt {produkt_id} aktualisiert auf {neuer_preis}")

# Beispielaufrufe
aktualisiere_preise(101, 2.99, benutzer='admin')
aktualisiere_preise(101, 2.99, benutzer='kunde')
```

Hier sorgt der Dekorator `zugriffs_kontrolle` dafür, dass nur bestimmte Nutzergruppen Preise aktualisieren können.

#### Aufgaben zum Verständnis

1. **Dekorator für Zeitmessung:**
   Entwickeln wir einen Dekorator, der die Ausführungszeit einer Funktion misst und die Ergebnisse protokolliert.

2. **Validierungs-Dekorator:**
   Erstellen wir einen Dekorator, der sicherstellt, dass alle Eingabewerte der Funktion `berechne_rabatt` gültig sind (z.B. positive Zahlen).

3. **Benachrichtigungs-Dekorator:**
   Implementieren wir einen Dekorator, der nach der Aktualisierung von Lagerbeständen automatisch eine Benachrichtigung sendet.