import streamlit as st
import pandas as pd

from src.data_generator import generate_7ps_data
from src.fusion_engine import FusionEngine
from src.ui_components import sidebar_filters, kpi_card
from src.feedback_loop import add_new_datapoint

st.set_page_config(page_title="Marketing Data Fusion Matrix", layout="wide")

# Load or generate data
try:
    df = pd.read_csv("data/synthetic_7ps_dataset.csv")
except FileNotFoundError:
    df = generate_7ps_data()
    df.to_csv("data/synthetic_7ps_dataset.csv", index=False)

engine = FusionEngine(df)

st.title("📊 Marketing Data Fusion Matrix (MDFM)")
st.markdown("""
    <span style="font-size:18px;color:#667;">A portfolio-grade analytics engine that turns the Marketing Mix (7Ps) into live business intelligence.</span>
""", unsafe_allow_html=True)

# Sidebar filters
filters = sidebar_filters(df)
filtered_df = df.copy()
for col, (min_val, max_val) in filters.items():
    filtered_df = filtered_df[(filtered_df[col] >= min_val) & (filtered_df[col] <= max_val)]

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Data Ingestion", "Fusion Engine", "Simulation", "Execution", "Reports"])

with tab1:
    st.header("Synthetic Data Overview")
    st.dataframe(filtered_df.head(20))
    st.download_button("Download CSV", filtered_df.to_csv(index=False), "filtered_7ps.csv")

with tab2:
    st.header("Correlate: Feature Importances")
    coefs = engine.correlate()
    st.bar_chart(coefs)
    st.write("Top drivers for marketing performance:")
    for feat, coef in coefs.head(3).items():
        kpi_card(feat.replace('_', ' ').title(), coef, "📈")

with tab3:
    st.header("Simulate: What-if Scenario")
    feature = st.selectbox("Select Feature", [c for c in df.columns if c != 'marketing_performance'])
    new_value = st.slider("New Value", float(df[feature].min()), float(df[feature].max()), float(df[feature].mean()))
    pred = engine.simulate(feature, new_value)
    st.write(f"If `{feature}` is set to `{new_value:.2f}`, predicted marketing performance is: **{pred:.2f}**")
    kpi_card("Simulated Performance", pred, "🎯")

with tab4:
    st.header("Prescribe: Recommended Actions")
    actions = engine.prescribe()
    for feat, action in actions.items():
        st.markdown(f"- {action}")

with tab5:
    st.header("Continuous Learning Feedback Loop")
    new_df = add_new_datapoint(df)
    if new_df is not None:
        df_updated = pd.concat([df, new_df], ignore_index=True)
        engine.retrain(df_updated)
        st.success("Model retrained with new data point!")
        st.write("Updated model R2 score:", engine.score)

st.markdown("---")
st.markdown("""
### 📚 Marketing Mix 7Ps as Data Sensors
> Each P is a live sensor feeding business intelligence.<br>
> Use the tabs to explore, simulate, and prescribe actions.<br>
> Export your insights for presentations or strategy sessions.
""", unsafe_allow_html=True)