# Solar data discovery

This repository contains the work of analyzing solar farm data from Benin, Sierra Leone, and Togo.

## 🔧 Setup Instructions

```bash
git clone https://github.com/smucav/solar-data_discovery.git
cd solar-data_discovery
python -m venv .venv

# Activate the virtual environment
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

## 📁 Project Structure
solar-data_discovery/
├── notebooks/           # EDA notebooks for each country
├── app/                 # Streamlit dashboard code
├── data/                # Local storage for CSVs (not committed to Git)
├── .github/workflows/   # CI/CD pipeline configuration
├── scripts/             # Utility scripts
├── src/                 # Source code
└── tests/               # Test files
