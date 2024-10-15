# Pytest: Einführung und Aufbau von Tests

Tests sind ein integraler Bestandteil der Softwareentwicklung, da sie sicherstellen, dass unser Code wie erwartet funktioniert und korrektes Verhalten in verschiedenen Szenarien zeigt. In PyTest, einem der beliebtesten Test-Frameworks für Python, haben wir ein mächtiges Werkzeug, um einfache Unit-Tests sowie komplexere Testszenarien effizient umzusetzen.

Ein guter Test stellt sicher, dass das Verhalten eines Systems oder einer Funktion, auf die wir uns verlassen, stabil und vorhersehbar bleibt. Dies ist besonders wichtig in großen Projekten, in denen kleine Änderungen an einem Teil des Codes unvorhergesehene Auswirkungen auf andere Bereiche haben könnten.

## Aufbau von Tests

Ein Test soll das Ergebnis eines bestimmten Verhaltens überprüfen und sicherstellen, dass dieses Ergebnis den Erwartungen entspricht. „Verhalten“ beschreibt, wie ein System auf eine bestimmte Situation oder Reize reagiert. Dabei ist weniger wichtig, wie oder warum etwas geschieht, sondern was genau passiert. Das Ziel eines Tests ist es, das System unter verschiedenen Bedingungen zu beobachten und zu überprüfen, ob es korrekt reagiert.

Ein Test lässt sich typischerweise in vier Schritte unterteilen:

- **Vorbereitung (Arrange)**
- **Aktion (Act)**
- **Überprüfung (Assert)**
- **Aufräumen (Cleanup)**

### 1. Vorbereitung (Arrange)

In der Vorbereitungsphase schaffen wir die Voraussetzungen, damit der eigentliche Test durchgeführt werden kann. Dies umfasst das Einrichten von Objekten, das Laden von Testdaten, das Starten von Diensten oder das Initialisieren von Variablen. In vielen Fällen kann dies auch das Einfügen von Testdatensätzen in eine Datenbank oder das Setzen eines erwarteten Zustands in einer API-Anfrage sein. Die Vorbereitung stellt sicher, dass der Kontext des Tests vollständig ist, bevor die eigentliche Aktion ausgelöst wird.

Beispiele für Vorbereitung:
- Das Erstellen eines neuen Benutzers für einen Login-Test.
- Das Einrichten einer Netzwerkverbindung für eine API-Abfrage.
- Das Initialisieren einer Klasse mit bestimmten Startwerten.

### 2. Aktion (Act)

Dies ist der zentrale Teil des Tests, in dem eine Aktion ausgeführt wird, die das zu testende Verhalten des Systems (SUT – *System under Test*) auslöst. Typischerweise handelt es sich dabei um einen Methoden- oder Funktionsaufruf. Die Aktion sollte genau eine Änderung am Zustand des Systems hervorrufen. Diese Zustandsänderung könnte z. B. eine Berechnung, eine API-Anfrage oder das Speichern eines Datensatzes sein.

Beispiele für Aktionen:
- Ein Funktionsaufruf, der den aktuellen Bestand in einem Lager zurückgibt.
- Das Absenden eines Formulars über eine API.
- Das Hinzufügen eines neuen Artikels zu einem Warenkorb.

### 3. Überprüfung (Assert)

Nach der Aktion wird das Verhalten überprüft, um festzustellen, ob das Ergebnis den Erwartungen entspricht. Hier wird geprüft, ob der resultierende Zustand korrekt ist. Dies geschieht durch **Asserts**. Ein Assert vergleicht das tatsächliche Ergebnis mit dem erwarteten Ergebnis und sorgt dafür, dass der Test nur dann erfolgreich ist, wenn beide übereinstimmen.

Beispiele für Asserts:
- Überprüfung, ob ein Artikel erfolgreich in den Warenkorb hinzugefügt wurde.
- Sicherstellen, dass die API eine korrekte Erfolgsmeldung zurückgibt.
- Überprüfen, dass ein Rabatt korrekt auf einen Produktpreis angewendet wurde.

```python
assert actual_value == expected_value
```

Wenn diese Überprüfung fehlschlägt, zeigt PyTest den Test als fehlgeschlagen an und gibt das erwartete und tatsächliche Ergebnis aus, was das Debugging erleichtert.

