# Parametrisierung von Tests

In diesem Abschnitt widmen wir uns der **Parametrisierung von Tests**. Dies ist besonders nützlich, wenn wir unsere Tests mit verschiedenen Eingabewerten wiederholt ausführen möchten, ohne dafür mehrfach den gleichen Code schreiben zu müssen. Insbesondere in Projekten, die umfangreiche Datenverarbeitung beinhalten, wie es im Einzelhandel oft der Fall ist, ermöglicht uns die Parametrisierung, effizient und flexibel zu testen.

### Was ist Parametrisierung?

Mit der Parametrisierung können wir eine Testfunktion mit verschiedenen Eingabewerten mehrfach ausführen. Stellen wir uns vor, wir entwickeln ein Kassensystem für einen Discounter und möchten die Berechnung von Rabatten für verschiedene Produkttypen testen. Anstatt für jeden Produkttyp eine eigene Testfunktion zu schreiben, können wir dieselbe Testfunktion mit verschiedenen Rabattsätzen und Preisen aufrufen.

Dies ermöglicht es uns, die Testfälle sauber und wiederverwendbar zu halten, ohne unnötigen doppelten Code.

### Parametrisierung mit `@pytest.mark.parametrize`

In PyTest verwenden wir den Dekorator `@pytest.mark.parametrize`, um eine Funktion zu parametrisieren. Nehmen wir an, wir haben eine Funktion, die für ein Kassensystem den Endpreis eines Produkts berechnet, nachdem ein Rabatt abgezogen wurde. Wir möchten diese Funktion mit verschiedenen Rabatten testen.

Zunächst ein einfaches Beispiel:

```python
import pytest

@pytest.mark.parametrize("price, discount, expected", [
    (100, 0.10, 90),
    (200, 0.15, 170),
    (50, 0.20, 40)
])
def test_discount(price, discount, expected):
    assert price * (1 - discount) == expected
```

Hier haben wir die Funktion `test_discount` mit drei verschiedenen Satzpaaren von Preis und Rabattwerten parametrisiert. PyTest wird diesen Test dreimal ausführen – einmal für jedes Tupel von Werten (Preis, Rabatt, erwarteter Endpreis).

### Mehrere Parameter

Manchmal müssen wir mehr als nur einen Parameter kombinieren. Nehmen wir an, wir testen in einem Discounter-Szenario nicht nur den Rabatt, sondern auch, ob der Preis brutto oder netto vorliegt. Dazu können wir mehrere Parameter in einer Parametrisierung kombinieren:

```python
@pytest.mark.parametrize("price, discount, is_gross, expected", [
    (100, 0.10, True, 90), 
    (200, 0.15, False, 170),
    (50, 0.20, True, 40)
])
def test_discount(price, discount, is_gross, expected):
    if is_gross:
        net_price = price * 0.9  # Vereinfachte Beispielsteuer
    else:
        net_price = price
    assert net_price * (1 - discount) == expected
```

In diesem Beispiel haben wir den zusätzlichen Parameter `is_gross` eingeführt, der anzeigt, ob der angegebene Preis bereits die Mehrwertsteuer enthält oder nicht. Je nach Eingabeparameter wird der Preis unterschiedlich berechnet.

### Aufgaben

**Aufgabe 1:** Parametrisiere einen Test, der verschiedene Rabatte und Preise für Lebensmittelprodukte testet. Denke dabei daran, dass Lebensmittel in Deutschland eine andere Mehrwertsteuer (7 %) haben als andere Produkte (19 %).

**Aufgabe 2:** Schreibe eine Testfunktion, die die korrekte Berechnung von Mengenrabatten für verschiedene Produktmengen und Rabattstaffeln testet. Verwende die Parametrisierung, um unterschiedliche Rabattstufen für unterschiedliche Mengen zu testen.

### Verwendung von Fixtures mit Parametrisierung

Wie bereits im vorherigen Abschnitt erläutert, sind Fixtures in PyTest extrem nützlich. Wir können sie auch zusammen mit der Parametrisierung verwenden, um komplexere Szenarien abzubilden. Nehmen wir an, wir haben eine Fixture, die eine Liste von Artikeln in einem Warenkorb zurückgibt. Diese Liste könnte für verschiedene Kundengruppen parametrisiert werden, z.B. für Privatkunden und Großkunden.

