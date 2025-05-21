# 🌞 Streamlit App Module — Solar Potential Dashboard

This directory contains the core Streamlit application for visualizing and analyzing solar potential data from **Benin**, **Sierra Leone**, and **Togo**. The app provides interactive visualizations, key performance indicators (KPIs), and summary statistics to aid in identifying regions with high solar energy potential.

---

## 📄 Files Overview

### `main.py`
Main entry point of the Streamlit app.

**Key Features:**
- Sidebar for country and metric selection (`GHI`, `DNI`, `DHI`)
- Slider for filtering values within a desired solar metric range
- Boxplots of metric distributions by country
- KPI cards showing average metric values per country
- Annotated bar chart of average metric values
- Summary statistics table (mean, median, std)
- Refresh dashboard button to update visualizations only on demand

This script uses modules from both `app/utils.py` and `scripts/viz_utils.py`.

---

### `utils.py`
Helper module for handling data operations within the app.

**Functions:**
- `load_data()`  
  Loads and combines cleaned CSV datasets for the three countries from public Google Drive links.

- `filter_data(df, countries, metric, min_val, max_val)`  
  Filters the dataset based on selected countries and metric range.

- `calculate_kpis(filtered_df, metric)`  
  Computes average metric values by country for KPI display.

---

## 🔗 Data Sources
CSV datasets for Benin, Sierra Leone, and Togo are pulled from public Google Drive links (or local files during development).

---

## 📦 Dependencies
- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy`
