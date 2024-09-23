
import numpy as np
import pandas as pd
import plotly.express as px

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
            color = ["#5360FD"];
            
        else:
            titleNameFeature = f"right {feature[7:]}";
            color = ["#449E48"];
        
        fig = px.scatter(data_frame = self.shaps, 
                        x = feature, 
                        labels={
                            feature: "SHAP values",
                            "Age": "Age [years]",
                        },
                        y = "Age",
                        title = f"Dependence plot: {titleNameFeature}",
                        color_discrete_sequence = color,
                        );

        fig.update_layout(plot_bgcolor='#F5F5F5');
        
        fig.update_xaxes(showline=True,
                         ticks='outside',
                         linecolor='black',
                         gridcolor='white');
        
        fig.update_yaxes(ticks='outside',
                        showline=True,
                        linecolor='black',
                        gridcolor='white'
                        );     
        return fig




    def draw_manhattan(self):
    
        ''' Draw manhattan plot '''
        

        fig = px.scatter(data_frame = self.data, 
                            x = "Feature", 
                            y = "-log10(p value)",
                            title = "Manhattan plot",
                            color = "Position",
                            labels = {"Position": "Legend"},
                            color_discrete_sequence = ["#5360FD","#449E48"],
                        );

        fig.add_hline(y = -np.log10(self.alpha), 
                        line_color = 'red', 
                        line_dash = 'dash', 
                        showlegend = True,
                        name = '\u03B1 (5%)',
                    );


        fig.add_hline(y = -np.log10(self.alpha/self.data.shape[0]), 
                        line_color = 'orange', 
                        line_dash = 'dash', 
                        showlegend = True,
                        name = "Bonferroni \u03B1"
                    );
        
        fig.update_xaxes(tickangle=-60,
                         ticks='outside',
                         showline=True,
                         linecolor='black',
                         gridcolor='white');
        
        fig.update_yaxes(ticks='outside',
                        showline=True,
                        linecolor='black',
                        gridcolor='white'
                        );
        
        fig.update_layout(plot_bgcolor='#F5F5F5');
        
        return fig