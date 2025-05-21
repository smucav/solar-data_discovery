import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal
import numpy as np

def load_and_combine_data(benin_path: str, sierra_leone_path: str, togo_path: str) -> pd.DataFrame:
    """
    Load CSV data for three countries, add 'Country' column, and combine into a single DataFrame.

    Args:
        benin_path (str): File path for Benin data CSV.
        sierra_leone_path (str): File path for Sierra Leone data CSV.
        togo_path (str): File path for Togo data CSV.

    Returns:
        pd.DataFrame: Combined data with country labels.
    """
    benin = pd.read_csv(benin_path)
    sierra_leone = pd.read_csv(sierra_leone_path)
    togo = pd.read_csv(togo_path)
    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    return pd.concat([benin, sierra_leone, togo], ignore_index=True)

def plot_metric_boxplots(df: pd.DataFrame, metrics: list, save_path: str) -> None:
    """
    Generate and save boxplots for given metrics grouped by country.

    Args:
        df (pd.DataFrame): Data containing metrics and 'Country' column.
        metrics (list): List of metric column names to plot.
        save_path (str): File path to save the figure.

    Returns:
        None
    """
    fig, axes = plt.subplots(1, len(metrics), figsize=(6, 3))
    for i, metric in enumerate(metrics):
        sns.boxplot(x='Country', y=metric, data=df, ax=axes[i])
        axes[i].set_title(f'{metric} Distribution')
        axes[i].set_xlabel('Country')
        axes[i].set_ylabel(f'{metric} (W/m²)')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def create_summary_table(df: pd.DataFrame, metrics: list) -> pd.DataFrame:
    """
    Compute summary statistics (mean, median, std) for specified metrics by country.

    Args:
        df (pd.DataFrame): Data containing metrics and 'Country' column.
        metrics (list): List of metric column names to summarize.

    Returns:
        pd.DataFrame: Summary statistics table with countries as rows.
    """
    summary = []
    for country in df['Country'].unique():
        country_data = df[df['Country'] == country]
        stats = {'Country': country}
        for metric in metrics:
            stats[f'{metric}_Mean'] = country_data[metric].mean()
            stats[f'{metric}_Median'] = country_data[metric].median()
            stats[f'{metric}_Std'] = country_data[metric].std()
        summary.append(stats)
    return pd.DataFrame(summary)

def run_kruskal_wallis(df: pd.DataFrame, metric: str) -> tuple:
    """
    Perform Kruskal-Wallis H-test to compare distributions of a metric across countries.

    Args:
        df (pd.DataFrame): Data containing metric and 'Country' column.
        metric (str): Metric column name to test.

    Returns:
        tuple: Test statistic and p-value.
    """
    groups = [df[df['Country'] == country][metric].dropna() for country in df['Country'].unique()]
    stat, p_value = kruskal(*groups)
    return stat, p_value

def plot_metric_means_bar(df: pd.DataFrame, metric: str, ax) -> None:
    """
    Plot a horizontal bar chart of mean metric values by country, with values displayed on bars.

    Args:
        df (pd.DataFrame): Data containing metric and 'Country' column.
        metric (str): Metric column name to plot.
        ax (matplotlib.axes.Axes): Matplotlib axis to draw the plot on.

    Returns:
        None
    """
    means = df.groupby("Country")[metric].mean().sort_values(ascending=False)
    sns.barplot(x=means.values, y=means.index, ax=ax)
    for i, v in enumerate(means.values):
        ax.text(v + 1, i, f"{v:.2f}", color='black', va='center')
    ax.set_title(f"Average {metric} by Country")
    ax.set_xlabel(f"{metric} (W/m²)")
    ax.set_ylabel("")
