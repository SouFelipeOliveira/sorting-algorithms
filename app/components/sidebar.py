
import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

import time

from datetime import datetime as dt, date
import plotly.express as px
import numpy as np
import pandas as pd



layout = dbc.Col([
    html.H1('Dashboard', className='text-primary'),
    html.P('By Felipe Oliveira', className='text-secondary'),
    html.Hr(),


# Botão para gerar arrays
    # dbc.Button(id='logo-uerr', children=[html.Img(src='assets/Logotipo-UERR-Cores-Sólidas.png')],
    #             style={'background-color': 'transparent', 'border-color': 'transparent', 'width': 'auto', 'height': 'auto'}
    #         ),
    
    dbc.Row([
        dbc.Col([
            dbc.Button('Gerar Arrays', id='generate-arrays', color='success')
        ]),
        dbc.Col([
            dbc.Button('Deletar Arrays', id='delete-arrays', color='danger')
        ]),
    ]),


    dbc.Alert('Arays deletados com sucesso!', color='warning', id='alert-delete', is_open=False),
    dbc.Alert('Arays gerados com sucesso!', color='success', id='alert-generate', is_open=False),

# Botão para deletar arrays




# Navegação entre overview e os algoritmos
    
    dbc.Nav([
        dbc.NavLink('Visão geral', href='/overview', active='exact'),
        dbc.NavLink('Algoritmos', href='/algorithms', active='exact'),
        html.Hr(),
        html.H2('Algoritmos de Ordenação', className='text-primary'),
        dbc.NavLink('Bubble Sort', href='/bubble_sort', active='exact'),
        dbc.NavLink('Gnome Sort', href='/gnome_sort', active='exact'),
        dbc.NavLink('Heap Sort', href='/heap_sort', active='exact'),
        dbc.NavLink('Insertion Sort', href='/insertion_sort', active='exact'),
        dbc.NavLink('Merge Sort', href='/merge_sort', active='exact'),
        dbc.NavLink('Quick Sort', href='/quick_sort', active='exact'),
        dbc.NavLink('Selection Sort', href='/selection_sort', active='exact'),
    ],vertical=True, pills=True, id='tabs', style={"margin-bottom": "50px", "margin-top": "30px"}),

    # dbc.Card([
    #     dbc.CardBody(id='card-content')
    # ])
], id='sidebar')



@app.callback(Output('alert-delete', 'is_open'), Input('delete-arrays', 'n_clicks'), State('delete-arrays', 'is_open'))
def toggle(n, is_open):
    if n:
        return not is_open

@app.callback(Output('alert-generate', 'is_open'), Input('generate-arrays', 'n_clicks'), State('delete-arrays', 'is_open'))
def toggle(n, is_open):
    if n:
        return not is_open
    return is_open