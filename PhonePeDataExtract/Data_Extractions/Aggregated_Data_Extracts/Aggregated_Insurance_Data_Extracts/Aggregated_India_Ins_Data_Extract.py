import pandas as pd
import json
import os
from Common_Git_Clone_Path.Local_Path_Func import Local_Path_Func
#This is to direct the path to get the data as states
def Aggregated_India_Ins_Func():
    x=Local_Path_Func()
    path= x+"/aggregated/insurance/country/india/"
    yr_list=os.listdir(path)
    yr_list_final=[]
    for i in yr_list:
        if(i.isnumeric()):
            yr_list_final.append(i)

#Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

    clm={'Country':'India','Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for j in yr_list_final:
        p_j=path+j+"/"
        Agg_json_list = os.listdir(p_j)
        for k in Agg_json_list:
            p_k = p_j + k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm['Transaction_type'].append(Name)
                    clm['Transaction_count'].append(count)
                    clm['Transaction_amount'].append(amount)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
#Succesfully created a dataframe
#print(clm)
    Agg_Ins_India=pd.DataFrame(clm)
    return Agg_Ins_India
