# Styles

Ähnlich, wie wir in html und css Styles verwenden können, um das Aussehen einer Webseite zu verändern, können wir auch in Dash-Anwendungen Styles verwenden, um das Aussehen der Anwendung zu verändern. In Dash können Styles entweder inline oder über externe Stylesheets definiert werden. 

Neben den Standard-HTML- und CSS-Styles können in Dash auch Third-Party-Styles verwendet werden. Zu den Dash-Styles gehören beispielsweise die Bootstrap-Styles, die in Dash integriert sind und verwendet werden können, um das Aussehen der Anwendung zu verändern.

## Inhaltsverzeichnis

- [Styles](#styles)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Inline Styles](#inline-styles)
  - [Externe Stylesheets](#externe-stylesheets)
  - [Dash Bootstrap](#dash-bootstrap)

## Inline Styles

Inline Styles sind Styles, die direkt in den Komponenten definiert werden. Sie werden als Python-Dictionary übergeben und können beispielsweise die Farbe, Schriftgröße oder den Abstand eines Elements festlegen.

Ein Beispiel für die Verwendung von Inline Styles ist:

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    children='Hello World',
    style={
        'color': 'red',
        'fontSize': 24,
        'margin': 20
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird ein `html.Div`-Element erstellt, das den Text 'Hello World' enthält. Das Element hat die Farbe Rot, eine Schriftgröße von 24 und einen Abstand von 20 Pixeln.

## Externe Stylesheets

Externe Stylesheets sind Styles, die in einer separaten CSS-Datei definiert werden. Diese Stylesheets können dann in der Dash-Anwendung eingebunden werden, um das Aussehen der Anwendung zu verändern.

Ein Beispiel für die Verwendung von externen Stylesheets ist:

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    children='Hello World',
    className='my-class'
)

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird ein `html.Div`-Element erstellt, das den Text 'Hello World' enthält. Das Element verwendet die Klasse `my-class`, die in einem externen Stylesheet definiert ist. Das Stylesheet könnte beispielsweise folgenden Inhalt haben:

```css
.my-class {
    color: red;
    font-size: 24px;
    margin: 20px;
}
```

Um dieses Stylesheet in der Dash-Anwendung zu verwenden, muss es im gleichen Verzeichnis wie das Skript gespeichert werden und den Namen `styles.css` haben. Anschließend kann es in der Dash-Anwendung eingebunden werden, indem der Parameter `external_stylesheets` an die `dash.Dash`-Instanz übergeben wird:

```python
import dash
from dash import html

app = dash.Dash(__name__, external_stylesheets=['styles.css'])

app.layout = html.Div(
    children='Hello World',
    className='my-class'
)

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Dash Bootstrap

Ein einfacher Weg, um in kurzer Zeit zu optisch ansprechenden Komponenten zu kommen, ist die Verwendung von Dash Bootstrap. Dash Bootstrap ist eine Sammlung von vorgefertigten Komponenten und Layouts, die auf der Bootstrap-Bibliothek basieren.

Um Dash Bootstrap zu verwenden, muss das `dash_bootstrap_components`-Modul installiert und in der Dash-Anwendung eingebunden werden. Anschließend können die vorgefertigten Komponenten und Layouts verwendet werden, um das Aussehen der Anwendung zu verändern.

```python
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Alert('Hello World', color='primary'),
    className='my-class'
)

if __name__ == '__main__':
    app.run_server(debug=True)
```

In diesem Beispiel wird ein `dbc.Alert`-Element erstellt, das den Text 'Hello World' enthält. Das Element verwendet das Bootstrap-Theme `BOOTSTRAP`, das in der Dash-Anwendung eingebunden wird. Durch die Verwendung von Dash Bootstrap können schnell und einfach ansprechende Dash-Anwendungen erstellt werden.
