
import numpy as np
import pandas as pd
import plotly.express as px
from .globals import dataPath, shapsPath

class tabManager:


    def __init__(self,
                 dataType: str,
                 data: pd.DataFrame,
                 shaps: pd.DataFrame,
                 alpha: float = 0.05,
                 ):
        
        self.dataType = dataType;
        self.alpha = alpha;
        
        self.data = data[data["Data_type"] == self.dataType];
        self.shaps = shaps[shaps["Data_type"] == self.dataType];

    

    def draw_dependency(self, feature: str):
        
        if feature[4:6] == "lh":
            titleNameFeature = f"left {feature[7:]}";
            color = ["blue"];
            
        else:
            titleNameFeature = f"right {feature[7:]}";
            color = ["darkorange"];
        
        fig = px.scatter(data_frame = self.shaps, 
                        x = feature, 
                        labels={
                            feature: "SHAP values",
                            "Age": "Age [years]",
                        },
                        y = "Age",
                        title = f"Dependency plot: {titleNameFeature}",
                        color_discrete_sequence = color,
                        );
    
        return fig




    def draw_manhattan(self):
    
        ''' Draw manhattan plot '''
        

        fig = px.scatter(data_frame = self.data, 
                            x = "Feature", 
                            y = "-log10(p value)",
                            title = "Manhattan plot",
                            color = "Position",
                            color_discrete_sequence = ["blue","darkorange"],
                        );

        fig.add_hline(y = -np.log10(self.alpha), 
                        line_color = 'red', 
                        line_dash = 'dash', 
                        annotation_text = "alpha",
                        annotation_position="bottom left",
                    );


        fig.add_hline(y = -np.log10(self.alpha/self.data.shape[0]), 
                        line_color = 'green', 
                        line_dash = 'dash', 
                        annotation_text = "Corr. alpha",
                        annotation_position="top left",
                    );
        
        fig.update_xaxes(tickangle=-60);
        
        return fig