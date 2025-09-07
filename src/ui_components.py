import streamlit as st

def sidebar_filters(df):
    st.sidebar.header("7Ps Filters")
    filters = {}
    for col in df.columns:
        if col != 'marketing_performance':
            min_val, max_val = float(df[col].min()), float(df[col].max())
            filters[col] = st.sidebar.slider(col.replace('_', ' ').title(), min_val, max_val, (min_val, max_val))
    return filters

def kpi_card(label, value, icon):
    st.markdown(
        f"""
        <div style="background:#f9fafd;border-radius:12px;padding:18px;margin-bottom:12px;box-shadow:0 2px 6px #eee;">
            <span style="font-size:32px;vertical-align:middle;margin-right:12px;">{icon}</span>
            <span style="font-size:20px;font-weight:600;">{label}:</span>
            <span style="font-size:28px;color:#1a6fd3;font-weight:700;margin-left:8px;">{value:.2f}</span>
        </div>
        """, unsafe_allow_html=True
    )