```python
@pytest.fixture
def customer_type():
    return {"type": "retail", "discount": 0.10}

@pytest.mark.parametrize("price, expected", [
    (100, 90),
    (200, 180),
])
def test_customer_discount(price, expected, customer_type):
    discount = customer_type['discount']
    assert price * (1 - discount) == expected
```

Hier verwenden wir eine Fixture, um den Kundentyp zu simulieren. In diesem Fall gibt die Fixture an, dass es sich um einen Einzelkunden handelt, der einen festen Rabatt erhält. Die Parametrisierung sorgt dafür, dass wir die Testlogik mit verschiedenen Preisen durchlaufen können.

### Parametrisierung komplexer Objekte

In manchen Fällen möchten wir komplexe Datenstrukturen an unsere Tests übergeben, wie zum Beispiel Objekte oder Wörterbücher. Dies ist besonders im Einzelhandel relevant, wenn wir z.B. mit Produktinformationen arbeiten.

Stellen wir uns vor, wir haben ein Wörterbuch, das verschiedene Eigenschaften eines Produkts speichert, und wir möchten die Preiskalkulation auf Basis dieser Daten testen:

```python
@pytest.mark.parametrize("product, expected_price", [
    ({"name": "Apple", "price": 1.00, "discount": 0.05}, 0.95),
    ({"name": "Banana", "price": 0.50, "discount": 0.10}, 0.45),
    ({"name": "Laptop", "price": 1000, "discount": 0.20}, 800)
])
def test_product_discount(product, expected_price):
    final_price = product["price"] * (1 - product["discount"])
    assert final_price == expected_price
```

In diesem Beispiel verwenden wir Wörterbücher, die die Eigenschaften der Produkte enthalten, und parametrisieren den Test, um verschiedene Produkte und ihre Rabatte zu überprüfen. Dies ist besonders nützlich, wenn wir Tests schreiben, die mit realistischen Daten arbeiten sollen.

### Aufgaben

**Aufgabe 3:** Erstelle eine Parametrisierung, bei der du verschiedene Kundentypen (z.B. Privatkunde, Großkunde, Mitarbeiter) testest und sicherstellst, dass jeweils der richtige Rabatt angewendet wird.

**Aufgabe 4:** Schreibe einen Test, der unterschiedliche Produkte testet, bei denen neben dem Preis auch noch andere Eigenschaften wie Mindesthaltbarkeitsdatum oder Stückzahl berücksichtigt werden. Parametrisiere die Tests, um sicherzustellen, dass für verderbliche Waren spezielle Regeln gelten (z.B. zusätzliche Rabatte kurz vor Ablaufdatum).

### Parametrisierung und Fehlererwartungen

In manchen Fällen möchten wir nicht nur testen, ob eine Funktion korrekt arbeitet, sondern auch, ob sie bei falschen Eingabewerten erwartungsgemäß Fehler auslöst. Dies lässt sich ebenfalls mit der Parametrisierung kombinieren. Nehmen wir an, wir möchten sicherstellen, dass unser Kassensystem bei einem negativen Preis eine Ausnahme wirft:

```python
@pytest.mark.parametrize("price, discount", [
    (-10, 0.10),
    (100, -0.15),
    (-50, -0.20)
])
def test_invalid_discount(price, discount):
    with pytest.raises(ValueError):
        if price < 0 or discount < 0:
            raise ValueError("Preis oder Rabatt dürfen nicht negativ sein")
```

In diesem Fall parametrisieren wir den Test mit fehlerhaften Eingabewerten und erwarten, dass eine `ValueError`-Exception geworfen wird, wenn der Preis oder der Rabatt negativ ist. Dies ist nützlich, um sicherzustellen, dass unser System robust gegenüber falschen Eingaben ist.

### Aufgaben

**Aufgabe 5:** Parametrisiere einen Test, der sicherstellt, dass das Kassensystem bei ungültigen Eingaben (z.B. negativen Preisen oder ungültigen Rabattwerten) korrekt Fehler auslöst.

