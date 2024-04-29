import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px


df = pd.read_csv('daily_sales_data_0.csv')

app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer"),
    dcc.Graph(id='sales-chart'),
])

@app.callback(
    dash.dependencies.Output('sales-chart', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_chart(selected_region):
    filtered_df = df[df['Region'] == selected_region]
    fig = px.line(filtered_df, x='Date', y='Sales', title='Sales Data')
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
