from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import app
from components import sidebar, overview

from components.algorithms import (
    component_bubble_sort,
    component_gnome_sort,
    component_heap_sort,
    component_insertion_sort,
    component_merge_sort,
    component_quick_sort,
    component_selection_sort
)

content = html.Div(id='page-content')

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url', refresh=False),
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10)
    ])
], fluid=True)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview.layout
    
    if pathname == '/bubble_sort':
        return component_bubble_sort.layout
    if pathname == '/gnome_sort':
        return component_gnome_sort.layout
    if pathname == '/heap_sort':
        return component_heap_sort.layout
    if pathname == '/insertion_sort':
        return component_insertion_sort.layout
    if pathname == '/merge_sort':
        return component_merge_sort.layout
    if pathname == '/quick_sort':
        return component_quick_sort.layout
    if pathname == '/selection_sort':
        return component_selection_sort.layout
    

if __name__ == '__main__':
    app.run_server(debug=True)