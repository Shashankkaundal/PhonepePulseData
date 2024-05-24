import seaborn

from DB_Config.DBconnect import db_connect
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def query1():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query1 = """(  select transaction_count,year from Aggr_Tran_State where
                    transaction_type='Recharge & bill payments'  group by year,transaction_count
                        )"""
    cursorObject.execute(query1)
    #creating the bar plot
    #x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["Transaction Amount(in Crores)","Year" ])
    #print(df)
    groupedvalues = df.groupby('Year').sum().reset_index()
    #groupedvalues["Transaction Count(in Millions)"].map(lambda y: "{:,.1f}".format(y / 10000000.))
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Transaction Amount(in Crores)'] = groupedvalues['Transaction Amount(in Crores)'] / 10000000
    groupedvalues.sort_values(by='Transaction Amount(in Crores)', ascending=False, inplace=True)
    #print(groupedvalues)
    #flights_wide = flights.pivot(index="year", columns="month", values="passengers")
    #sns.barplot(flights_wide)
    # who v/s fare barplot
    #groupedvalues['Transaction Count(in Millions)'] = [f'${Transaction Count(in Millions) / 10000000:.1f}cr' for value in bars.datavalues])
    #plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:.1f} Million".format(x / 1000000)))
    sns.barplot(data=groupedvalues,x='Year', y='Transaction Amount(in Crores)',palette="muted",hue="Year",errorbar="sd")
    #ax.locator_params(integer=True)
    return plt

def query2():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query2 = """(select sum(percentage),brand from Aggr_User_State group by brand,percentage
                        )"""
    cursorObject.execute(query2)
    df = pd.DataFrame(cursorObject.fetchall(), columns=["Percentage","Brand"])
    groupedvalues = df.groupby(['Brand']).sum().reset_index()
    palette_color = seaborn.color_palette('bright')
    # plotting data on chart
    plt.pie(groupedvalues['Percentage'], labels=groupedvalues['Brand'], autopct='%1.1f%%')

    #plt.show()
    return plt
def query3():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query3 = """(select sum(transaction_amount),year from Aggr_Ins_State group by transaction_amount,year
                            )"""
    cursorObject.execute(query3)
    df = pd.DataFrame(cursorObject.fetchall(), columns=["Transaction_Amount(in Crs)", "Year"])
    groupedvalues = df.groupby(['Year']).sum().reset_index()
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Transaction_Amount(in Crs)'] = groupedvalues['Transaction_Amount(in Crs)'] / 10000000
    # plotting data on chart
    #print(groupedvalues)
    #plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:.1f}Cr".format(x / 10000000)))
    ax=sns.lineplot(data=groupedvalues, x="Year", y="Transaction_Amount(in Crs)")
    ax.locator_params(integer=True)
    return plt
def query4():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query4 = """(select state,sum(transaction_amount) from Aggr_Tran_Dist  
    where year=2023 group by state,transaction_amount order by 
                transaction_amount )"""
    cursorObject.execute(query4)
    # creating the bar plot
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["State","Transaction Amount(in Crores)"])
    df.replace('-', '')
    #print(df)
    groupedvalues = df.groupby(['State']).sum().reset_index()
    groupedvalues.sort_values(by='Transaction Amount(in Crores)', ascending=False,inplace = True)
    groupedvalues.State = groupedvalues.State.str.title()
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Transaction Amount(in Crores)'] = groupedvalues['Transaction Amount(in Crores)'] / 1000000000
    # plotting data on chart
    print(groupedvalues)
    #plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda y, loc: "{:.1f} Million".format(y / 1000000)))
    sns.barplot(data=groupedvalues.head(10), x="Transaction Amount(in Crores)",
                y="State", errorbar=("pi", 95),palette="pastel",hue="State",legend=False)
    #ax.locator_params(integer=True)
    return plt


def query5():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query5 = """(select brand,sum(count),year from Aggr_User_State group by brand,count,year)"""
    cursorObject.execute(query5)
    # creating the bar plot
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["Brand", "Registered Users By The Brand(in Crs)","Year"])
   # df.replace('-', '')
    groupedvalues = df.groupby(['Brand','Year']).sum().reset_index()
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Registered Users By The Brand(in Crs)'] = groupedvalues['Registered Users By The Brand(in Crs)'] / 10000000
    # plotting data on chart
    #print(groupedvalues)
    plt.figure(figsize=(9, 7))
    ax=sns.lineplot(data=groupedvalues, x="Year", y="Registered Users By The Brand(in Crs)", hue="Brand", style="Brand")
    ax.locator_params(integer=True)
    return plt

