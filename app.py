from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

csv_path = Path(__file__).parent / "climate_data" / "edmonton.csv"

#Page title and info
st.set_page_config(page_title="Edmonton Historical Weather Data", layout="wide")
st.title("Monthly Temperature Fluxuation")

#Get data from csv
@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin-1")                  #Encoding swap for degree symbol
    df = df.iloc[:, 1:4]                                        #Township uneeded for now
    df.columns = ["date", "temperature", "precip"]              #Column names
    df["date"] = pd.to_datetime(df["date"], format="%Y")        #Match date format to csv dates
    return df.sort_values("date").reset_index(drop=True)        #Return sorted by date, oldest to newest (does this need to happen? All csvs from gov are sorted)

#Confirm csv file exists in path
if not csv_path.exists():
    st.error(f"CSV not found: '{csv_path}'")    #Error printout
    st.stop()                                   #Stopping point

#Load csv file
df = load_data(csv_path)

#Trendline checkbox
show_trend1 = st.checkbox("Decade Trend", True)


#Chart creation
fig1, ax1 = plt.subplots(figsize=(8,5))
ax1.plot(
    df["date"],
    df["temperature"],
    color="tab:red",
    linewidth=0.8,
    label="Yearly Average"
)

#Decade Trend Line, Temperature
if show_trend1:
    ax1.plot(
        df["date"],
        df["temperature"].rolling(10,center=True).mean(),
        color = (0,0,0),
        linewidth=1,
        label="10 Year Trend"
    )

#Temperature chart formatting
ax1.axhline(0, color="gray", linewidth=0.8, linestyle="--")
ax1.set_xlim(df["date"].min(), df["date"].max())
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title(f"Average Yearly Temperature: {df["date"].min():%Y} - {df["date"].max():%Y}")  #Wildcard for variable dates
ax1.legend(loc="upper left")
fig1.tight_layout(pad=3)

st.pyplot(fig1)
plt.close(fig1)

#Precip trend line
show_trend2 = st.checkbox("Trendline", True)

#Precipitation chart
fig2, ax2 = plt.subplots(figsize=(8,5))
ax2.plot(
    df["date"],
    df["precip"],
    color="tab:blue",
    linewidth=0.8,
    label="Yearly Average"
)

#Decade Trend Line, Precip
if show_trend2:
    ax2.plot(
        df["date"],
        df["precip"].rolling(10,center=True).mean(),
        color = (0,0,0),
        linewidth=1,
        label="10 Year Trend"
    )

#Precip chart formatting
ax2.axhline(0, color="gray", linewidth=0.8, linestyle="--")
ax2.set_xlim(df["date"].min(), df["date"].max())
ax2.set_xlabel("Year")
ax2.set_ylabel("Precipitation (mm)")
ax2.set_title(f"Average Annual Precipitation: {df["date"].min():%Y} - {df["date"].max():%Y}")  #Wildcard for variable dates
ax2.legend(loc="upper right")
fig2.tight_layout(pad=3)

st.pyplot(fig2)
plt.close(fig2)