import pandas as pd
import json
import os
from Common_Git_Clone_Path.Local_Path_Func import Local_Path_Func
#This is to direct the path to get the data as states
def clean_nones(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_nones(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value

def Aggregated_India_User_Func():
    x=Local_Path_Func()
    path= x+"/aggregated/user/country/india/"
    yr_list=os.listdir(path)
    yr_list_final=[]
    for i in yr_list:
        if(i.isnumeric()):
            yr_list_final.append(i)

#Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

    clm={'Country':'India','Year':[],'Quater':[],'Brand':[], 'Count':[], 'Percentage':[]}
    clm1={'value':[]}
    for j in yr_list_final:
        p_j=path+j+"/"
        Agg_json_list = os.listdir(p_j)
        for k in Agg_json_list:
            p_k = p_j + k
            Data=open(p_k,'r')
            D=json.load(Data)
            l1=[]
            cleaned_data = clean_nones(D)
            #print(cleaned_data)
            #print(D)
            try:
                for z in cleaned_data['data']['usersByDevice']:
                #print(z)
                    brand = z['brand']
                    count = z['count']
                    percentage = z['percentage']
                    clm['Brand'].append(brand)
                    clm['Count'].append(count)
                    clm['Percentage'].append(percentage)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
#Succesfully created a dataframe
#print(clm)
    Agg_User_India=pd.DataFrame(clm)
    return Agg_User_India
#x=Aggregated_India_User_Func()
#print(x)


