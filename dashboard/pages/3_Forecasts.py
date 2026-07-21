import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from utils import (
    load_event_data,
    load_forecast,
    load_importance,
    load_validation
)

st.set_page_config(
    page_title="Forecasts",
    layout="wide"
)

st.title("📈 Financial Inclusion Forecasts")

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

history = load_event_data()

forecast = load_forecast()

importance = load_importance()

validation = load_validation()

history = history[
    history["record_type"]=="observation"
].copy()

history = history[
    history["indicator_code"]=="ACC_OWNERSHIP"
]

history["year"] = pd.to_datetime(
    history["observation_date"]
).dt.year

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.header("Forecast Settings")

scenario = st.sidebar.selectbox(

    "Scenario",

    [

        "Base",

        "Optimistic",

        "Pessimistic"

    ]

)

model = st.sidebar.selectbox(

    "Forecast Model",

    [

        "Linear Regression"

    ]

)

# ----------------------------------------------------
# Forecast Selection
# ----------------------------------------------------

if scenario=="Base":

    prediction = forecast["base"]

elif scenario=="Optimistic":

    prediction = forecast["optimistic"]

else:

    prediction = forecast["pessimistic"]

# ----------------------------------------------------
# Historical + Forecast
# ----------------------------------------------------

st.subheader(

    "Historical and Forecast"

)

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=history["year"],

        y=history["value_numeric"],

        mode="lines+markers",

        name="Historical"

    )

)

fig.add_trace(

    go.Scatter(

        x=forecast["year"],

        y=prediction,

        mode="lines+markers",

        name=scenario

    )

)

upper = forecast["optimistic"]

lower = forecast["pessimistic"]

fig.add_trace(

    go.Scatter(

        x=list(forecast["year"])

        +

        list(forecast["year"])[::-1],

        y=list(upper)

        +

        list(lower)[::-1],

        fill="toself",

        fillcolor="rgba(0,100,80,0.2)",

        line=dict(color="rgba(255,255,255,0)"),

        name="Confidence Interval"

    )

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ----------------------------------------------------
# Forecast Table
# ----------------------------------------------------

st.subheader(

    "Forecast Values"

)

st.dataframe(

    forecast.round(2)

)

# ----------------------------------------------------
# Feature Importance
# ----------------------------------------------------

st.subheader(

    "Feature Importance"

)

fig2 = px.bar(

    importance,

    x="Coefficient",

    y="Feature",

    orientation="h",

    title="Linear Regression Coefficients"

)

st.plotly_chart(

    fig2,

    use_container_width=True

)

# ----------------------------------------------------
# Cross Validation
# ----------------------------------------------------

st.subheader(

    "Cross Validation"

)

fig3 = go.Figure()

fig3.add_trace(

    go.Scatter(

        y=validation["Actual"],

        mode="lines+markers",

        name="Actual"

    )

)

fig3.add_trace(

    go.Scatter(

        y=validation["Predicted"],

        mode="lines+markers",

        name="Predicted"

    )

)

st.plotly_chart(

    fig3,

    use_container_width=True

)

# ----------------------------------------------------
# Residuals
# ----------------------------------------------------

st.subheader(

    "Residual Analysis"

)

validation["Residual"]=(

validation["Actual"]

-

validation["Predicted"]

)

fig4=px.scatter(

validation,

x="Predicted",

y="Residual",

title="Residual Plot"

)

st.plotly_chart(

fig4,

use_container_width=True

)

# ----------------------------------------------------
# Key Milestones
# ----------------------------------------------------

st.subheader(

"Projected Milestones"

)

milestone=forecast.loc[

forecast["base"]>=60

]

if len(milestone)>0:

    year=int(

    milestone.iloc[0]["year"]

    )

    st.success(

    f"60% Financial Inclusion Target projected in {year}"

    )

else:

    st.warning(

    "60% target is not reached in current forecast horizon."

    )

# ----------------------------------------------------
# Downloads
# ----------------------------------------------------

st.subheader(

"Download Results"

)

st.download_button(

"Download Forecast",

forecast.to_csv(index=False),

"forecast.csv",

"text/csv"

)

st.download_button(

"Download Feature Importance",

importance.to_csv(index=False),

"feature_importance.csv",

"text/csv"

)

st.download_button(

"Download Validation Results",

validation.to_csv(index=False),

"validation.csv",

"text/csv"

)