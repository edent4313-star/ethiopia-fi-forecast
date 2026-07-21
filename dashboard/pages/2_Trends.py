import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_event_data

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(

    page_title="Trends",

    layout="wide"

)

st.title("📈 Financial Inclusion Trends")

# ------------------------------------------------
# Load Data
# ------------------------------------------------

data = load_event_data()

obs = data[
    data["record_type"] == "observation"
].copy()

obs["observation_date"] = pd.to_datetime(
    obs["observation_date"]
)

# ------------------------------------------------
# Sidebar Filters
# ------------------------------------------------

st.sidebar.header("Filters")

start = obs["observation_date"].min()

end = obs["observation_date"].max()

date_range = st.sidebar.date_input(

    "Select Date Range",

    value=(start, end)

)

if len(date_range) == 2:

    start_date, end_date = date_range

    obs = obs[

        (obs["observation_date"] >= pd.Timestamp(start_date))

        &

        (obs["observation_date"] <= pd.Timestamp(end_date))

    ]

# ------------------------------------------------
# Indicator Selection
# ------------------------------------------------

indicator = st.selectbox(

    "Choose Indicator",

    sorted(

        obs["indicator"].dropna().unique()

    )

)

selected = obs[
    obs["indicator"] == indicator
]

# ------------------------------------------------
# Interactive Trend
# ------------------------------------------------

fig = px.line(

    selected,

    x="observation_date",

    y="value_numeric",

    markers=True,

    color="gender",

    title=f"{indicator} Trend"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ------------------------------------------------
# Channel Comparison
# ------------------------------------------------

st.subheader("Channel Comparison")

channels = [

    "Account Ownership Rate",

    "ATM Access",

    "Telebirr Users",

    "P2P Transactions"

]

comparison = obs[

    obs["indicator"].isin(channels)

]

fig2 = px.line(

    comparison,

    x="observation_date",

    y="value_numeric",

    color="indicator",

    markers=True,

    title="Comparison Across Financial Channels"

)

st.plotly_chart(

    fig2,

    use_container_width=True

)

# ------------------------------------------------
# Summary Table
# ------------------------------------------------

st.subheader("Filtered Dataset")

st.dataframe(

    selected.sort_values(

        "observation_date"

    )

)

# ------------------------------------------------
# Download
# ------------------------------------------------

st.download_button(

    "Download Filtered Data",

    selected.to_csv(

        index=False

    ),

    file_name="filtered_indicator.csv",

    mime="text/csv"

)