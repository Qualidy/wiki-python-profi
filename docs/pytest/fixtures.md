In diesem Abschnitt beschäftigen wir uns mit einem der wichtigsten Konzepte in PyTest: den **Fixtures**. Fixtures sind eine Möglichkeit, Testdaten oder Testumgebungen bereitzustellen, die wir in unseren Tests wiederverwenden können. Dadurch wird nicht nur der Code aufgeräumter, sondern wir vermeiden auch unnötige Wiederholungen. 

### Was sind Fixtures?

Fixtures sind Funktionen, die vor unseren Tests aufgerufen werden, um bestimmte Vorbedingungen oder Ressourcen bereitzustellen. Das können Datenbankverbindungen, Dateien, Netzwerkressourcen oder einfach nur Daten sein, die in mehreren Tests benötigt werden. Eine der größten Stärken von Fixtures liegt darin, dass sie sich nicht nur um die Vorbereitung, sondern auch um die Aufräumarbeiten kümmern können, falls nötig.

Stellen wir uns vor, wir testen eine Anwendung, die auf eine Datenbank zugreift. In jedem Test benötigen wir eine frische, vorbereitete Datenbank. Mit Fixtures können wir das Setup und das Teardown dieser Datenbank in einer zentralen Funktion unterbringen und diese dann in unseren Tests nutzen. Das bedeutet: Wir müssen die Initialisierung nicht in jedem Test wiederholen.

### Wie definieren wir eine Fixture?

Fixtures werden in PyTest mithilfe des `@pytest.fixture`-Dekorators definiert. Lassen Sie uns gemeinsam ein einfaches Beispiel durchgehen. Angenommen, wir haben eine Funktion, die eine Berechnung auf einer Liste von Zahlen durchführt. Wir möchten sicherstellen, dass in unseren Tests immer eine bestimmte Liste von Zahlen verwendet wird.

```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]
```

In diesem Fall ist `sample_list` unsere Fixture. Sie liefert eine Liste von Zahlen, die wir in mehreren Tests wiederverwenden können.

### Verwendung einer Fixture in Tests

Um diese Fixture in einem Test zu verwenden, übergeben wir einfach den Namen der Fixture als Parameter an die Testfunktion:

```python
def test_sum(sample_list):
    assert sum(sample_list) == 15
```

Hier ruft PyTest die Fixture `sample_list` auf und injiziert deren Rückgabewert in den Test. Der Test selbst bleibt übersichtlich und fokussiert, da wir uns nicht um die Erstellung der Liste kümmern müssen.

### Fixture-Scopes

Oft benötigen wir mehr Kontrolle darüber, wie oft eine Fixture erstellt wird. Standardmäßig wird eine Fixture für jeden Test neu ausgeführt, aber manchmal möchten wir, dass eine Fixture über mehrere Tests hinweg besteht. PyTest bietet dafür verschiedene **Scopes**, wie:

- `function`: Die Fixture wird vor jedem Test aufgerufen (Standard).
- `module`: Die Fixture wird einmal pro Modul aufgerufen.
- `class`: Die Fixture wird einmal pro Klasse aufgerufen.
- `session`: Die Fixture wird einmal pro Test-Session aufgerufen.

Schauen wir uns ein Beispiel an, in dem wir eine Datenbankverbindung nur einmal pro Modul erstellen wollen:

```python
@pytest.fixture(scope="module")
def db_connection():
    conn = setup_database()
    yield conn
    conn.close()
```

Hier verwenden wir den `yield`-Befehl, um die Verbindung nach dem Testen zu schließen. Mit `yield` geben wir die Ressource zurück, aber die Funktion kann auch nach dem Test weiterlaufen, um Aufräumarbeiten durchzuführen.

### Aufgaben

**Aufgabe 1:** Definiere eine Fixture, die eine Datei öffnet, diese nach dem Testen aber automatisch schließt. Nutze dafür `yield` und überlege, welche Aufräumarbeiten notwendig sind.

**Aufgabe 2:** Erstelle eine Fixture mit einem `class`-Scope, die eine komplexe Datenstruktur (z.B. einen großen JSON-Datensatz) erstellt und in mehreren Tests einer Klasse verwendet wird.

### Parametrisierte Fixtures

Manchmal wollen wir unsere Tests mit unterschiedlichen Daten ausführen. Hier kommen **parametrisierte Fixtures** ins Spiel. Damit können wir eine Fixture mit verschiedenen Werten bereitstellen, ohne den Code zu duplizieren.

Ein Beispiel:

```python
@pytest.fixture(params=[(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def numbers(request):
    return request.param
```

Die Fixture `numbers` liefert in jedem Testlauf ein anderes Zahlenpaar. In unseren Tests sieht das so aus:

```python
def test_addition(numbers):
    a, b, result = numbers
    assert a + b == result
```

PyTest führt diesen Test dreimal aus, jedes Mal mit einem anderen Tupel von Werten. Parametrisierte Fixtures helfen uns dabei, umfangreiche Tests mit unterschiedlichen Eingabedaten zu schreiben, ohne den Code zu vervielfachen.

### Fixture-Komposition

In realen Projekten kommt es häufig vor, dass wir mehrere Fixtures kombinieren müssen. Glücklicherweise unterstützt PyTest die Abhängigkeit von Fixtures, das heißt, eine Fixture kann eine andere Fixture verwenden. Dies ermöglicht uns eine elegante Komposition von Funktionen.

Schauen wir uns folgendes Beispiel an:

```python
@pytest.fixture
def user_data():
    return {"name": "Max", "age": 28}

@pytest.fixture
def user_profile(user_data):
    return {"profile": f"{user_data['name']} is {user_data['age']} years old."}

def test_profile(user_profile):
    assert user_profile == "Max is 28 years old."
```

Hier verwendet die `user_profile`-Fixture die `user_data`-Fixture, um ein zusammengesetztes Ergebnis zu erzeugen. Dies ist eine sehr nützliche Technik, wenn unsere Testkonfigurationen komplexer werden und wir bestimmte Teile in separaten Fixtures kapseln wollen.

### Aufgaben

**Aufgabe 3:** Erstelle zwei Fixtures, bei denen die eine auf der anderen basiert. Die erste Fixture sollte eine Liste mit Zahlen liefern, die zweite Fixture soll den Durchschnitt dieser Liste berechnen.

**Aufgabe 4:** Verwende parametrisierte Fixtures, um einen Test zu erstellen, der verschiedene Benutzereingaben testet (z.B. eine Liste von Benutzernamen und Passwörtern) und prüft, ob die Anmeldung erfolgreich ist.
