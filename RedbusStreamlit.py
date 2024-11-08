import pandas as pd
import pymysql
import streamlit as st
from streamlit_option_menu import option_menu
import time

#KERALA BUS
lists_k=[]
df_k=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfk.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#ANDHRA BUS
lists_A=[]
df_A=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfA.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#TELUNGANA BUS
lists_T=[]
df_T=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfT.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#SOUTHBENGAL BUS
lists_SB=[]
df_SB=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfSB.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

#RAJASTHAN BUS
lists_R=[]
df_R=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfR.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])

#GOA BUS
lists_G=[]
df_G=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfG.csv")
for i,r in df_G.iterrows():
    lists_G.append(r["Route_name"])

#PUNJAB BUS
lists_P=[]
df_P=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfP.csv")
for i,r in df_P.iterrows():
    lists_P.append(r["Route_name"])

#UTTAR PRADESH
lists_UP=[]
df_UP=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfUP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#ASSAM BUS
lists_AS=[]
df_AS=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfAS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#HARYANA BUS
lists_H=[]
df_H=pd.read_csv(r"H:\\streamlit_session\myenv\redbus routes csv file\dfH.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#SETTING UP STREAMLIT PAGE
st.set_page_config(layout="wide")

web=option_menu(menu_title="OnlineBus",
                options=["Home","States and Routes"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )


#HOME PAGE SETTING
if web=="Home":
    st.image("https://i.pinimg.com/564x/58/91/2b/58912b2e3ad6a279347eebb47751a9c1.jpg",width=200)
    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    st.subheader(":blue[Domain:] Transportation")
    st.subheader(":blue[Objective] ")
    st.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution")
    st.subheader(":blue[Overview:]")
    st.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites")
    st.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from csv format into a Structured dataframe.
                   Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    st.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                   and the data was efficiently inserted into the relevant tables for storage and retrievel.''')
    st.markdown("Streamlit: Developed an Interactive web application using streamlit, a user-friendly framework for data visualization and analysis.")
    st.subheader(":blue[Skill take:]")
    st.markdown("Selenium,Python, Pandas, MySQL,mysql-connector-python,Streamlit.")
    st.subheader(":blue[Developed-by:] Sridhara krishnan")

#States and Routes page setting
if web=="States and Routes":
    S=st.selectbox("Lists of States",["Kerala","Andhra Pradesh","Telungana","South Bengal","Rajasthan","Goa","Punjab","Uttar Pradesh","Assam","Haryana"])
    select_fare=st.radio("choose bus fare range",("50-1000","1000-2000","2000 and above"))

    #KERALA BUS FARE FILTERING
    if S=="Kerala":
        K=st.selectbox("list of routes",lists_k)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{K}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{K}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{K}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    #ANDHRA PRADESH BUS FARE FILTERING
    if S=="Andhra Pradesh":
        A=st.selectbox("list of routes",lists_A)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{A}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{A}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{A}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    #TELUNGANA BUS FARE FILTERING
    if S=="Telungana":
        T=st.selectbox("list of routes",lists_T)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{T}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{T}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{T}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    #SOUTH BENGAL BUS FARE FILTERING
    if S=="South Bengal":
        SB=st.selectbox("list of routes",lists_SB)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{SB}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{SB}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{SB}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    #RAJASTHAN BUS FARE FILTERING
    if S=="Rajasthan":
        R=st.selectbox("list of routes",lists_R)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{R}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{R}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{R}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    #GOA BUS FARE FILTERING
    if S=="Goa":
        G=st.selectbox("list of routes",lists_G)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{G}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{G}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{G}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    
    #PUNJAB BUS FARE FILTERING
    if S=="Punjab":
        P=st.selectbox("list of routes",lists_P)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{P}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{P}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{P}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    #UTTAR PRADESH BUS FARE FILTERING
    if S=="Uttar Pradesh":
        UP=st.selectbox("list of routes",lists_UP)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{UP}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{UP}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{UP}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)


    #ASSAM BUS FARE FILTERING
    if S=="Assam":
        AS=st.selectbox("list of routes",lists_AS)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{AS}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{AS}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{AS}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)



    #HARYANA BUS FARE FILTERING
    if S=="Haryana":
        H=st.selectbox("list of routes",lists_H)
        
        if select_fare == "50-1000":
            fare_min=50
            fare_max=1000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{H}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "1000-2000":
            fare_min=1000
            fare_max=2000
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price BETWEEN {fare_min} AND {fare_max} and Route_name='{H}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)

        if select_fare == "2000 and above":
            mydb = pymysql.connect(host="localhost", user="root", password="",database="redbus_details")
            mycursor = mydb.cursor()
            query=f'''Select * from bus_details 
                            where Price > 2000 and Route_name='{H}'
                            order by Price desc'''
            mycursor.execute(query)
            out = mycursor.fetchall()
            df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",  
                                            "Total_duration", "Price", "Seats_Available", "Ratings", 
                                            "Route_link", "Route_name"])
            st.write(df)





        

            
        
            

            
        










