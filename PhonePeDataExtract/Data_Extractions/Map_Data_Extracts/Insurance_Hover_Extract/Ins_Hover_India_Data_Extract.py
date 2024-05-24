import pandas as pd
import json
import os
from Common_Git_Clone_Path.Local_Path_Func import Local_Path_Func
#This is to direct the path to get the data as states
def Hover_India_Ins_Func():
    x=Local_Path_Func()
    path= x+"/map/insurance/hover/country/india/"
    yr_list=os.listdir(path)
    yr_list_final=[]
    for i in yr_list:
        if(i.isnumeric()):
            yr_list_final.append(i)

#Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

    clm={'State_Name':[],'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for j in yr_list_final:
        p_j=path+j+"/"
        Agg_json_list = os.listdir(p_j)
        for k in Agg_json_list:
            p_k = p_j + k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['hoverDataList']:
                    Name=z['name']
                    count=z['metric'][0]['count']
                    amount=z['metric'][0]['amount']
                    type=z['metric'][0]['type']
                    clm['Transaction_type'].append(type)
                    clm['Transaction_count'].append(count)
                    clm['Transaction_amount'].append(amount)
                    clm['State_Name'].append(Name)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
#Succesfully created a dataframe
#print(clm)
    Hover_Ins_India=pd.DataFrame(clm)
    to_drop = ['Transaction_amount',
               'Transaction_type',
               'Quater']
    Hover_Ins_India.drop(to_drop, inplace=True, axis=1)
    Hover_Ins_India.replace('dadra & nagar haveli & daman & diu', 'Dadra and Nagar Haveli and Daman and Diu')
    Hover_Ins_India.replace('andaman & nicobar islands', 'Andaman & Nicobar')
    Hover_Ins_India.State_Name = Hover_Ins_India.State_Name.str.title()
    ##Taking Mean of all transaction by states for all the years
    avg_transactions_by_state = Hover_Ins_India.groupby(['State_Name', 'Year'], as_index=False)
    average_transaction_df = avg_transactions_by_state.mean()
    # print(average_transaction_df)
    # average_transaction_df.to_csv('Hover_tran_data.csv', index=False)
    return average_transaction_df
#x=Hover_India_Ins_Func()
#print(x)
