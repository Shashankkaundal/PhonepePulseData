from PhonePeDataExtract.Data_Extractions.Map_Data_Extracts.Insurance_Hover_Extract.Ins_Hover_India_Data_Extract import \
    Hover_India_Ins_Func
import pandas as pd
import os
import pandas as pd
pd.options.mode.chained_assignment = None
def Ins_Data_For_Map_By_Year(year):
    #
    x=Hover_India_Ins_Func()
    year= x[x["Year"]==str(year)]
    to_drop = ['Year']
    year.drop(to_drop, inplace=True, axis=1)
    year.to_csv("/Users/shashankkaundal/Downloads/PhonepePulseData/Ins_Csv_For_Map/Ins_India.csv", index=False)
    return year
#x=Ins_Data_For_Map_By_Year(2020)
#print(x)