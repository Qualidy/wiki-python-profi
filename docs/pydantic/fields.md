# Fields

Die Types in Pydantic sind in der Regel die Python-Standardtypen, aber Pydantic bietet auch spezielle Felder, die zusätzliche Validierungen und Konvertierungen ermöglichen. Einige der verfügbaren Felder sind:

- `Field`: Ein generisches Feld, das zusätzliche Validierungen und Konvertierungen ermöglicht.
- `ConstrainedStr`: Ein Feld, das eine Zeichenkette mit zusätzlichen Einschränkungen validiert.
- `EmailStr`: Ein Feld, das eine E-Mail-Adresse validiert.
- `SecretStr`: Ein Feld, das sensible Daten wie Passwörter maskiert.

Mit diesen speziellen Feldern können wir die Validierung und Konvertierung von Daten weiter anpassen.

```python
from pydantic import EmailStr, Field

class User(BaseModel):
    id: int
    name: str
    email: EmailStr = Field(..., description='E-Mail-Adresse des Benutzers')
```

Wir schauen nachfolgend auf einige der Felder, die Pydantic anbietet und wie sie verwendet werden können.

## Erweiterte Anpassungen mit `Field`
`Field` erlaubt es uns, zusätzliche Metadaten wie `title`, `description`, `default_factory` und `alias` anzugeben, um sowohl die Validierung als auch die Serialisierung (z. B. bei der JSON-Schema-Generierung) zu beeinflussen.

```python
from pydantic import Field, BaseModel

class Produkt(BaseModel):
    name: str = Field(..., title="Produktname", description="Der Name des Produkts", min_length=3)
```

Hier wird der Name des Produkts mit einer Mindestlänge von 3 Zeichen validiert und zusätzlich in der JSON-Schema-Darstellung mit einem Titel und einer Beschreibung versehen.

## Optionale Felder
Mit der Verwendung von `Optional` wird explizit erlaubt, dass ein Feld den Wert `None` annehmen kann. Außerdem kannst du festlegen, ob ein Feld weggelassen oder standardmäßig mit einem Wert versehen werden soll.

```python
from typing import Optional
from pydantic import BaseModel

class Bestellung(BaseModel):
    artikel_id: int
    rabatt_code: Optional[str] = None  # Optionales Feld mit Standardwert
```

In diesem Beispiel ist der `rabatt_code` optional und kann weggelassen oder explizit auf `None` gesetzt werden.

## Einschränkende Feldtypen (`Constrained Types`)
Pydantic bietet auch spezielle Feldtypen wie `ConstrainedInt`, `ConstrainedStr`, `PositiveInt` und `StrictStr`, die es ermöglichen, zusätzliche Einschränkungen wie minimale/maximale Werte oder Zeichenlängen zu setzen.

```python
from pydantic import conint, constr

class Kunde(BaseModel):
    alter: conint(gt=18, lt=65)  # Das Alter muss zwischen 18 und 65 Jahren liegen
    benutzername: constr(min_length=3, regex=r'^[a-zA-Z0-9_]+$')  # Benutzername mit minimaler Länge und Regex-Überprüfung
```

## Mehrere Typen für ein Feld mit `Union`
Mit `Union` kannst du festlegen, dass ein Feld mehrere Typen akzeptiert. Pydantic versucht dabei automatisch, den ersten passenden Typ zuzuweisen.

```python
from typing import Union
from pydantic import BaseModel, EmailStr

class Kontakt(BaseModel):
    kontakt_info: Union[EmailStr, str]  # Akzeptiert entweder eine E-Mail-Adresse oder eine Zeichenkette
```

In diesem Fall wird `kontakt_info` entweder als E-Mail-Adresse oder als einfache Zeichenkette akzeptiert.

### Aufgaben

1. **Produktmodell erstellen:**
   Erstelle ein Pydantic-Modell `Produkt` mit folgenden Feldern:
    - `name`: Ein String-Feld mit einer Mindestlänge von 3 Zeichen
    - `preis`: Ein Float-Feld mit einem Mindestwert von 0
    - `kategorie`: Ein String-Feld, das nur bestimmte Werte akzeptiert (z.B. "Lebensmittel", "Elektronik", "Kleidung")
    - `lagerbestand`: Ein optionales Integer-Feld mit einem Standardwert von 0

2. **Benutzermodell mit E-Mail-Validierung:**
   Erstelle ein Pydantic-Modell `Benutzer` mit folgenden Feldern:
    - `benutzername`: Ein String-Feld mit einer Mindestlänge von 5 Zeichen
    - `email`: Ein E-Mail-Feld mit Validierung
    - `alter`: Ein Integer-Feld mit einem Mindestwert von 18
    - `passwort`: Ein Feld vom Typ `SecretStr`

3. **Bestellungsmodell mit Validierung:**
   Erstelle ein Pydantic-Modell `Bestellung` mit folgenden Feldern:
    - `bestellnummer`: Ein String-Feld mit einem bestimmten Muster (z.B. "ORD-" gefolgt von 6 Ziffern)
    - `produkte`: Eine Liste von `Produkt`-Objekten (verwende das Modell aus Aufgabe 1)
    - `gesamtpreis`: Ein berechnetes Feld, das die Summe der Produktpreise darstellt
    - `bestelldatum`: Ein Datum-Feld mit dem aktuellen Datum als Standardwert

Versuche, diese Modelle zu implementieren und teste sie mit verschiedenen Eingaben. Achte besonders darauf, wie Pydantic die Daten validiert und konvertiert.