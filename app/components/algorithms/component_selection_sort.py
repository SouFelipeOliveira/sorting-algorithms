import dash_bootstrap_components as dbc
from dash import html



layout = dbc.Col([
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                html.H2('Selection Sort', className='card-title', style={'text-align': 'center'}),
            ])
            ])
        ])
    ], style={'padding-top': '20px'}),



    dbc.Row([
        # Lista com 10 elementos
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('10 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),

        # Lista com 50 elementos
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('50 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),

        # Lista com 100 elementos
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('100 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),
    ], style={'padding-top': '20px'}),


    dbc.Row([

        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('200 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),

        
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),

        
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('800 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),
    ], style={'padding-top': '20px'}),


    dbc.Row([
        # Lista com 10 elementos
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('1000 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),


        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('1500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),

        
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('2000 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),
    ], style={'padding-top': '20px'}),



     dbc.Row([
        # Lista com 10 elementos
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('3500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),


        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('4500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),

        
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('5500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),
    ], style={'padding-top': '20px'}),


    dbc.Row([
        # Lista com 10 elementos
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('6500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),


        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('7500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),

        
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('8500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),
    ], style={'padding-top': '20px'}),


    dbc.Row([
        # Lista com 10 elementos
        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('9500 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),


        dbc.Col([
            dbc.CardGroup([
            dbc.Card([
                html.Legend('10.000 Elementos')
            ], style={'padding-left': '16px', 'padding-top': '10px'}),
        ])
        ], width=4),
    ], style={'padding-top': '20px'}),
    
], style={'margin': '10px'})