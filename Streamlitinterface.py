import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit as st
import mpld3
import streamlit.components.v1 as components
from Geo_Visualisation.Geo_Visual_Map_India import geo_visual_func
from Geo_Visualisation.Geo_Visual_Map_District import geo_visual_func_district
from Geo_Visualisation.Geo_Visual_Map_Ins_India import geo_visual_ins_func
from Geo_Visualisation.Geo_Visual_Map_Ins_District import geo_visual_func_ins_district
from DBCreation.DB_Tables.Aggregated_User_Table.Aggr_User_Dist_Table import Aggr_User_Dist_Table
from DBCreation.DB_Tables.Aggregated_User_Table.Agg_User_India_Table import Aggr_User_India_Table
from DBCreation.DB_Tables.Aggregated_Insurance_Tables.Aggr_Ins_Dist_Table import Aggr_Ins_Dist_Table
from DBCreation.DB_Tables.Aggregated_Insurance_Tables.Aggr_Ins_India_Table import Aggr_Ins_India_Table
from DBCreation.DB_Tables.Aggregated_Transaction_Tables.Aggr_Tran_Dist_Table import Aggr_Tran_Dist_Table
from DBCreation.DB_Tables.Aggregated_Transaction_Tables.Aggr_Tran_India_Table import Aggr_Tran_India_Table
from Insight_Queries.DB_Queries import query1
from Insight_Queries.DB_Queries import query2
from Insight_Queries.DB_Queries import query3
from Insight_Queries.DB_Queries import query4
from Insight_Queries.DB_Queries import query5
from Insight_Queries.DB_Queries import query6
from Insight_Queries.DB_Queries import query7
from Insight_Queries.DB_Queries import query8
from Insight_Queries.DB_Queries import query9
from Insight_Queries.DB_Queries import query10
def HomePage():
    import streamlit as st
    st.write("# Welcome to Phonepe Pulse Data Visualization 👋")
    st.sidebar.success("Select an option above.")
    st.markdown(
        """
        Project Problem Objective:
        
        #The problem statement is to create a Streamlit application that allows users to geo-visualise and analyze data from PhonePe Pulse. 
        
        The Project has below functionalities:
        
        #Ability to Geo Visualise the payments and insurance data from 2018-2024 in States and Districts.
        
        #Ability to analyse the data from different trends and patterns across the years using various plots
        
        #Please refer below link for more details about phone pe pulse.
        
        https://www.phonepe.com/pulse/
    """
    )

