# Erste Schritte mit Dash


Um eine einfache Dash-Anwendung zu starten, muss eine Instanz der `dash.Dash`-Klasse erstellt werden. Diese Instanz dient als Container für die Anwendung. Anschließend können Layout und Callbacks definiert werden.

Über das Layout wird festgelegt, wie die Anwendung aussieht. Das Layout wird beispielsweise durch HTML-Elemente wie Überschriften, Textfelder oder Schaltflächen definiert. Diese Komponenten sind großteils in den Modulen `dash.html` und `dash.core_components` enthalten.

Callbacks sind Funktionen, die aufgerufen werden, wenn ein bestimmtes Ereignis eintritt. Beispielsweise kann eine Callback-Funktion aufgerufen werden, wenn ein Button gedrückt wird. Callbacks werden in Dash verwendet, um die Interaktivität der Anwendung zu steuern.

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.H1('Hello World')

if __name__ == '__main__':
    app.run_server(debug=True)
```

Um die Anwendung zu starten, kann das Skript ausgeführt werden. Anschließend kann die Anwendung im Browser unter `localhost:8000` aufgerufen werden.

Wir werden uns als nächstes das Layout und in dem Zusammenhang die verschiedenen Komponenten und Möglichkeiten für das Styling von Dash-Anwendungen ansehen.






