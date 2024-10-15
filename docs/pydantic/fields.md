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
