import os
import pandas as pd
import json
import os
from Common_Git_Clone_Path.Local_Path_Func import Local_Path_Func

def Aggr_State_User_Func():
    x=Local_Path_Func()
    path= x+"/aggregated/user/country/india/state/"
    Agg_state_list=os.listdir(path)
    Agg_state_list

    clm={'State':[], 'Year':[],'Quater':[],'Brand':[], 'Count':[], 'Percentage':[]}

    for i in Agg_state_list:
        p_i=path+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                try:
                    for z in D['data']['usersByDevice']:
                        brand=z['brand']
                        count=z['count']
                        percentage=z['percentage']
                        clm['Brand'].append(brand)
                        clm['Count'].append(count)
                        clm['Percentage'].append(percentage)
                        clm['State'].append(i)
                        clm['Year'].append(j)
                        clm['Quater'].append(int(k.strip('.json')))
                except:
                    pass
#Succesfully created a dataframe
    #print(clm)
    Agg_State_user=pd.DataFrame(clm)
    return Agg_State_user
#x=Aggr_State_User_Func()
#print(x)