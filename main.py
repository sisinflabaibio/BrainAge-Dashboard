from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
from modules.funcs import load_data, load_shaps, update_dependecy, toyData
from modules.tab import tabManager

from modules.globals import startFeature, serverAdress, serverPort


''' Load data and draw plot'''

tab_deep= tabManager("DeepSHAP", load_data(), load_shaps());
tab_vol = tabManager("Gray matter volume", load_data(), load_shaps());
tab_avg = tabManager("Average thickness", load_data(), load_shaps());



''' Start app and manage Layout '''

app = Dash()

# Layout of entire page
app.layout = html.Div([  
    
    dcc.Tabs([
        
        dcc.Tab(label = "DeepSHAP", 
                children = [
                    html.Div([
                        dcc.Graph(id='manhattanPlotDeep',
                                  figure = tab_deep.draw_manhattan(),
                                  config={
                                        'displayModeBar': False
                                    })],
                        style = {   
                                'padding-top': '10px',         
                                'float': 'left',
                                'display': 'inline-block',
                                'width':'70%',}),
    
                    html.Div([
                        dcc.Graph(id='dependencyPlotDeep',
                                  figure = tab_deep.draw_dependency(startFeature),
                                  config={
                                        'displayModeBar': False
                                    })],
                        style = {
                                'padding-top': '10px',
                                'display': 'inline-block',
                                'float': 'right',
                                'width':'30%'}),
                            ]),

    
        dcc.Tab(label = "Gray matter volume", 
                children = [
                    html.Div([
                        dcc.Graph(id='manhattanPlotVol',
                                  figure = tab_vol.draw_manhattan(),
                                  config={
                                        'displayModeBar': False
                                    })],                              
                        style = {   
                                'padding-top': '10px',         
                                'float': 'left',
                                'display': 'inline-block',
                                'width':'70%',}),
    
                    html.Div([
                        dcc.Graph(id='dependencyPlotVol',
                                  figure = tab_vol.draw_dependency(startFeature),
                                  config={
                                        'displayModeBar': False
                                    })],
                        style = {
                                'padding-top': '10px',
                                'display': 'inline-block',
                                'float': 'right',
                                'width':'30%'}),
                            ]),



        dcc.Tab(label = "Average thickness", 
                children = [
                    html.Div([
                        dcc.Graph(id='manhattanPlotAvg',
                                  figure = tab_avg.draw_manhattan(),
                                  config={
                                        'displayModeBar': False
                                    })],
                        style = {   
                                'padding-top': '10px',         
                                'float': 'left',
                                'display': 'inline-block',
                                'width':'70%',}),
    
                    html.Div([
                        dcc.Graph(id='dependencyPlotAvg',
                                  figure = tab_avg.draw_dependency(startFeature),
                                  config={
                                        'displayModeBar': False
                                    })],
                        style = {
                                'padding-top': '10px',
                                'display': 'inline-block',
                                'float': 'right',
                                'width':'30%'}),
                            ]),
                    
    ])
      
]);    
    
    


''' Callbacks '''


@callback(
    Output('dependencyPlotDeep', 'figure'),
    Input('manhattanPlotDeep', 'clickData')
)
def update_dependecy_deep(clickData):
    if clickData is None:
        clickData = toyData();
    return update_dependecy(clickData, tab_deep);


@callback(
    Output('dependencyPlotAvg', 'figure'),
    Input('manhattanPlotAvg', 'clickData')
)
def update_dependecy_deep(clickData):
    if clickData is None:
        clickData = toyData();
    return update_dependecy(clickData, tab_avg);


@callback(
    Output('dependencyPlotVol', 'figure'),
    Input('manhattanPlotVol', 'clickData')
)
def update_dependecy_deep(clickData):
    if clickData is None:
        clickData = toyData();
    return update_dependecy(clickData, tab_vol);




''' Run server '''

if __name__ == '__main__':
    app.run(debug=False);
