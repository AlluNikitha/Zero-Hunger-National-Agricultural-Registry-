# 🌾 AgriPulse: Crop & Farmer Data Management System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.62%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![NumPy](https://img.shields.io/badge/NumPy-2.0%2B-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![SDG](https://img.shields.io/badge/UN%20SDG-2%3A%20Zero%20Hunger-DDA63A?logo=unitednations&logoColor=white)](https://sdgs.un.org/goals/goal2)

**AgriPulse** is an agricultural intelligence and data management web application built with **Streamlit, Pandas, and NumPy**. Designed in alignment with **United Nations Sustainable Development Goal 2 (Zero Hunger)**, the platform integrates smallholder farmer registries, agronomic crop intelligence, parametric yield modeling, and real-time APMC Mandi wholesale prices into a unified dashboard.

---

## 🌟 Key Features

### 1. ℹ️ Prominent About & UN SDG 2 Mission Hub
- Accessible via the **top navbar "ℹ️ About" button** (modal dialog) and the **first top navigation tab**.
- Detailed tracking of UN SDG 2 targets:
  - **Target 2.1**: Universal food access & post-harvest loss prevention.
  - **Target 2.3**: Smallholder agricultural productivity doubling.
  - **Target 2.4**: Sustainable farming & climate resilience tracking.
  - **Target 2.c**: Fair wholesale APMC Mandi market price discovery vs Government Minimum Support Price (MSP).

### 2. 👨‍🌾 Farmer Directory & Land Registry
- Search and filter across **251 registered farming operations** across 14 Indian states.
- Multi-criteria filtering by State, Primary Cultivated Crop, and Soil Type.
- Instant filtered CSV export.
- **Register New Farmer**: Real-time modal registration form with persistent updates to `data/farmer_data.csv`.

### 3. 🌱 Crop Explorer & Agronomic Match Recommender
- Complete agronomic profiles for **18 major Indian crops** across Cereals, Pulses, Cash Crops, Oilseeds, and Vegetables.
- Verified high-resolution cultivation photography.
- Agronomic specifications: MSP, Water Requirement, Optimal Soil, Season, Growth Duration, Ideal Temperature, and Rainfall.
- **NumPy Vectorized Soil-Crop Match Recommender**:
  - Encodes parcel soil type, water availability, and season into normalized vectors.
  - Computes weighted feature dot products to rank the top 3 recommended crops with compatibility percentages.

### 4. 📊 NumPy Statistical Yield Engine & Z-Score Benchmark
- Parametric statistical breakdown: Mean, Median, Std Dev ($\sigma$), Variance ($\sigma^2$), Range (Peak-to-Peak), Quartiles (P25, P75), P90/P95 elite benchmarks, and Coefficient of Variation (CV%).
- Dynamic **Gaussian normal distribution curve** fitted over harvest yield histograms:
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2\right)$$
- **Farmer Performance Z-Scores**:
  $$Z = \frac{Y_{\text{farm}} - \mu_{\text{crop}}}{\sigma_{\text{crop}}}$$
  Identifies and highlights farms operating $> 1\sigma$ below median ($Z < -1.0$) for prioritized agronomic intervention.

### 5. 🎲 NumPy Monte Carlo Harvest & Financial Risk Simulator
- Vectorized stochastic simulation running **1,000 synthetic harvest trials** using `np.random.normal` and `np.clip`.
- Factors in acreage, cultivation costs, and weather risk scenarios (Normal, Favorable Monsoon, Drought Stress, High Volatility).
- Computes Expected Median Profit, 5% Value-at-Risk (VaR), 95% Upside Target, Probability of Profitability, and Expected ROI %.

### 6. 💰 APMC Mandi & Inter-Mandi Arbitrage Tracker
- Daily modal wholesale prices compared directly against Government Minimum Support Price (MSP) benchmarks.
- Inter-Mandi Arbitrage Matrix computing Peak-to-Peak price spreads (`np.ptp`) and price standard deviations across mandis.

