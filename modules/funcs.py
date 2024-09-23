import numpy as np
import pandas as pd
from .tab import tabManager
from .globals import dataPath, shapsPath

''' Here there are some support functions '''


def load_data():
    return pd.read_csv(dataPath);


def load_shaps():
    return pd.read_csv(shapsPath);


def update_dependecy(clickData: dict, manager: tabManager):
    
    ''' Redraw dependency plot on click of a point in manhattan plot  '''
    
    featureData = clickData['points'][0]["x"];
    index = clickData['points'][0]["curveNumber"];
    
    feature = convert_feature_name(featureData, index);
    
    return manager.draw_dependency(feature);


def toyData():
    return {"points": [{"x": 'bankssts', "curveNumber": 0}]};


def convert_feature_name(feature: str, index: int):
    
    if index == 1:
        return f"ctx-rh-{feature}";
    
    else:
        return f"ctx-lh-{feature}";
    