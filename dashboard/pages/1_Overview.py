import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt # Moved to top

from utils import (
    load_event_data,
    load_forecast
)

from components.metrics import metric_card
from components.downloads import csv_download

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Overview",
    layout="wide"
)

st.title("📊 Overview")

# -------------------------
# Load Data
# -------------------------
data = load_event_data()
forecast = load_forecast()

# -------------------------
# Observations Only
# -------------------------
obs = data[data["record_type"] == "observation"].copy()

# -------------------------
# Account Ownership Data Prep
# -------------------------
ownership = obs[obs["indicator_code"] == "ACC_OWNERSHIP"].copy()
ownership["observation_date"] = pd.to_datetime(ownership["observation_date"])
ownership = ownership.sort_values("observation_date")

# Ensure 'year' column exists for the Matplotlib plot
if 'year' not in ownership.columns:
    ownership['year'] = ownership['observation_date'].dt.year

current_value = ownership.iloc[-1]["value_numeric"]
previous_value = ownership.iloc[-2]["value_numeric"]
growth = current_value - previous_value

# -------------------------
# Event Prep
# -------------------------
events = data[data["record_type"] == "event"].copy()
event_count = len(events)
forecast_year = forecast["year"].max()

# -------------------------
# KPI Cards
# -------------------------
c1, c2, c3, c4 = st.columns(4)
with c1:
    metric_card("Current Account Ownership", f"{current_value:.1f}%")
with c2:
    metric_card("Growth Since Previous Survey", f"{growth:.1f}%")
with c3:
    metric_card("Recorded Events", event_count)
with c4:
    metric_card("Forecast Available Until", forecast_year)

st.divider()

# -------------------------
# Progress to Target
# -------------------------
st.subheader("Progress Toward 60% Financial Inclusion Target")
progress = current_value / 60
st.progress(min(progress, 1.0))
st.write(f"Current Progress: {current_value:.1f}% of 60% target")

# -------------------------
# Ownership / Digital crossover Ratio
# -------------------------
st.subheader("Ownership / Digital crossover Ratio")
try:
    avg_ownership = ownership["value_numeric"].mean()
    avg_digital = obs[obs["indicator_code"] == "USG_ACTIVE_RATE"]["value_numeric"].mean()
    ratio = avg_ownership / avg_digital
    st.metric("Ownership / Digital Ratio", f"{ratio:.2f}")
except:
    st.info("Digital usage indicators are not available for ratio calculation.")

# -------------------------
# Plotly Historical Trend
# -------------------------
st.subheader("Historical Account Ownership (Plotly)")
fig = px.line(
    ownership,
    x="observation_date",
    y="value_numeric",
    markers=True,
    title="Account Ownership Trend"
)
st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Scenario-Based Forecast (Matplotlib)
# -------------------------
st.subheader("Complete Trend & Scenario Forecast")

# 1. Prepare historical trend
df_hist_trend = ownership.groupby('year')['value_numeric'].mean().reset_index()

# 2. Bridge the Gap (Connect to Forecast)
last_hist_point = df_hist_trend.iloc[-1]
bridge = pd.DataFrame({
    'year': [last_hist_point['year']],
    'base': [last_hist_point['value_numeric']],
    'optimistic': [last_hist_point['value_numeric']],
    'pessimistic': [last_hist_point['value_numeric']]
})
forecast_connected = pd.concat([bridge, forecast], ignore_index=True)

# 3. Create the Figure
fig_mpl, ax = plt.subplots(figsize=(12, 6)) 

# A. Historical Line
ax.plot(df_hist_trend['year'], df_hist_trend['value_numeric'], 
         color='black', linewidth=1.5, alpha=0.6, label='Historical Trend')

# B. Historical Dots
ax.scatter(ownership['year'], ownership['value_numeric'], 
            s=50, color='black', zorder=5, label='Observed Historical')

# C. Forecast Lines
ax.plot(forecast_connected['year'], forecast_connected['base'], 
         color='blue', linewidth=2.5, label='Base Forecast')
ax.plot(forecast_connected['year'], forecast_connected['optimistic'], 
         color='green', linestyle='--', linewidth=1.5, label='Optimistic Scenario')
ax.plot(forecast_connected['year'], forecast_connected['pessimistic'], 
         color='red', linestyle='--', linewidth=1.5, label='Pessimistic Scenario')

# D. Shading
ax.fill_between(forecast_connected['year'],
                 forecast_connected['pessimistic'],
                 forecast_connected['optimistic'],
                 alpha=0.1, color='gray', label='Scenario Range')

# E. Formatting
ax.axvline(x=last_hist_point['year'], color='gray', linestyle=':', alpha=0.7)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
ax.legend(loc='upper left', fontsize='small')
ax.grid(True, alpha=0.3)

# IMPORTANT: Use st.pyplot instead of plt.show()
st.pyplot(fig_mpl)

# -------------------------
# Event Categories
# -------------------------
st.subheader("Event Categories")
event_chart = px.histogram(
    events,
    x="category",
    color="category",
    title="Distribution of Events"
)
st.plotly_chart(event_chart, use_container_width=True)

# -------------------------
# Download Section
# -------------------------
st.subheader("Downloads")
csv_download(forecast, "forecast_2025_2027.csv", "Download Forecast")