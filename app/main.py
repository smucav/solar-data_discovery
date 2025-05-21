"""
Main Streamlit app for the Solar Potential Dashboard.

Loads solar data, allows users to filter by country and solar metrics,
and displays interactive visualizations and KPIs.

Features:
- Sidebar controls for country selection, metric choice, and value range filtering.
- Boxplot showing metric distribution by country.
- KPI table and metric cards showing average values by country.
- Bar chart visualization of average metrics with values annotated.
- Summary statistics table for selected metric.

Updates dashboard only when the "Update Dashboard" button is clicked.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_data, filter_data, calculate_kpis
from scripts.viz_utils import create_summary_table, plot_metric_means_bar

st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")
st.title("Solar Potential Dashboard")

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Filters")
    countries = st.multiselect("Select Countries", options=['Benin', 'Sierra Leone', 'Togo'], default=['Benin', 'Sierra Leone', 'Togo'])
    metric = st.selectbox("📊 Select Metric", ['GHI', 'DNI', 'DHI'])
    min_val, max_val = st.slider(f"{metric} Range (W/m²)", 50.0, 300.0, (75.0, 250.0))
    update = st.button("Update Dashboard")

# Load and filter data
df = load_data()
filtered_df = filter_data(df, countries, metric, min_val, max_val)

# Show dashboard after update
if update:
    st.subheader(f"📊 {metric} Distribution by Country")
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.boxplot(x='Country', y=metric, data=filtered_df, ax=ax)
    ax.set_ylabel(f"{metric} (W/m²)")
    st.pyplot(fig)

    st.subheader(f"📌 Average {metric} by Country")
    kpi_df = calculate_kpis(filtered_df, metric)
    st.dataframe(kpi_df, use_container_width=True)


    cols = st.columns(len(kpi_df))
    for i, row in kpi_df.iterrows():
        with cols[i]:
            st.metric(label=row['Country'], value=f"{row[metric]:.2f} W/m²")

    # Enhanced bar chart
    st.subheader(f"📊 Bar Chart of Average {metric}")
    fig, ax = plt.subplots(figsize=(8, 4))
    plot_metric_means_bar(filtered_df, metric, ax)
    st.pyplot(fig)

    # Summary stats
    st.subheader("📋 Summary Statistics")
    summary_df = create_summary_table(filtered_df, metrics=[metric])
    st.dataframe(summary_df, use_container_width=True)

    # After all existing code in if update: block

    # Generate summary stats for selected metric
    summary_stats = create_summary_table(filtered_df, metrics=[metric])

    # Extract key stats as dict for easy access
    stats_dict = summary_stats.set_index('Country').to_dict(orient='index')

    # Logic to find key observations
    highest_avg_country = summary_stats.loc[summary_stats[f'{metric}_Mean'].idxmax()]['Country']
    lowest_median_country = summary_stats.loc[summary_stats[f'{metric}_Median'].idxmin()]['Country']
    highest_std_country = summary_stats.loc[summary_stats[f'{metric}_Std'].idxmax()]['Country']

    # Compose summary markdown string
    summary_md = f"""
    ### 🔍 Key Observations

    🌍 **{highest_avg_country}** has the highest average {metric}, indicating strong solar potential.

    🌩️ **{lowest_median_country}** shows the lowest median {metric} values, suggesting inconsistencies or lower availability.

    ⚡ **{highest_std_country}** has the highest variability in {metric}, indicating unstable solar conditions.
    """

    st.markdown(summary_md)


    st.success("Dashboard updated!")
else:
    st.info("Use the sidebar to filter and click 'Update Dashboard'")