### 7. 🗺️ Agricultural GIS Belt Map
- Geospatial mapping rendered with Folium and OpenStreetMap tiles.
- Proportional cluster circles illustrating farmer concentration across 14 major agricultural states.

### 8. 📁 Raw Datasets Explorer & Exporter
- Interactive tabular inspection and one-click direct CSV downloads for all 4 relational datasets.

---

## 🎨 5 Curated Light Themes

The application includes 5 clean, high-contrast, modern **Light Themes** selectable from the top navbar:

| Theme | Primary Tone | Description |
|---|---|---|
| 🌿 **Fresh Emerald** *(Default)* | `#059669` | Clean Agro Light with mint and emerald accents |
| 🌾 **Golden Harvest** | `#d97706` | Sunlit Amber Light with warm ivory background |
| 🌊 **Nordic Breeze** | `#0284c7` | Oceanic Cyan Light with crisp sky blue palette |
| 🍃 **Sage & Olive** | `#15803d` | Botanical Earth Light with natural sage and olive tones |
| 🌸 **Lavender Bloom** | `#7c3aed` | Pastel Modern Light with royal amethyst highlights |

*(All dark themes have been removed for clean readability and neatness).*

---

## 📂 Project Structure

```
crop_managment_python/
├── .streamlit/
│   └── config.toml               # Native Streamlit light theme & server configuration
├── data/
│   ├── farmer_data.csv           # 251 Farmer demographics, landholdings, and soil profiles
│   ├── crop_data.csv             # 18 Crop varieties with agronomic requirements and MSP benchmarks
│   ├── production_data.csv       # 250 Historical harvest records with per-acre yields
│   ├── market_data.csv           # 249 APMC Mandi daily modal, min, and max wholesale price feeds
│   └── images/                   # High-resolution cultivation photos for all 18 crops (crop_C01 to crop_C18)
├── app.py                        # Main Streamlit application with reactive light theme engine
├── download_images.py            # Utility script for refreshing agricultural imagery
├── implementation_plan.md        # Technical architecture and implementation documentation
├── README.md                     # Comprehensive project documentation
└── requirements.txt              # Python production dependencies
```

---

## 🚀 Quickstart & Installation

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### 1. Clone or Navigate to Directory
```bash
cd c:/Studies/sem3/Python/crop_managment_python
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```

The application will start immediately and can be accessed at:
**http://localhost:8501**

---

## 📦 Backing Datasets

The platform is powered by 4 modular, interconnected datasets:
1. **`data/farmer_data.csv`** (251 records): `Farmer_ID`, `Name`, `Gender`, `Contact`, `State`, `District`, `Village`, `Land_Area_Acres`, `Soil_Type`, `Irrigation_Type`, `Primary_Crop`, `PM_Kisan_Beneficiary`.
2. **`data/crop_data.csv`** (18 records): `Crop_ID`, `Crop_Name`, `Category`, `Season`, `Water_Requirement`, `Optimal_Soil`, `Growth_Period_Days`, `MSP_Per_Quintal`, `Ideal_Temp_C`, `Ideal_Rainfall_MM`.
3. **`data/production_data.csv`** (250 records): `Production_ID`, `Farmer_ID`, `Crop_ID`, `Crop_Name`, `Year`, `Season`, `Cultivated_Area_Acres`, `Production_Tonnes`, `Yield_T_Per_Acre`, `Harvest_Loss_Percent`.
4. **`data/market_data.csv`** (249 records): `Market_ID`, `Mandi_Name`, `State`, `Crop_ID`, `Crop_Name`, `Modal_Price_Rs_Qtl`, `Min_Price_Rs_Qtl`, `Max_Price_Rs_Qtl`, `MSP_Rs_Qtl`, `Price_Trend`.

---

## 📜 License
Developed for academic and public agricultural intelligence research aligned with United Nations Sustainable Development Goals (SDG 2: Zero Hunger).
