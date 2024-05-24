import os
import pandas as pd
import json
import os
from Common_Git_Clone_Path.Local_Path_Func import Local_Path_Func

def Hover_State_Tran_Func():
    x=Local_Path_Func()
    path= x+"/map/transaction/hover/country/india/state/"
    Agg_state_list=os.listdir(path)
    Agg_state_list

    clm={'District_Name':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

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
                #print(D)
                try:
                    for z in D['data']['hoverDataList']:
                        Name=z['name']
                        count=z['metric'][0]['count']
                        amount=z['metric'][0]['amount']
                        type=z['metric'][0]['type']
                        clm['Transaction_type'].append(type)
                        clm['Transaction_count'].append(count)
                        clm['Transaction_amount'].append(amount)
                        clm['District_Name'].append(Name)
                        clm['Year'].append(j)
                        clm['Quater'].append(int(k.strip('.json')))
                except:
                    pass
#Succesfully created a dataframe
    Hover_State_Trans=pd.DataFrame(clm)
    to_drop = ['Transaction_amount',
               'Transaction_type',
               'Quater']
    Hover_State_Trans.drop(to_drop, inplace=True, axis=1)

    # replacing and capitalising the states as per requirement
    Hover_State_Trans['District_Name']=Hover_State_Trans['District_Name'].str.replace('district', '')
    Hover_State_Trans['District_Name'].str.strip()
    Hover_State_Trans.District_Name = Hover_State_Trans.District_Name.str.title()
    avg_transactions_by_district = Hover_State_Trans.groupby(['District_Name', 'Year'], as_index=False)
    average_transaction_df = avg_transactions_by_district.mean()
    return average_transaction_df
#x=Hover_State_Tran_Func()
#print(x)