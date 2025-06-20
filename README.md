# PRODIGY_DS_05

## 🚗 Task 05 – Traffic Accident Analysis: Full Dataset

### ✅ Objective:
Identify and visualize patterns in U.S. traffic accidents using the full updated dataset (~600 MB).

### 📁 Dataset:
- File: `US_Accidents_Dec21_updated.csv` (~600 MB)
- Columns analyzed: time, severity, weather, state, and geolocation

### 🔍 Analyses Performed:
1. Accidents by hour of day  
2. Top 10 weather conditions during accidents  
3. Severity distribution across top 10 states  
4. Geospatial hotspots via KDE heatmap

### 📊 Output Files:
- `accidents_by_hour.png`
- `accidents_by_weather.png`
- `severity_by_state.png`
- `accident_hotspots.png`

### 📌 Run Instructions:
```bash
pip install pandas matplotlib seaborn
python accident_analysis_full.py
