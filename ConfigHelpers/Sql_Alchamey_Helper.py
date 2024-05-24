from sqlalchemy import create_engine


def Sql_Alchamey_Helper():
    engine = create_engine("mysql+mysqlconnector://root:Bethebest%4031@localhost/PhonePePulse")
    return engine
