# Custom Fields & Validators

In pydantic haben wir 2 Möglichkeiten, um eine eigene Validierung eines Feldes vorzunehmen. Entweder definieren wir ein ganz eigenes Feld oder wir definieren für ein bestehendes Feld einen eigenen Validator.


## Eigene Felder

Wir können in pydantic auch eigene Felder definieren, die spezielle Validierungen oder Konvertierungen durchführen. Dies kann beispielsweise sinnvoll sein, wenn wir eine eigene Logik für die Validierung von Daten benötigen, die über die Standardfelder von pydantic hinausgeht. 

Stellen wir uns vor, wir möchten eine Klasse Produkt erstellen und haben ein spezielles Feld `Price`, das den Preis eines Produkts repräsentiert. Der Preis soll als Dezimalzahl mit zwei Nachkommastellen gespeichert werden und muss größer oder gleich Null sein. Wir können ein benutzerdefiniertes Feld `PriceField` erstellen, das diese Validierung durchführt.

```python
from decimal import Decimal
from pydantic import BaseModel, ValidationError, validator

class PriceField(Decimal):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value, field, **kwargs):
        if not isinstance(value, Decimal):
            try:
                value = Decimal(value)
            except (ValueError, TypeError):
                raise ValueError('value is not a valid decimal number')
        if value < 0:
            raise ValueError('value must be greater than or equal to 0')
        if value.as_tuple().exponent != -2:
            raise ValueError('value must have exactly 2 decimal places')
        return value

class Produkt(BaseModel):
    name: str
    price: PriceField

try:
    produkt = Produkt(name='Laptop', price='999.99')
    print(produkt)
except ValidationError as e:
    print(e)
```

In diesem Beispiel definieren wir das benutzerdefinierte Feld `PriceField`, das von der Klasse `Decimal` erbt und spezielle Validierungen für den Preis eines Produkts durchführt. Die Validierung überprüft, ob der Preis eine Dezimalzahl ist, größer oder gleich Null ist und genau zwei Nachkommastellen hat.

Wir verwenden das benutzerdefinierte Feld `PriceField` in der Klasse `Produkt`, um den Preis eines Produkts zu validieren. Wenn wir versuchen, ein `Produkt`-Objekt mit einem ungültigen Preis zu erstellen, wird eine `ValidationError` ausgelöst.

Durch die Definition benutzerdefinierter Felder können wir die Validierung und Konvertierung von Daten in pydantic an unsere spezifischen Anforderungen anpassen. Dies ermöglicht es uns, flexiblere und genauere Datenmodelle zu erstellen, die unseren Anwendungsfällen entsprechen.
In der Praxis können benutzerdefinierte Felder in pydantic verwendet werden, um spezielle Validierungen oder Konvertierungen vorzunehmen, die über die Standardfunktionen hinausgehen.

## Eigene Validatoren

Manchmal benötigen wir gar keinen eigenen Datentyp, sondern möchten nur eine spezielle Validierung für ein Feld durchführen. In solchen Fällen können wir benutzerdefinierte Validatoren verwenden, um die Daten zu überprüfen und gegebenenfalls Fehler zu melden.

Stellen wir uns vor, wir möchten ein Feld `username` erstellen, das nur aus Buchstaben, Zahlen und Unterstrichen bestehen darf. Wir können ein benutzerdefiniertes Validierungsmethode `validate_username` erstellen, das diese Überprüfung durchführt.

```python
from pydantic import BaseModel, ValidationError, validator

class User(BaseModel):
    username: str

    @validator('username')
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError('username must only contain letters and numbers')
        return value

try:
    user = User(username='alice123')
    print(user)
except ValidationError as e:
    print(e)
```

In diesem Beispiel definieren wir die Klasse `User` mit einem Feld `username`, das nur Buchstaben und Zahlen enthalten darf. Wir erstellen ein benutzerdefiniertes Validierungsmethode `validate_username`, das die Überprüfung durchführt und eine `ValueError` auslöst, wenn das Feld nicht den Anforderungen entspricht.

Wir verwenden das benutzerdefinierte Validierungsmethode `validate_username` mit dem Dekorator `@validator`, um das Feld `username` zu validieren. Wenn wir versuchen, ein `User`-Objekt mit einem ungültigen Benutzernamen zu erstellen, wird eine `ValidationError` ausgelöst.

### Aufgabe: Implementierung eines eigenen Validators

Erstelle ein Pydantic-Modell `Artikel` mit folgenden Anforderungen:

1. Das Modell soll folgende Felder haben:
    - `name`: Ein String-Feld für den Namen des Artikels
    - `artikelnummer`: Ein String-Feld für die Artikelnummer
    - `preis`: Ein Float-Feld für den Preis des Artikels
    - `kategorie`: Ein String-Feld für die Kategorie des Artikels

2. Implementiere einen eigenen Validator für das Feld `artikelnummer` mit folgenden Regeln:
    - Die Artikelnummer muss genau 8 Zeichen lang sein
    - Die ersten zwei Zeichen müssen Buchstaben sein (Großbuchstaben)
    - Die letzten 6 Zeichen müssen Zahlen sein
    - Beispiel für eine gültige Artikelnummer: "AB123456"

3. Implementiere einen weiteren Validator für das Feld `kategorie`, der sicherstellt, dass nur bestimmte Kategorien erlaubt sind. Die erlaubten Kategorien sind:
    - "Elektronik"
    - "Kleidung"
    - "Lebensmittel"
    - "Haushalt"

4. Teste dein Modell mit verschiedenen Eingaben, sowohl mit gültigen als auch mit ungültigen Daten.

Hier ist ein Grundgerüst für dein Modell:

```python
from pydantic import BaseModel, validator

class Artikel(BaseModel):
    name: str
    artikelnummer: str
    preis: float
    kategorie: str

    @validator('artikelnummer')
    def validate_artikelnummer(cls, v):
        # Implementiere hier die Validierung für die Artikelnummer
        pass

    @validator('kategorie')
    def validate_kategorie(cls, v):
        # Implementiere hier die Validierung für die Kategorie
        pass

# Teste dein Modell hier
```