import pandas as pd
import plotly.express as px
from Transaction_Count_By_Year.Tran_Count_By_Year_Map import Trans_Data_For_Map_By_Year
def geo_visual_func(year):
    z=Trans_Data_For_Map_By_Year(year)
    df= pd.read_csv("/Users/shashankkaundal/Downloads/PhonepePulseData/Tran_Csv_For_Map/year.csv")
    fig = px.choropleth(df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State_Name',
        color='Transaction_count',
        color_continuous_scale='magma'
        )
    fig.update_geos(fitbounds="locations", visible=False)

    return fig

