# Callbacks

Bisher haben unsere Dashboards nur statische Inhalte angezeigt. Um die Interaktivität zu erzeugen, können wir Callbacks verwenden. Callbacks sind Funktionen, die aufgerufen werden, wenn ein bestimmtes Ereignis eintritt. Beispielsweise kann eine Callback-Funktion aufgerufen werden, wenn ein Button gedrückt wird.

In Dash ermöglichen Callbacks, die Anwendung dynamisch zu aktualisieren, basierend auf Benutzereingaben oder anderen Ereignissen.

Ein Callback in Dash besteht aus drei Teilen:

- **Input**: Das Ereignis, auf das reagiert werden soll. Dies kann beispielsweise ein Klick auf einen Button oder eine Änderung in einem Eingabefeld sein.
- **Output**: Die Komponente, die aktualisiert werden soll. Dies kann beispielsweise ein Textfeld oder ein Diagramm sein.
- **Callback-Funktion**: Die Funktion, die aufgerufen wird, wenn das Ereignis eintritt. Diese Funktion nimmt die Eingabewerte entgegen, verarbeitet sie und gibt die aktualisierten Werte zurück.

Um Callbacks in Dash zu definieren, verwenden wir das `@app.callback`-Dekorator. Das Dekorator wird über der Callback-Funktion platziert und nimmt die Input- und Output-Komponenten als Argumente. Hier ist ein einfaches Beispiel für die Verwendung von Callbacks in Dash:

```python
import dash
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Click Me', id='button'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('button', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        return 'No clicks yet'
    else:
        return f'Button clicked {n_clicks} times'

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird eine einfache Dash-Anwendung erstellt, die einen Button und ein Textfeld enthält. Der Text im Textfeld wird aktualisiert, wenn der Button geklickt wird. Die Callback-Funktion `update_output` wird aufgerufen, wenn der Button geklickt wird, und aktualisiert den Text basierend auf der Anzahl der Klicks.

## Inhaltsverzeichnis

- [Callbacks](#callbacks)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Inputs und Outputs](#inputs-und-outputs)
    - [Callbacks mit mehreren Inputs/Outputs](#callbacks-mit-mehreren-inputsoutputs)
  - [State](#state)
  - [Speichereffizienz in Dash](#speichereffizienz-in-dash)
    - [Aufrufen des Callbacks bei Initialisierung](#aufrufen-des-callbacks-bei-initialisierung)
    - [Verwendung von `prevent_initial_call`](#verwendung-von-prevent_initial_call)
    - [Caching von Ergebnissen](#caching-von-ergebnissen)
    - [Patch für partielle Updates](#patch-für-partielle-updates)

## Inputs und Outputs

Inputs und Outputs in Dash sind die Komponenten, die in der Callback-Funktion verwendet werden. Inputs sind die Ereignisse, auf die reagiert werden soll, während Outputs die Komponenten sind, die aktualisiert werden sollen.

Inputs und Outputs in Dash werden als Listen von `dash.dependencies.Input` und `dash.dependencies.Output`-Objekten definiert. Diese Objekte nehmen die ID und den Attributnamen der Komponenten als Argumente.

Ein Beispiel für die Definition von Inputs und Outputs:

```python
import dash
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def update_output(value):
    return f'Input value: {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird ein Eingabefeld (`dcc.Input`) und ein Textfeld (`html.Div`) erstellt. Der Text im Textfeld wird aktualisiert, wenn der Wert im Eingabefeld geändert wird. Die Callback-Funktion `update_output` wird aufgerufen, wenn der Wert im Eingabefeld geändert wird, und aktualisiert den Text basierend auf dem neuen Wert.


### Callbacks mit mehreren Inputs/ Outputs

Dash ermöglicht es auch, mehrere Inputs und Outputs in einer Callback-Funktion zu verwenden. Dies ermöglicht es, die Anwendung basierend auf mehreren Ereignissen zu aktualisieren.

```python
import dash
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input1', value='initial value', type='text'),
    dcc.Input(id='input2', value='initial value', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input('input1', 'value'), Input('input2', 'value')]
)
def update_output(value1, value2):
    return f'Input value 1: {value1}, Input value 2: {value2}'

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel werden zwei Eingabefelder (`dcc.Input`) und ein Textfeld (`html.Div`) erstellt. Der Text im Textfeld wird aktualisiert, wenn der Wert in einem der Eingabefelder geändert wird. Die Callback-Funktion `update_output` nimmt die Werte der beiden Eingabefelder entgegen und aktualisiert den Text basierend auf den neuen Werten.

Gleichermaßen können auch mehrere Outputs in einer Callback-Funktion verwendet werden:

```python
import dash
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value', type='text'),
    html.Div(id='output1'),
    html.Div(id='output2')
])

@app.callback(
    [Output('output1', 'children'), Output('output2', 'children')],
    Input('input', 'value')
)
def update_output(value):
    return f'Output 1: {value}', f'Output 2: {value}'
```

In diesem Beispiel wird ein Eingabefeld (`dcc.Input`) und zwei Textfelder (`html.Div`) erstellt. Die Textfelder werden aktualisiert, wenn der Wert im Eingabefeld geändert wird. Die Callback-Funktion `update_output` nimmt den Wert des Eingabefelds entgegen und aktualisiert beide Textfelder basierend auf dem neuen Wert.

Oftmals möchten wir zwar mehrere Eingaben verwenden, jedoch nicht bei jedem Input die Callback-Funktion ausführen. In diesem Fall können wir die `State`-Komponente verwenden.


## State

State in Dash ist ein Konzept, das verwendet wird, um den internen Zustand der Anwendung zu speichern. State kann verwendet werden, um Informationen zwischen Callbacks zu übertragen oder um den Zustand einer Komponente zu speichern.

In Dash wird State als Liste von `dash.dependencies.State`-Objekten definiert. Diese Objekte nehmen die ID und den Attributnamen der Komponenten als Argumente.

Ein Beispiel für die Verwendung von State:

```python
import dash
from dash import html, dcc, Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value', type='text'),
    html.Button('Submit', id='button'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('button', 'n_clicks'),
    State('input', 'value')
)
def update_output(n_clicks, value):
    if n_clicks is None:
        return 'No clicks yet'
    else:
        return f'Button clicked {n_clicks} times, Input value: {value}'
