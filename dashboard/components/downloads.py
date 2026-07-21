import streamlit as st


def csv_download(

        df,

        filename,

        label

):

    st.download_button(

        label,

        df.to_csv(

            index=False

        ),

        filename,

        "text/csv"

    )