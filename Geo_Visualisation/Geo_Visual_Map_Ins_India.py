import pandas as pd
import plotly.express as px

from Transaction_Count_By_Year.Tran_Count_By_Year_Map import Trans_Data_For_Map_By_Year
from Insurance_Count_By_Year.Insurance_Count_By_Year_Map_Ind import Ins_Data_For_Map_By_Year
def geo_visual_ins_func(year):
    z=Ins_Data_For_Map_By_Year(year)
    df= pd.read_csv("/Users/shashankkaundal/Downloads/PhonepePulseData/Ins_Csv_For_Map/Ins_India.csv")
    fig = px.choropleth(df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State_Name',
        color='Transaction_count',
        color_continuous_scale='inferno'
        )
    fig.update_geos(fitbounds="locations", visible=False)
    #fig.update_traces(mode="markers+lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    return fig