### 4. Aufräumen (Cleanup)

Nicht jeder Test benötigt explizite Aufräumarbeiten, aber in vielen Fällen ist es sinnvoll, Ressourcen wie Datenbanken, Dateien oder Netzwerkverbindungen nach einem Test zu schließen. PyTest bietet verschiedene Mechanismen wie Fixtures, um dies automatisch zu handhaben, insbesondere wenn Aufräumarbeiten immer nach einem Test durchgeführt werden sollen.

Beispiele für Cleanup:
- Schließen einer Datenbankverbindung nach dem Test.
- Löschen temporärer Dateien oder Verzeichnisse.
- Zurücksetzen von Testdaten oder Entfernen von Testbenutzern.

### Der ARRANGE-ACT-ASSERT-CYCLE

Im Wesentlichen besteht jeder Test aus den Schritten **Aktion** und **Überprüfung**, wobei die Vorbereitung den Kontext für die Aktion liefert. Die Aktion verändert den Zustand des Systems, und die Überprüfung stellt sicher, dass das Verhalten den Erwartungen entspricht. 

Das folgende Beispiel zeigt, wie diese Schritte in einem simplen Unit-Test umgesetzt werden:

**Beispiel:**

```python
import pytest

def my_function(x):
    return x + 1

def test_my_function():
    x = 3  # Arrange: Vorbereitung des Testfalls
    result = my_function(x)  # Act: Ausführung der zu testenden Aktion
    assert result == 4  # Assert: Überprüfung, ob das Ergebnis korrekt ist
```

In diesem einfachen Beispiel testen wir eine Funktion `my_function`, die eine Zahl um 1 erhöht. Zuerst bereiten wir den Test vor, indem wir den Wert `x` auf 3 setzen. Dann rufen wir die Funktion auf (Aktion) und überprüfen schließlich, ob das Ergebnis korrekt ist (Überprüfung).

### Strukturierter Aufbau von Testfällen

Gute Tests folgen einem konsistenten Muster, das für alle Tests gleich bleibt. Dies erleichtert das Schreiben, Warten und Lesen von Tests, insbesondere wenn diese zahlreicher und komplexer werden. In diesem Beispiel haben wir gesehen, wie die Schritte **Arrange-Act-Assert** auf einfache Weise implementiert werden können.

### Beispiel für einen vollständigen Test:

Nehmen wir ein komplexeres Szenario aus dem Einzelhandel. Wir haben eine Funktion, die basierend auf einem gegebenen Artikelpreis und einem Rabatt den endgültigen Preis berechnet. Wir möchten sicherstellen, dass unsere Rabattberechnungen korrekt funktionieren:

```python
import pytest

def calculate_discounted_price(price, discount):
    return price * (1 - discount)

def test_calculate_discounted_price():
    # Arrange
    price = 100.0
    discount = 0.2  # 20% Rabatt
    expected_price = 80.0
    
    # Act
    final_price = calculate_discounted_price(price, discount)
    
    # Assert
    assert final_price == expected_price
```

In diesem Beispiel verwenden wir den **Arrange-Act-Assert-Zyklus**, um die Preisberechnung zu testen. Wir bereiten den Artikelpreis und den Rabatt vor, führen die Preisberechnung durch und überprüfen, ob das Endergebnis korrekt ist.

### Aufgaben:

1. **Erstelle einen Test für eine Funktion, die den Lagerbestand eines Artikels in einem Discounter aktualisiert.**
   - Verwende den **Arrange-Act-Assert-Zyklus**, um sicherzustellen, dass der Lagerbestand korrekt erhöht wird, wenn eine Lieferung eintrifft.

2. **Schreibe einen Test für eine Funktion, die basierend auf dem Artikelpreis und der Menge den Gesamtpreis berechnet.**
   - Implementiere eine Aktion, die eine Menge von Artikeln an einen Warenkorb hinzufügt, und überprüfe, ob der Gesamtpreis korrekt berechnet wird.

3. **Implementiere einen Test für eine Funktion, die prüft, ob ein Benutzer erfolgreich eingeloggt werden kann.**
   - Parametrisiere den Test, um verschiedene Benutzeranmeldeinformationen zu testen.
