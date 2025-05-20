# Solar data discovery

This repository contains work for analyzing solar farm data from **Benin**, **Sierra Leone**, and **Togo** to support **MoonLight Energy** in identifying high-potential regions for solar installations.

## 🚀 Contributions & Implementation

### ✅ Task 1: Git & Environment Setup

**Objective:** Establish a reproducible development environment with Git and CI/CD.

**Implementation:**

- Initialized GitHub repo: [solar-data_discovery](https://github.com/smucav/solar-data_discovery)
- Created modular folder structure:
  - `app/`, `notebooks/`, `scripts/`, `src/`, `tests/`

- Configured `.gitignore` to exclude:
  - `data/`, raw `.csv` files, and `.venv/`

- Set up `requirements.txt` with dependencies:
  - e.g., `pandas==2.2.3`, `streamlit==1.45.1`, `windrose`, etc.

- Implemented CI workflow:
  - `.github/workflows/ci.yml` using Python 3.12.3

- Documented setup in `README.md`
- Merged `setup-task` branch into `main` via Pull Request with multiple commits

**Outcome:** A robust, reproducible environment with automated CI checks.

---

### 📊 Task 2: Data Profiling, Cleaning & EDA

**Objective:** Clean and analyze solar datasets to uncover trends in GHI, DNI, DHI, and related variables.

**Implementation:**
- Created branches:
  - `eda-benin`, `eda-sierra_leone`, `eda-togo`
- Developed Jupyter notebooks:
  - `notebooks/benin_eda.ipynb`, `sierra_leone_eda.ipynb`, `togo_eda.ipynb`

#### 🧹 Cleaning:
- Imputed missing values (e.g., `GHI`, `DNI`, `DHI`) using **median**
- Removed outliers using **Z-score** method (> 3)
- Saved cleaned CSVs:
  - e.g., `data/benin_clean.csv`

#### 📈 EDA:
- **Time Series Analysis:** Diurnal and seasonal trends for:
  - GHI, DNI, DHI, Tamb
- **Correlation Heatmaps:** Relationships like `GHI vs TModA`
- **Wind Rose Plots:** Visualizing wind direction vs. speed (`windrose`)
- **Bubble Charts:** Multivariable analysis (e.g., `GHI vs Tamb`, bubble sized by `RH`)
- Saved plots in:
  - `notebooks/figures/` (e.g., `benin_timeseries.png`)

- Merged all EDA branches into `main` with CI passing

**Key Findings:**
- **Benin:** High GHI in dry season (Nov–Mar); strong GHI-TModA correlation
- **Sierra Leone:** Consistent GHI; humidity moderates solar radiation
- **Togo:** GHI more variable; cleaning improves ModA/ModB values

**Outcome:** Clean datasets with actionable insights into solar energy potential across regions.

## Cross-Country Comparison (Task 3)
- Synthesized cleaned datasets in `notebooks/compare_countries.ipynb`
- Visualizations:
  - Side-by-side boxplots for GHI, DNI, DHI across Benin, Sierra Leone, Togo
  - Bar chart ranking countries by average GHI
- Summary table: Mean, median, standard deviation for GHI, DNI, DHI
- Statistical testing: Kruskal-Wallis test on GHI (p-value reported)
- Key observations: Highlighted differences in solar potential
- Modular functions in `scripts/viz_utils.py` with docstrings
- Outputs saved in `notebooks/figures/` and `notebooks/figures/summary_table.csv`

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/smucav/solar-data_discovery.git

# Navigate into the project directory
cd solar-data_discovery

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# For Linux/Mac:
source .venv/bin/activate

# For Windows:
.venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```
## 📁 Project Structure
```
solar-data_discovery/
├── notebooks/         # Jupyter notebooks (EDA & visualizations)
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── figures/
├── app/               # Streamlit dashboard code
│   ├── main.py
│   └── utils.py
├── data/              # Raw and cleaned CSVs (local, not committed)
├── .github/
│   └── workflows/
│       └── ci.yml     # CI/CD pipeline config
├── scripts/           # Utility scripts
├── src/               # Core processing logic
├── tests/             # Unit and integration tests
└── requirements.txt   # Project dependencies
```
## 🧪 Running the Analysis

Open notebooks:
```
jupyter notebook notebooks/
```
View visualizations:
   - Located in notebooks/figures/
