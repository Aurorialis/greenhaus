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
show_trend = st.checkbox("Trendline", True)


#Chart creation
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(
    df["date"],
    df["temperature"],
    color="tab:red",
    linewidth=0.6,
    label="Yearly Average"
)

if show_trend:
    ax.plot(
        df["date"],
        df["temperature"].rolling(10,center=True).mean(),
        color = (0,0,0),
        linewidth=0.8,
        label="Decadal Trend"
    )

#Chart formatting
ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
ax.set_xlim(df["date"].min(), df["date"].max())
ax.set_xlabel("Year")
ax.set_ylabel("Temperature")
ax.set_title(f"Average Yearly Temperature: {df["date"].min():%Y} - {df["date"].max():%Y}")  #Wildcard for variable dates
ax.legend(loc="upper left")
fig.tight_layout(pad=3)

st.pyplot(fig)
plt.close(fig)