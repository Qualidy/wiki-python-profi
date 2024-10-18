### Dataclasses in Pydantic

Pydantic bietet die Möglichkeit, Python-Dataclasses um Validierungslogik und zusätzliche Features zu erweitern. Normalerweise sind **Dataclasses** einfache Container für Daten, die keine eingebaute Validierung oder Konvertierung bieten. Pydantic-Dataclasses hingegen fügen diesen Funktionen eine starke Datenvalidierung hinzu, ähnlich wie bei einem `BaseModel`.

Wir können die Dataclass von Pydantic als wie eine Erweiterung der built-in Dataclass in Python sehen.

#### Beispiel: Pydantic-Dataclass

```python
from pydantic import dataclasses, ValidationError

@dataclasses.dataclass
class Produkt:
    id: int
    name: str
    preis: float

# Instanziierung eines Produkts
try:
    produkt = Produkt(id="123", name="Laptop", preis="999.99")  # Automatische Konvertierung
    print(produkt)
except ValidationError as e:
    print(e)
```

In diesem Beispiel wird eine Pydantic-Dataclass verwendet, die eine automatische Typkonvertierung und Validierung durchführt. Hier wird z.B. die `id` und `preis` von einem `str` in den korrekten Typ umgewandelt (`int` und `float`).

### Unterschiede zwischen einer normalen Dataclass und einer Pydantic-Dataclass

Eine normale Python-Dataclass bietet keine Datenvalidierung oder Typkonvertierung. Alle Felder müssen beim Instanziieren der Klasse bereits den richtigen Typ haben, da Python-Dataclasses keine eingebaute Prüfung durchführen.

#### Normale Dataclass

```python
from dataclasses import dataclass

@dataclass
class Produkt:
    id: int
    name: str
    preis: float

# Instanziierung mit falschen Typen führt zu keinem Fehler, sondern falschem Verhalten
produkt = Produkt(id="123", name="Laptop", preis="999.99")
print(produkt)  # Dies wird fehlerhaft ausgeführt, weil die Typen nicht konvertiert werden
```

Hier wird **keine** Typkonvertierung durchgeführt. Wenn die Felder falsche Typen haben, wie `id` als `str` anstatt `int`, führt dies zu Problemen bei der späteren Verwendung, ohne dass ein Fehler gemeldet wird.

#### Vorteile der Pydantic-Dataclass gegenüber der normalen Dataclass:
- **Automatische Typkonvertierung**: Pydantic-Dataclasses konvertieren Eingabewerte automatisch in die erwarteten Typen.
- **Eingebaute Validierung**: Jede Zuweisung wird validiert. Falsche Typen oder ungültige Werte führen zu einem `ValidationError`.
- **Leichte Integration in Pydantic-Ökosystem**: Pydantic-Dataclasses unterstützen JSON-Schema-Generierung und lassen sich leicht mit anderen Pydantic-Features kombinieren.

### Nachteile der Pydantic-Dataclass gegenüber einem `BaseModel`

Während Pydantic-Dataclasses viele Vorteile gegenüber normalen Dataclasses bieten, gibt es einige Einschränkungen im Vergleich zu einem Pydantic `BaseModel`:

1. **Leistung**: Pydantic-Dataclasses sind im Vergleich zu `BaseModel`-Objekten etwas langsamer, da sie durch Python-Dataclasses eingeschränkt sind und nicht alle Optimierungen von Pydantic übernehmen können.
   
2. **Fehlende Methoden**: Ein `BaseModel` bietet viele nützliche Methoden, wie z.B. `.json()`, `.dict()` und `.copy()`, die für die Serialisierung und Manipulation von Daten sehr praktisch sind. Diese fehlen bei Pydantic-Dataclasses.

3. **Mehr Flexibilität in `BaseModel`**: `BaseModel`-Objekte bieten umfassendere Konfigurationsmöglichkeiten. Einige Fehldtypen von `BaseModel` sind in Pydantic `dataclasses` nicht abbildbar. Die Dokumentation ist an dieser Stelle auch noch nicht vollständig. Mehr dazu [hier](https://github.com/pydantic/pydantic/issues/710)
