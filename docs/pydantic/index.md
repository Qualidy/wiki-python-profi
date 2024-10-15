# Pydantic

Python ist standardmäßig eine dynamisch typisierte Sprache, was bedeutet, dass Variablen nicht explizit mit einem Datentyp deklariert werden müssen. Dies kann jedoch zu unerwarteten Fehlern führen, wenn die Daten nicht den erwarteten Typen entsprechen. Pydantic ist eine Bibliothek, die es ermöglicht, Datenmodelle zu definieren und zu validieren, um sicherzustellen, dass die Daten den erwarteten Typen entsprechen.

In diesem Abschnitt werden wir uns ein Paar grundlegegende Konzepte von Pydantic ansehen und wie wir sie in unseren Projekten verwenden können.

## Models

Ein Modell in Pydantic ist eine Klasse, die Datenattribute definiert und validiert. Ein Modell wird durch eine Klasse definiert, die von der Klasse `pydantic.BaseModel` erbt. Die Datenattribute werden als Klassenvariablen definiert, die durch Typenannotationen gekennzeichnet sind.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

In diesem Beispiel definiert das Modell `User` drei Datenattribute: `id`, `name` und `email`, die die Typen `int`, `str` und `str` haben. Durch die Verwendung von Pydantic können wir sicherstellen, dass die Daten, die wir in ein `User`-Objekt einfügen, den erwarteten Typen entsprechen.

```python
user = User(id=1, name='Alice', email='alice@im-wunderland.de')
print(user)
# User id=1 name='Alice'
```

## Validierung

Pydantic validiert die Daten automatisch, wenn wir ein Modell instanziieren. Wenn die Daten nicht den erwarteten Typen entsprechen, wird eine `ValidationError` ausgelöst.


Wie können die Validierung theorethisch auch manuell auslösen:
1. **`model_validate()`**:
   - Validiert Daten in Form eines Wörterbuchs oder eines Objekts.
   - Wirft einen `ValidationError`, wenn die Eingabe ungültig ist oder kein Wörterbuch/Objekt vom Modelltyp ist.

2. **`model_validate_json()`**:
   - Validiert Daten, die als JSON-String oder -Bytes vorliegen.
   - Ist schneller als manuelles Parsen, wenn die Eingabedaten im JSON-Format sind.

3. **`model_validate_strings()`**:
   - Nimmt ein Wörterbuch mit Zeichenketten als Schlüssel und Werte (auch verschachtelt).
   - Zwingt diese Zeichenketten, in die richtigen Datentypen konvertiert zu werden.

**Beispiele:**

- `model_validate()`: Validierung eines Wörterbuchs.
   ```python
   m = User.model_validate({'id': 123, 'name': 'James'})
   print(m)  # id=123 name='James' signup_ts=None
   ```
   Bei ungültigen Eingabedaten wird ein `ValidationError` ausgelöst.

- `model_validate_json()`: Validierung von JSON-Daten.
   ```python
   m = User.model_validate_json('{"id": 123, "name": "James"}')
   print(m)  # id=123 name='James' signup_ts=None
   ```

- `model_validate_strings()`: Konvertiert Zeichenketten in entsprechende Datentypen.
   ```python
   m = User.model_validate_strings({'id': '123', 'name': 'James'})
   print(m)  # id=123 name='James' signup_ts=None
   ```

   Bei fehlerhaften Zeichenketten-Daten wird ein `ValidationError` ausgelöst.


