import os
import pandas as pd
import json
import os
from Common_Git_Clone_Path.Local_Path_Func import Local_Path_Func

def Aggr_State_Tran_Func():
    x=Local_Path_Func()
    path= x+"/aggregated/transaction/country/india/state/"
    Agg_state_list=os.listdir(path)
    Agg_state_list

    clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

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
                    for z in D['data']['transactionData']:
                        Name=z['name']
                        count=z['paymentInstruments'][0]['count']
                        amount=z['paymentInstruments'][0]['amount']
                        clm['Transaction_type'].append(Name)
                        clm['Transaction_count'].append(count)
                        clm['Transaction_amount'].append(amount)
                        clm['State'].append(i)
                        clm['Year'].append(j)
                        clm['Quater'].append(int(k.strip('.json')))
                except:
                    pass
#Succesfully created a dataframe
    Agg_State_Trans=pd.DataFrame(clm)
    return Agg_State_Trans
#x=Aggr_State_Tran_Func()
#print(x)