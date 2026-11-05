import streamlit as st
import duckdb
import pandas as pd
import matplotlib.pyplot as plt

#Page info
st.set_page_config(page_title = "greenHaus App", layout = "wide")

#Title Text
st.title("A Climate Visualizer")

#Cache data from duckdb
@st.cache_data
def load_data():
    conn = duckdb.connect("data/production.duckdb", read_only = True)

    #Grab the columns from the table we want
    query = """SELECT "Date/Time", "Mean Max Temp (°C)" FROM s1865 ORDER BY "Date/Time" ASC;"""
    df = conn.execute(query).df()
    conn.close()
    return df

#Grab the dataframe
df = load_data()

#Construct the chart
fig, ax = plt.subplots(figsize = (8, 4))
ax.bar(df["Date/Time"], df["Mean Max Temp (°C)"], color = '#d4000e', edgecolor = 'black')

#Render the chart
st.pyplot(fig)