def query6():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query6 = """(select state,sum(count) from Aggr_User_Dist group by state,count)"""
    cursorObject.execute(query6)
    # creating the bar plot
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["State", "Registered Users Count By State(in Crs)"])
    # df.replace('-', '')
    groupedvalues = df.groupby(['State']).sum().reset_index()
    groupedvalues.sort_values(by='Registered Users Count By State(in Crs)', ascending=False, inplace=True)
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Registered Users Count By State(in Crs)'] = groupedvalues['Registered Users Count By State(in Crs)'] / 10000000
    groupedvalues.State = groupedvalues.State.str.title()
    # plotting data on chart
    #print(groupedvalues)
    plt.figure(figsize=(12, 12))
    sns.catplot(data=groupedvalues.head(10), x="Registered Users Count By State(in Crs)",
                y="State", errorbar=("pi", 95), kind="bar", palette="pastel", hue="State", legend=False)
    #ax.locator_params(integer=True)
    return plt
def query7():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query7 = """(select state,sum(count) from Aggr_User_Dist group by state,count)"""
    cursorObject.execute(query7)
    # creating the bar plot
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["State", "Registered Users Count By State(in Crs)"])
    groupedvalues = df.groupby(['State']).sum().reset_index()
    groupedvalues.State = groupedvalues.State.str.title()
    # plotting data on chart
    # print(groupedvalues)
    plt.figure(figsize=(12, 20))
    groupedvalues.sort_values(by='Registered Users Count By State(in Crs)', ascending=True, inplace=True)
    groupedvalues.State = groupedvalues.State.str.title()
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Registered Users Count By State(in Crs)'] = groupedvalues['Registered Users Count By State(in Crs)'] / 10000000
    # plotting data on chart
    #print(groupedvalues)
    sns.catplot(data=groupedvalues.head(10), x="Registered Users Count By State(in Crs)",
                y="State", palette="pastel",kind='bar', hue="State", legend=False,height=8.27, aspect=11.7/8.27)
    #ax.locator_params(integer=True)
    return plt

def query8():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query8 = """(select state,sum(transaction_amount) from Aggr_Tran_Dist  
    where year=2023 group by state,transaction_amount order by 
                transaction_amount )"""
    cursorObject.execute(query8)
    # creating the bar plot
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["State","Transaction Amt(in Crs)"])
    df.replace('-', '')
    groupedvalues = df.groupby(['State']).sum().reset_index()
    groupedvalues.sort_values(by='Transaction Amt(in Crs)', ascending=True,inplace = True)
    groupedvalues.State = groupedvalues.State.str.title()
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Transaction Amt(in Crs)'] = groupedvalues['Transaction Amt(in Crs)'] / 10000000
    plt.figure(figsize=(40, 40))
    sns.catplot(data=groupedvalues.head(10), x="Transaction Amt(in Crs)",
                y="State", errorbar=("pi", 95), kind="bar",palette="pastel",hue="State",legend=False)
    #ax.locator_params(integer=True)
    return plt

def query9():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query9 = """(select sum(TRANSACTION_COUNT),year from Aggr_Ins_State group by TRANSACTION_COUNT,year
                            )"""
    cursorObject.execute(query9)
    df = pd.DataFrame(cursorObject.fetchall(), columns=["Transaction_Count(in Crs)", "Year"])
    #print(df)
    groupedvalues = df.groupby(['Year']).sum().reset_index()
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Transaction_Count(in Crs)'] = groupedvalues['Transaction_Count(in Crs)'] / 10000000
    # plotting data on chart
    #print(groupedvalues)
   # plt.figure(figsize=(10, 12))
    #plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:.1f} Million".format(x / 1000000)))
    ax=sns.lineplot(data=groupedvalues, x="Year", y="Transaction_Count(in Crs)")
    ax.locator_params(integer=True)
    return plt

def query10():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE PhonePePulse""")
    query10 = """(select state,sum(transaction_count) from Aggr_Ins_Dist group by state,transaction_count
                                )"""
    cursorObject.execute(query10)
    df = pd.DataFrame(cursorObject.fetchall(), columns=["State","Insurance_Count(in Crs)"])
    groupedvalues = df.groupby(['State']).sum().reset_index()
    groupedvalues.sort_values(by='Insurance_Count(in Crs)', ascending=False, inplace=True)
    groupedvalues.State = groupedvalues.State.str.title()
    pd.options.display.float_format = 'Rs{:,.2f}Cr'.format
    groupedvalues['Insurance_Count(in Crs)'] = groupedvalues['Insurance_Count(in Crs)'] / 10000000
    plt.figure(figsize=(10, 12))
    sns.catplot(data=groupedvalues.head(10), x="Insurance_Count(in Crs)",
                y="State", errorbar=("pi", 95), kind="bar", palette="pastel", hue="State", legend=False)
    # ax.locator_params(integer=True)
    return plt

#x=query10()
#print(x)