def GeoVisualisation():
    import streamlit as st
    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    _LOREM_IPSUM = """
        Here You can see the Payments & Insurance Data in Every State based on year
        """
    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.01)
    st.write_stream(stream_data)
    #time.sleep(0.05)
    left_column, right_column = st.columns([1, 1])
    option1 = right_column.selectbox(
        label='Choose Data Source', options=("Choose an option", "Insurance", "Payments"))
    option2 = left_column.selectbox(
        label='Choose a year',options=("Choose an option","2018","2019","2020","2021","2022","2023","2024"))
    if (option2 == '2018' and option1=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_func(2018)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2019' and option1=="Payments" ):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig=geo_visual_func(2019)
        st.plotly_chart(fig,theme="streamlit",use_container_width=True)
        my_bar.empty()
    if (option2 == '2020' and option1=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_func(2020)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2021' and option1=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_func(2021)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2022' and option1=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_func(2022)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2023' and option1=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_func(2023)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2024' and option1=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_func(2024)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()

    ##########################

    if (option2 == '2018' and option1=="Insurance"):
        _LOREM_IPSUM = """
                Insurance Data for States is available from 2020 onwards.
                """

        def stream_data():
            for word in _LOREM_IPSUM.split(" "):
                yield word + " "
                time.sleep(0.05)

        st.write_stream(stream_data)
    if (option2 == '2019' and option1=="Insurance"):
        _LOREM_IPSUM = """
                        Insurance Data for States is available from 2020 onwards.
                        """

        def stream_data():
            for word in _LOREM_IPSUM.split(" "):
                yield word + " "
                time.sleep(0.05)

        st.write_stream(stream_data)
    if (option2 == '2020' and option1=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_ins_func(2020)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2021' and option1=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_ins_func(2021)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2022' and option1=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_ins_func(2022)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2023' and option1=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_ins_func(2023)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option2 == '2024' and option1=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        fig = geo_visual_ins_func(2024)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()


def GeoVisualisationDistrict():
    import streamlit as st
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    _LOREM_IPSUM = """
            Here You can see the Payments & Insurance Data in Every District based on year
            """

    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.01)

    st.write_stream(stream_data)
    # time.sleep(0.05)
    left_column, right_column = st.columns([1, 1])
    option1 = left_column.selectbox(
        label='Choose a year', options=("Choose an option","2018", "2019", "2020", "2021", "2022", "2023", "2024"))
    option2 = right_column.selectbox(
        label='Choose Data Source', options=("Choose an option", "Payments", "Insurance"))
    if (option1 == '2018' and option2=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_district(2018)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2019' and option2=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_district(2019)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2020' and option2=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_district(2020)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2021'and option2=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_district(2021)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2022' and option2=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_district(2022)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2023' and option2=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_district(2023)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2024' and option2=="Payments"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_district(2024)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    #####################
    if (option1 == '2018' and option2=="Insurance"):
        _LOREM_IPSUM = """
                        Insurance Data for Districts is available from 2020 onwards.
                        """

        def stream_data():
         for word in _LOREM_IPSUM.split(" "):
                yield word + " "
                time.sleep(0.05)

        st.write_stream(stream_data)
    if (option1 == '2019' and option2=="Insurance"):
        _LOREM_IPSUM = """
                            Insurance Data for Districts is available from 2020 onwards.
                            """

        def stream_data():
            for word in _LOREM_IPSUM.split(" "):
                yield word + " "
                time.sleep(0.05)

        st.write_stream(stream_data)
    if (option1 == '2020' and option2=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_ins_district(2020)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2021'and option2=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_ins_district(2021)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2022' and option2=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_ins_district(2022)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2023' and option2=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_ins_district(2023)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()
    if (option1 == '2024' and option2=="Insurance"):
        progress_text = "Geo Visualisation is in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        fig = geo_visual_func_ins_district(2024)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        my_bar.empty()


def Insights():
    import streamlit as st
    st.markdown(f'# {list(page_names_to_funcs.keys())[3]}')
    _LOREM_IPSUM = """
                              Here you can choose which insights you want.
                               """

    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.05)

    st.write_stream(stream_data)
    inr = st.button("Insert Data in DB to view insights")
    if(inr==True):
        progress_text = "I am inserting Data in DB. Please be patient."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            call_aggr_user_dist = Aggr_User_Dist_Table()
            call_aggr_user_dist = Aggr_User_India_Table()
            call_aggr_ins_dist = Aggr_Ins_Dist_Table()
            call_aggr_ins_state = Aggr_Ins_India_Table()
            call_aggr_trans_dist = Aggr_Tran_Dist_Table()
            call_aggr_trans_state = Aggr_Tran_India_Table()
            my_bar.progress(percent_complete + 1, text=progress_text)
        #time.sleep(1)
        my_bar.empty()
    option = st.selectbox(
        label='Select a query?',
        options=("---------Chose a Query----------------",
                 "1. What is the trend of total transactions amount across years for Recharge & bill payments in country?",
                 "2. What is the percentage share of different brands in country used for transaction from 2018 onwards?",
                 "3. What is the amount spent on insurance over the years?",
                 "4. Which are the top 10 states having highest transaction spend in year 2023?",
                 "5. What is the trend of registered users by brand across the years?",
                 "6. What are the top 10 States having highest registered users counts?",
                 "7. What are the top 10 States having lowest registered users counts?",
                 "8. Which are the top 10 states having least transaction spend in year 2023?",
                 "9. What is the trend of total no of insurance's done across the years?",
                 "10. What are the top 10 states with most no. of insurance's done across the years?")
    )
    if (option == "1. What is the trend of total transactions amount across years for Recharge & bill payments in country?"):
        x = query1()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif ( option == "2. What is the percentage share of different brands in country used for transaction from 2018 onwards?"):
        x = query2()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif ( option == "3. What is the amount spent on insurance over the years?"):
        x = query3()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif (option=="4. Which are the top 10 states having highest transaction spend in year 2023?"):
        x = query4()
        st.pyplot(x)
    elif(option=="5. What is the trend of registered users by brand across the years?"):
        x = query5()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif (option == "6. What are the top 10 States having highest registered users counts?"):
        x = query6()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif (option == "7. What are the top 10 States having lowest registered users counts?"):
        x = query7()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif (option == "8. Which are the top 10 states having least transaction spend in year 2023?"):
        x = query8()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif(option=="9. What is the trend of total no of insurance's done across the years?"):
        x = query9()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif (option == "10. What are the top 10 states with most no. of insurance's done across the years?"):
        x = query10()
        st.pyplot(x)
        st.write("*2024 data is available only for 1st Quater")
    elif (option == "---------Chose a Query----------------"):
        st.write("Kindly click on Insert into DB button first before selecting query")

page_names_to_funcs = {
    "Home": HomePage,
    "Geo Visualisation States": GeoVisualisation,
    "Geo Visualisation Districts":GeoVisualisationDistrict,
    "Insights": Insights
}
demo_name = st.sidebar.selectbox("Choose an option", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()