```

In diesem Beispiel wird ein Eingabefeld (`dcc.Input`), ein Button (`html.Button`) und ein Textfeld (`html.Div`) erstellt. Der Text im Textfeld wird aktualisiert, wenn der Button geklickt wird. Die Callback-Funktion `update_output` wird aufgerufen, wenn der Button geklickt wird, und aktualisiert den Text basierend auf der Anzahl der Klicks und dem Wert im Eingabefeld.

## Speichereffizienz in Dash

Normalerweise werden Callback-Funktionen in Dash serverseitig aufgerufen, wenn ein Ereignis eintritt. Dies kann bei vielen Aufrufen und großen Datenmengen zu einer Verzögerung führen, die wir vermeiden möchten. Wir werden uns nun einige Möglichkeiten ansehen, um Ressourcen zu schonen und die Effizienz von Dash-Anwendungen zu verbessern.

### Aufrufen des Callbacks bei Initialisierung

 Eine Möglichkeit um Ressourcen zu schonen ist es, die Callback-Funktion clientseitig aufzurufen.

Manchmal möchten wir, dass ein Callback-Funktion bei der Initialisierung der Anwendung aufgerufen wird. Dies kann beispielsweise nützlich sein, um den Anfangszustand der Anwendung zu setzen.

In Dash können wir das `app.clientside_callback`-Dekorator verwenden, um eine Callback-Funktion bei der Initialisierung der Anwendung aufzurufen.

```python
import dash
from dash import html, dcc, Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value', type='text'),
    html.Div(id='output')
])

@app.clientside_callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def update_output(value):
    return f'Input value: {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird ein Eingabefeld (`dcc.Input`) und ein Textfeld (`html.Div`) erstellt. Der Text im Textfeld wird aktualisiert, wenn der Wert im Eingabefeld geändert wird. Die Callback-Funktion `update_output` wird bei der Initialisierung der Anwendung aufgerufen und setzt den Text basierend auf dem Anfangswert des Eingabefelds.

### Verwendung von `prevent_initial_call`

Manchmal möchten wir verhindern, dass eine Callback-Funktion bei der Initialisierung der Anwendung aufgerufen wird. Dies kann nützlich sein, wenn die Callback-Funktion teure Berechnungen durchführt oder auf externe Ressourcen zugreift.

In Dash können wir das Argument `prevent_initial_call=True` verwenden, um zu verhindern, dass eine Callback-Funktion bei der Initialisierung der Anwendung aufgerufen wird.

```python
import dash
from dash import html, dcc, Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('input', 'value'),
    prevent_initial_call=True
)
def update_output(value):
    return f'Input value: {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird ein Eingabefeld (`dcc.Input`) und ein Textfeld (`html.Div`) erstellt. Der Text im Textfeld wird aktualisiert, wenn der Wert im Eingabefeld geändert wird. Die Callback-Funktion `update_output` wird nur aufgerufen, wenn der Wert im Eingabefeld geändert wird, nicht bei der Initialisierung der Anwendung.

### Caching von Ergebnissen

Eine weitere Möglichkeit, Ressourcen zu schonen, ist das Caching von Ergebnissen. Das Caching ermöglicht es, die Ergebnisse von teuren Berechnungen zu speichern und bei Bedarf wiederzuverwenden.

In Dash können wir das `@cache`-Dekorator verwenden, um die Ergebnisse einer Callback-Funktion zu cachen.

```python
import dash
from dash import html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate
from dash_extensions import Input, Output, State, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('input', 'value')
)
@cache.memoize()
def update_output(value):
    return f'Input value: {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird ein Eingabefeld (`dcc.Input`) und ein Textfeld (`html.Div`) erstellt. Der Text im Textfeld wird aktualisiert, wenn der Wert im Eingabefeld geändert wird. Die Callback-Funktion `update_output` wird die Ergebnisse cachen, um Ressourcen zu sparen.

### Aufgabe:

Erstellen Sie ein Dashboard mit folgenden Komponenten und Funktionen:

1. Zwei Eingabefelder (`dcc.Input`) für numerische Werte.
2. Ein Dropdown-Menü (`dcc.Dropdown`) mit verschiedenen mathematischen Operationen (Addition, Subtraktion, Multiplikation, Division).
3. Ein Button zum Ausführen der Berechnung.
4. Zwei Ausgabefelder (`html.Div`):
    - Ein Feld, das das Ergebnis der Berechnung anzeigt.
    - Ein Feld, das die Anzahl der Berechnungen anzeigt.

Verwenden Sie einen Callback mit mehreren Inputs (die beiden Eingabefelder und das Dropdown-Menü) und mehreren Outputs (die beiden Ausgabefelder).
Nutzen Sie den `State` für die Eingabefelder und das Dropdown-Menü, sodass die Berechnung erst bei Knopfdruck ausgeführt wird.
Verwenden Sie `prevent_initial_call=True`, um zu verhindern, dass der Callback bei der Initialisierung aufgerufen wird.
Implementieren Sie eine einfache Caching-Strategie für die Berechnungsfunktion.
