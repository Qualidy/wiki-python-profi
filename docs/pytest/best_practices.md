# Best Practices


## Test Organization

Für pytest gibt es 2 allgemeine Methoden, um Tests zu organisieren:

1. **Im Anwendungscode integrierte Tests**: Tests werden in den gleichen Ordner wie der Anwendungscode geschrieben. Dies kann beispielsweise in einem `tests/`-Ordner innerhalb des Projekts erfolgen.

```plaintext
[src/]my_package/
    __init__.py
    app.py
    view.py
    tests/
        __init__.py
        test_app.py
        test_view.py
        ...
```

Wollen wir die Tests ausführen, können wir folgenden Befehl verwenden:

```bash
pytest --pyargs tests/
```

2. **Separater Testordner**: Tests werden in einem separaten Ordner geschrieben, z.B. `tests/`. Dies ist nützlich, wenn die Tests unabhängig von der Anwendungsstruktur sein sollen.

```plaintext
src/
    my_package/
        __init__.py
        app.py
        view.py
tests/
    test_app.py
    test_view.py
    ...
```

Wollen wir die Tests ausführen, können wir folgenden Befehl verwenden:

```bash
python -m pytest
```

Falls wir mehrere Tests mit dem gleichen Namen haben, können wir uns über weitere Subfolder behelfen:

```plaintext
tests/
    __init__.py
    test_app/
        test_app.py
    test_view/
        test_view.py
    ...
```