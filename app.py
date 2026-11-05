import streamlit as st
import duckdb as db
import pandas as pd
import matplotlib.pyplot as pl

st.set_page_config(page_title = "greenHaus App", layout = "wide")
st.title("A Climate Visualizer")

@st.cache_resource
def get_duckdb_conn(db_path = ":memory"):
    return duckdb.connect(db_path)