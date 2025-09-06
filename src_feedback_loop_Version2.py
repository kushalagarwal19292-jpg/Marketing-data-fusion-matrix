import streamlit as st
import pandas as pd

def add_new_datapoint(df):
    st.subheader("Add New Data Point")
    new_data = {}
    for col in df.columns:
        if col != 'marketing_performance':
            new_data[col] = st.number_input(f"{col.replace('_', ' ').title()}", float(df[col].min()), float(df[col].max()))
    # Optionally let the user input target or predict it with model
    if st.button("Add Data Point"):
        return pd.DataFrame([new_data])
    return None