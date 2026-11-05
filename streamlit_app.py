import streamlit as st
import duckdb
import pandas as pd
import matplotlib.pyplot as plt

#Page info
st.set_page_config(page_title = "greenHaus App", layout = "wide")

#Title Text
st.title("A Climate Visualizer")

#Cache data from duckdb
@st.cache_resource
def get_db_conn():
    return duckdb.connect("production.duckdb", read_only = False)

#Conntect to the database
conn = get_db_conn()

#database query for chart making data
query = "SELECT Date/Time, Mean Max Temp (°C) FROM production.duckdb ORDER BY Date/Time ASC;"
df = conn.execute(query).df()

#Construct the chart
fig, ax = plt.subplots(figsize = (8, 4))
ax.bar(df["Date/Time"], df["Mean Max Temp (°C)"], color = '#d4000e', edgecolor = 'black')