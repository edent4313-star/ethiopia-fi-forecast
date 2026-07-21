import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils import load_forecast

st.set_page_config(
    page_title="Inclusion Projections",
    layout="wide"
)

st.title("🎯 Financial Inclusion Projections")

# ----------------------------------------------------
# Load Forecast
# ----------------------------------------------------

forecast = load_forecast()

TARGET = 60

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.header("Scenario")

scenario = st.sidebar.radio(

    "Select Scenario",

    [

        "Base",

        "Optimistic",

        "Pessimistic"

    ]

)

if scenario == "Base":

    values = forecast["base"]

elif scenario == "Optimistic":

    values = forecast["optimistic"]

else:

    values = forecast["pessimistic"]

forecast["selected"] = values

# ----------------------------------------------------
# KPI Cards
# ----------------------------------------------------

c1, c2, c3 = st.columns(3)

current = float(values.iloc[0])

target_gap = TARGET - current

milestone = forecast[
    forecast["selected"] >= TARGET
]

if len(milestone) > 0:

    target_year = int(milestone.iloc[0]["year"])

else:

    target_year = "Beyond Forecast"

with c1:

    st.metric(

        "Current Projection",

        f"{current:.1f}%"

    )

with c2:

    st.metric(

        "Remaining to Target",

        f"{target_gap:.1f}%"

    )

with c3:

    st.metric(

        "Target Achievement",

        target_year

    )

# ----------------------------------------------------
# Progress Gauge
# ----------------------------------------------------

st.subheader("Progress Toward 60% Target")

fig = go.Figure(

    go.Indicator(

        mode="gauge+number",

        value=current,

        title={

            "text":"Financial Inclusion (%)"

        },

        gauge={

            "axis":{"range":[0,100]},

            "threshold":{

                "line":{"color":"red","width":4},

                "value":TARGET

            }

        }

    )

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ----------------------------------------------------
# Forecast Trend
# ----------------------------------------------------

st.subheader("Projected Financial Inclusion")

trend = go.Figure()

trend.add_trace(

    go.Scatter(

        x=forecast["year"],

        y=values,

        mode="lines+markers",

        name=scenario

    )

)

trend.add_hline(

    y=TARGET,

    line_dash="dash",

    annotation_text="60% Target"

)

st.plotly_chart(

    trend,

    use_container_width=True

)

# ----------------------------------------------------
# Consortium Questions
# ----------------------------------------------------

st.header("Answers to Consortium Questions")

if len(milestone)>0:

    st.success(

        f"✔ Ethiopia is projected to achieve the 60% financial inclusion target in {target_year} under the {scenario.lower()} scenario."

    )

else:

    st.warning(

        "The 60% target is not achieved within the current forecast horizon."

    )

st.markdown("---")

st.subheader("Key Drivers")

st.markdown("""

- Expansion of digital financial services

- Mobile money adoption (Telebirr)

- Financial inclusion policies

- Infrastructure investment

- Agent banking

- Digital payment ecosystem

""")

st.subheader("Recommended Actions")

st.markdown("""

1. Continue expanding Telebirr services.

2. Increase ATM and agent banking coverage.

3. Promote person-to-person (P2P) digital payments.

4. Strengthen digital financial literacy.

5. Encourage partnerships between banks and fintech providers.

6. Continue financial inclusion policy reforms.

""")

# ----------------------------------------------------
# Download
# ----------------------------------------------------

st.subheader("Download")

st.download_button(

    "Download Projection",

    forecast.to_csv(index=False),

    "financial_inclusion_projection.csv",

    "text/csv"

)