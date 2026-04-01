import pandas as pd
import numpy as np

# --- MISSION: Transitioning Excel Research to Python Automation ---

def process_ice_telemetry(file_path):
    """
    Automating the cleaning and trend analysis of NASA GRACE-FO records.
    """
    # 1. DATA INGESTION
    # Replacing manual Excel imports with automated Pandas ingestion
    df = pd.read_csv(file_path)

    # 2. DATA INTEGRITY (The 'Cleaning' Step)
    # Removing null pings from the satellite sensor stream
    df_clean = df.dropna(subset=['ice_mass_gt'])

    # 3. ANOMALY DETECTION
    # Identifying 'noisy' data points that deviate from the mean
    # This ensures our backend reports are accurate and reliable
    threshold = df_clean['ice_mass_gt'].std() * 3
    df_no_noise = df_clean[df_clean['ice_mass_gt'].diff().abs() <= threshold]

    # 4. PREDICTIVE LOGIC (The 'Trendline' Step)
    # Calculating the annual melt rate using linear regression
    years = np.array(range(len(df_no_noise)))
    slope, intercept = np.polyfit(years, df_no_noise['ice_mass_gt'], 1)
    
    print(f"Pipeline executed. Detected melt rate: {slope:.2f} Gt/year.")
    return df_no_noise

# Note: File path placeholder for GitHub demonstration
# process_ice_telemetry('nasa_telemetry_data.csv')
