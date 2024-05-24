from PhonePeDataExtract.Data_Extractions.Map_Data_Extracts.Trans_Hover_Extract.Tran_Hover_India_Extract import Hover_India_Tran_Func
import pandas as pd
import os
import pandas as pd
pd.options.mode.chained_assignment = None
def Trans_Data_For_Map_By_Year(year):
    #
    x=Hover_India_Tran_Func()
    year= x[x["Year"]==str(year)]
    #path = "/Users/shashankkaundal/Downloads/PhonepePulseData/Tran_Csv_For_Map/"+str(year)
    #loc='/Users/shashankkaundal/Downloads/PhonepePulseData/Tran_Csv_For_Map/'
    #file_type='.csv'
    #fullpath=loc+str(year)+file_type
    to_drop = ['Year']
    year.drop(to_drop, inplace=True, axis=1)
    year.to_csv("/Users/shashankkaundal/Downloads/PhonepePulseData/Tran_Csv_For_Map/year.csv", index=False)
    return year
#x=Trans_Data_For_Map_By_Year()
#print(x)