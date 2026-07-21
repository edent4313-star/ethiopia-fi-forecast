import streamlit as st
import os

# Set up the title
st.title("CBE FI Intelligence Dashboard")
    # Get the directory where app.py is located
base_path = os.path.dirname(__file__)
logo_path = os.path.join(base_path, "assets", "logo.png")

if os.path.exists(logo_path):
    st.image(logo_path, width=200)
else:
    st.warning(f"Logo not found at {logo_path}")

import streamlit as st

from config import APP_TITLE

from components.sidebar import sidebar


st.set_page_config(

    page_title=APP_TITLE,

    layout="wide",

    page_icon="📊"

)

sidebar()

st.title(

    APP_TITLE

)

st.markdown(

"""
Welcome to the Ethiopia Financial Inclusion Dashboard.

Use the navigation menu on the left to explore:

• Overview

• Trends

• Forecasts

• Inclusion Projections
"""
)

# 1. Define the correct path once at the top of your file
BASE_DIR = os.path.dirname(__file__)
LOGO_PATH = os.path.join(BASE_DIR, "assets", "logo.png")

# 2. Use the LOGO_PATH variable whenever you want to show the image
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=200)
else:
    st.error(f"Logo missing! Looked in: {LOGO_PATH}"

)