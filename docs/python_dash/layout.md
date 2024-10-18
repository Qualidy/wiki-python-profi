# Erstellung von Layouts

Die visuelle Gestaltung von Dash-Anwendungen erfolgt über das Layout. Im Layout werden die Komponenten festgelegt, die in der Anwendung angezeigt werden. Die Komponenten können beispielsweise Textfelder, Schaltflächen oder Diagramme sein.

Dash bietet verschiedene Module, die die Erstellung von Layouts erleichtern. Die wichtigsten Module sind:

- `dash.html`: Enthält HTML-Elemente wie Überschriften, Textfelder oder Schaltflächen.
- `dash.core_components`: Enthält interaktive Komponenten wie Diagramme, Dropdown-Menüs oder Schieberegler.
- `dash.dcc`: Enthält alle Komponenten aus `dash.core_components` und `dash.html`.

In diesem Kapitel werden wir uns die verschiedenen Komponenten und Möglichkeiten für das Styling von Dash-Anwendungen ansehen.

## Inhaltsverzeichnis

- [Erstellung von Layouts](#erstellung-von-layouts)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [HTML-Elemente](#html-elemente)
  - [Interaktive Komponenten](#interaktive-komponenten)

## HTML-Elemente

Das Modul `dash.html` enthält verschiedene HTML-Elemente, die in Dash-Anwendungen verwendet werden können. Die Elemente können beispielsweise Überschriften, Textfelder oder Schaltflächen sein.

Einige Beispiele für HTML-Elemente sind:

- `html.H1`: Erstellt eine Überschrift der Größe 1.
- `html.P`: Erstellt einen Absatz.
- `html.Button`: Erstellt eine Schaltfläche.

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Hello World'),
    html.P('This is a paragraph.'),
    html.Button('Click Me', id='button')
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird eine einfache Dash-Anwendung erstellt, die eine Überschrift, einen Absatz und eine Schaltfläche enthält.

## Interaktive Komponenten

Das Modul `dash.core_components` enthält interaktive Komponenten, die in Dash-Anwendungen verwendet werden können. Die Komponenten können beispielweise Diagramme, Dropdown-Menüs oder Schieberegler sein. Das Modul `dash.dcc` enthält alle Komponenten aus `dash.core_components` und `dash.html`. Wir verwenden in diesem Kapitel `dash.dcc`.

Einige Beispiele für interaktive Komponenten sind:

- `dcc.Graph`: Erstellt ein Diagramm.
- `dcc.Dropdown`: Erstellt ein Dropdown-Menü.
- `dcc.Slider`: Erstellt einen Schieberegler.

```python
import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Berlin'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'München'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Berlin', 'value': 'Berlin'},
            {'label': 'München', 'value': 'München'}
        ],
        value='Berlin'
    ),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: str(i) for i in range(10)},
        value=5
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird eine Dash-Anwendung erstellt, die ein Diagramm, ein Dropdown-Menü und einen Schieberegler enthält. Das Diagramm zeigt zwei Balkendiagramme für die Städte Berlin und München.

### Aufgabe:

Erstelle eine Dash-Anwendung für einen Discounter, die folgende Elemente enthält:

1. Eine Überschrift (H1) mit dem Namen des Discounters.
2. Ein Dropdown-Menü zur Auswahl verschiedener Produktkategorien (z.B. Obst, Gemüse, Milchprodukte).
3. Ein Balkendiagramm, das die Verkaufszahlen für die Top 5 Produkte der ausgewählten Kategorie anzeigt.
4. Einen Schieberegler, mit dem der Benutzer einen Preisbereich auswählen kann.

Verwende dazu die passenden Komponenten aus `dash.html` und `dash.dcc`.