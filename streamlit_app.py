import streamlit as st
import duckdb
import pandas as pd
import matplotlib.pyplot as plt

#file paths
DB_PATH = "./data/climate_data.duckdb"
CSV_PATH = "./RawData/edmonton_raw.csv"
TABLE_NAME = "climate_records"

#columns to extract from csv

#Page info
st.set_page_config(page_title = "greenHaus App", layout = "wide")

#Title Text
st.title("A Climate Visualizer")

#database file path
db_path = "./data/climate_data.duckdb"

#connect to the database
conn = duckdb.connect(database=db_path, read_only=False)