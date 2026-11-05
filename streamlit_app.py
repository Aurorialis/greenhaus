import streamlit as st
import duckdb
import pandas as pd
import matplotlib.pyplot as plt

#file paths
DB_PATH = "./data/climate_data.duckdb"
CSV_PATH = "./RawData/edmonton_raw.csv"
TABLE_NAME = "climate_records"

#Page info
st.set_page_config(page_title = "greenHaus App", layout = "wide")

#Title Text
st.title("A Climate Visualizer")

#database file path
db_path = "./data/climate_data.duckdb"

def load_data_to_db():
    #Connect to db, write access needed currently (change later?)
    conn = duckdb.connect(database=db_path, read_only=False)

    try:
        #Query if everything goes right
        query = f"""
        CREATE OR REPLACE TABLE edmonton_climate AS
        SELECT
            "Date/Time" AS record_date,
            "Mean Temp" AS mean_temp
        FROM read_csv_auto('{CSV_PATH}');
        """
        #Execute query on csv
        conn.execute(query)
        st.success("Table created and populated")

    #If query fails
    except Exception as e:
        st.error(f"Extraction Failed: {e}")

    #close the connection
    finally:
        conn.close()

load_data_to_db()