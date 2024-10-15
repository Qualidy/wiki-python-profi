# Daten zwischen Dash-Komponenten teilen

Wie auch bei anderen Anwendungen wollen wir in Dash globale Variablen vermeiden. Insbesondere, da Dash serverseitig arbeitet, können globale Variablen zu unerwartetem Verhalten führen. Stattdessen können Daten zwischen verschiedenen Dash-Komponenten geteilt werden, indem wir ein `Store` Objekt verwenden. Das Store Objekt kann Daten sogar über einen längeren Zeitraum speichern und selbst nach einem Neustart der Anwendung wieder aufrufen.


## dcc.Store

Das `dcc.Store`-Komponente wird verwendet, um Daten temporär zu speichern. Die Daten werden im Browser des Benutzers gespeichert und gehen nicht verloren, wenn die Seite neu geladen wird.

```python
import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', type='text', value=''),
    dcc.Store(id='store'),
    html.Div(id='output'),
    html.Button('Clear Data', id='clear-button')
])

@app.callback(
    dash.dependencies.Output('store', 'data'),
    [dash.dependencies.Input('input', 'value')]
)
def update_store(input_value):
    return input_value

@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('store', 'data')]
)
def update_output(data):
    return f'Input: {data}'

@app.callback(
    dash.dependencies.Output('store', 'data'),
    [dash.dependencies.Input('clear-button', 'n_clicks')]
)
def clear_data(n_clicks):
    if n_clicks:
        return None

if __name__ == '__main__':
    app.run_server(debug=True)
```

Dadurch, dass die Daten in einer eigenen Component liegen, können Sie als State zwischen den Components geteilt werden. In dem Objekt liegen die Daten im Json Format vor.


