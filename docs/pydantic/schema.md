# Schema

Ähnlich wie auch bei `@dataclass` gibt es in Pydantic die Option, JSON-Schemas aus Objekten zu erstellen. Das Schema-Handling für Modelle und Felder wird automatisch generiert, um JSON-Schemas für die Validierung und Dokumentation bereitzustellen. Dabei können zusätzliche Metadaten für jedes Feld angegeben werden, wie z.B. Beschreibungen, Titel oder Beispiele, die im generierten Schema verwendet werden.

### Schema für Modelle und Felder

Mit der Funktion `Field` können wir zusätzliche Informationen wie `title`, `description` und `examples` festlegen, die im generierten JSON-Schema verwendet werden. Dies ist besonders nützlich für die API-Dokumentation.

Beispiel:
```python
from pydantic import BaseModel, Field

class Produkt(BaseModel):
    id: int = Field(..., title="Produkt-ID", description="Die eindeutige Kennung des Produkts", example=123)
    name: str = Field(..., title="Produktname", description="Der Name des Produkts", example="Laptop")
    preis: float = Field(..., title="Preis", description="Der Preis des Produkts in EUR", example=999.99)
```

### JSON-Schema-Generierung

Pydantic bietet die Möglichkeit, ein Modell als JSON-Schema zu exportieren. Das ist hilfreich für die Integration in API-Dokumentationen wie OpenAPI.

```python
produkt_schema = Produkt.model_json_schema()
print(produkt_schema)
```

Das resultierende Schema sieht dann in etwa so aus:
```json
{
  "title": "Produkt",
  "type": "object",
  "properties": {
    "id": {
      "title": "Produkt-ID",
      "type": "integer",
      "description": "Die eindeutige Kennung des Produkts",
      "example": 123
    },
    "name": {
      "title": "Produktname",
      "type": "string",
      "description": "Der Name des Produkts",
      "example": "Laptop"
    },
    "preis": {
      "title": "Preis",
      "type": "number",
      "description": "Der Preis des Produkts in EUR",
      "example": 999.99
    }
  },
  "required": ["id", "name", "preis"]
}
```

### Anpassung des Schemas

Durch die Verwendung von `Field`-Parametern können wir detaillierte Metadaten für jedes Feld hinzufügen:
- **`title`**: Gibt dem Feld einen Titel im Schema.
- **`description`**: Beschreibt das Feld detailliert.
- **`example`**: Definiert ein Beispiel, das im Schema angezeigt wird.

Mit diesen Informationen können wir sicherstellen, dass das Schema sowohl für die Validierung als auch für die API-Dokumentation aussagekräftig ist.