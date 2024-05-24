import MySQLdb
import mysql
import sqlalchemy
from sqlalchemy import create_engine
from ConfigHelpers.Sql_Alchamey_Helper import Sql_Alchamey_Helper
from DB_Config.DBconnect import db_connect
from PhonePeDataExtract.Data_Extractions.Aggregated_Data_Extracts.Aggregated_Insurance_Data_Extracts.Aggregated_State_Ins_Data_Extract import Aggr_State_Ins_Func
def Aggr_Ins_Dist_Table():
    configfile=db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""CREATE DATABASE IF NOT EXISTS PhonePePulse""")
    cursorObject.execute("""USE PhonePePulse""")
   # cursorObject.execute(aggr_tran_india)
    aggr_tan="""CREATE TABLE IF NOT EXISTS Aggr_Ins_Dist (
                            STATE VARCHAR(255),
                            YEAR YEAR(4),
                            QUATER INT,
                            TRANSACTION_TYPE VARCHAR(255),
                            TRANSACTION_COUNT bigint,
                            TRANSACTION_AMOUNT bigint
                            )"""
    cursorObject.execute(aggr_tan)
    z = Aggr_State_Ins_Func()
    sql_alchamey=Sql_Alchamey_Helper()
    # Step 3: Convert the Pandas DataFrame to a format for MySQL table insertion
    z.to_sql('Aggr_Ins_Dist', con=sql_alchamey, if_exists='append', index=False)
x=Aggr_Ins_Dist_Table()

