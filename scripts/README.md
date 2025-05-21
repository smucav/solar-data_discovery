# 📂 scripts/

This directory contains Python utility scripts used for data processing, visualization, and statistical analysis in the solar energy potential discovery project.

## 📄 Files

### `viz_utils.py`

This module provides reusable functions for:
- Loading and combining solar data from multiple countries
- Creating visual summaries and statistical comparisons of solar metrics
- Saving publication-ready visualizations

#### Functions:

##### `load_and_combine_data(benin_path, sierra_leone_path, togo_path) -> pd.DataFrame`
Loads cleaned CSV files for Benin, Sierra Leone, and Togo, adds a 'Country' column, and returns a combined DataFrame.

---

##### `plot_metric_boxplots(df, metrics, save_path)`
Generates boxplots for the specified list of metric columns across countries and saves the figure to the given path.

---

##### `create_summary_table(df, metrics) -> pd.DataFrame`
Computes and returns a summary table with mean, median, and standard deviation for each metric by country.

---

##### `run_kruskal_wallis(df, metric) -> (statistic, p_value)`
Performs the Kruskal-Wallis H-test to check for statistically significant differences in a given metric across countries.

---

##### `plot_metric_means_bar(df, metric, ax)`
Creates a horizontal bar plot of the mean value of a metric for each country, with values displayed on the bars. Intended to be embedded in a matplotlib subplot.

---

##### `plot_ghi_ranking(df, save_path)`
Generates a bar chart showing the average Global Horizontal Irradiance (GHI) by country and saves it to the specified file path.

---

## 📦 `__init__.py`
Marks this directory as a Python package.

---

## ⚠️ Notes
- This module assumes pre-cleaned input CSV files with consistent column naming.
- Visualizations use Matplotlib and Seaborn; make sure these libraries are installed.
- Designed for use in both local and Streamlit-based environments.
