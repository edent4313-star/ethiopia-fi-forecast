import os
import pandas as pd
from pathlib import Path
import streamlit as st

# 1. SET UP THE PATHS (The "Source of Truth")
# This automatically finds the project root regardless of where you run it.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"

# 2. THE REUSABLE LOADER (The "Recurrent" part)
@st.cache_data # This makes the dashboard load much faster!
def _safe_load(filename):
    """A private helper to handle paths and errors for any file."""
    file_path = DATA_DIR / filename
    
    if not file_path.exists():
        st.error(f"File not found: {filename}")
        # Return an empty dataframe so the UI doesn't crash
        return pd.DataFrame()
    
    return pd.read_csv(file_path)

# 3. SPECIFIC DATA LOADERS (Calling the recurrent helper)

def load_event_data():
    """This was the one causing the ImportError earlier."""
    return _safe_load("event_model_dataset.csv")

def load_forecast():
    return _safe_load("forecast_2025_2027.csv")

def load_importance():
    return _safe_load("feature_importance.csv")

def load_validation():
    return _safe_load("cross_validation_results.csv")
