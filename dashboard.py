import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Interactive Data Visualization Dashboard"),
    
    dcc.Dropdown(
        id="variable-selector",
        options=[
            {"label": "Temperature (°C)", "value": "temperature"},
            {"label": "Humidity (%)", "value": "humidity"},
            {"label": "Sales (units)", "value": "sales"},
        ],
        value="temperature",
        clearable=False
    ),

    dcc.Graph(id="time-series-graph"),

    dcc.Interval(
        id="interval-component",
        interval=5000,
        n_intervals=0
    )
])

@app.callback(
    Output("time-series-graph", "figure"),
    [Input("variable-selector", "value"), Input("interval-component", "n_intervals")]
)
def update_graph(selected_variable, n_intervals):
    df = pd.read_csv("data.csv")
    df["date"] = pd.to_datetime(df["date"])

    fig = px.line(df, x="date", y=selected_variable, title=f"{selected_variable.capitalize()} Over Time")
    fig.update_traces(line=dict(width=3)) 
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
