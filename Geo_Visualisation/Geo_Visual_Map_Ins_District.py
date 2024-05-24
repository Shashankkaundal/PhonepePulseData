import geojson as geojson
import pandas as pd
import plotly.express as px
from Transaction_Count_By_Year.Tran_Count_By_Year_Map import Trans_Data_For_Map_By_Year
from Transaction_Count_By_Year.Tran_Count_By_Year_Dist_Map import Trans_Data_For_Dist_Map_By_Year
from Insurance_Count_By_Year.Insurance_Count_By_Year_Map_Dist import Ins_Data_For_Map_By_Dist_Year
def trim(dataset):
    trim = lambda x: x.strip() if type(x) is str else x
    return dataset.map(trim)

def geo_visual_func_ins_district(year):
    z=Ins_Data_For_Map_By_Dist_Year(year)
    with open('/Users/shashankkaundal/Downloads/PhonepePulseData/india_district.geojson') as f:
        gj = geojson.load(f)
    loc="/Users/shashankkaundal/Downloads/PhonepePulseData/Ins_Csv_For_Map/Ins_Dist.csv"
    dataset = trim(pd.read_csv(loc))
    #trim_func_call=trim(loc)
    #df= pd.read_csv("/Users/shashankkaundal/Downloads/PhonepePulseData/Tran_Csv_For_Map/dist.csv")
    df=dataset
    fig = px.choropleth(df,
        geojson=gj,
        featureidkey='properties.NAME_2',
        locations='District_Name',
        color='Transaction_count',
        color_continuous_scale='viridis_r'
        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #fig.show()
    return fig
#x=geo_visual_func_ins_district(2019)
#print(x)
