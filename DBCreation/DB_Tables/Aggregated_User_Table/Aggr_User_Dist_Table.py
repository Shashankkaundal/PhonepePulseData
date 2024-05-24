import MySQLdb
import mysql
import sqlalchemy
from sqlalchemy import create_engine
from ConfigHelpers.Sql_Alchamey_Helper import Sql_Alchamey_Helper
from DB_Config.DBconnect import db_connect
from PhonePeDataExtract.Data_Extractions.Aggregated_Data_Extracts.Aggregated_User_Data_Extract.Aggregated_State_User_Data_Extract import Aggr_State_User_Func
def Aggr_User_Dist_Table():
    configfile=db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""CREATE DATABASE IF NOT EXISTS PhonePePulse""")
    cursorObject.execute("""USE PhonePePulse""")
   # cursorObject.execute(aggr_tran_india)
    aggr_tan="""CREATE TABLE IF NOT EXISTS Aggr_User_Dist (
                            STATE VARCHAR(255),
                            YEAR YEAR(4),
                            QUATER INT,
                            BRAND VARCHAR(255),
                            COUNT bigint,
                            PERCENTAGE decimal(5,2)
                            )"""
    cursorObject.execute(aggr_tan)
    z = Aggr_State_User_Func()
    sql_alchamey=Sql_Alchamey_Helper()
    # Step 3: Convert the Pandas DataFrame to a format for MySQL table insertion
    z.to_sql('Aggr_User_Dist', con=sql_alchamey, if_exists='append', index=False)
x=Aggr_User_Dist_Table()

