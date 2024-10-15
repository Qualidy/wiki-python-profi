# Multipage Apps

Seit dash 2.5. gibt es die Möglichkeit, in Dash Apps mit mehreren Seiten durch eine Ordnerstruktur, ähnlich zu NextJS zu erstellen. 

```
app.py
pages/
    __init__.py
    home.py
    archive.py
```

Die einzelnen Seiten werden über das keyword argument `use_pages=True` in der app initialisierung aktiviert. 

```python
import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)
```

Die einzelnen Seiten werden in den `page`-Dateien definiert. 


Seite `home.py`
```python
import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
])
```


Seite `archive.py`
```python
import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is our Archive page'),
    html.Div('This is our Archive page content.'),
])
```


