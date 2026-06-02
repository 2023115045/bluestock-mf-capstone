import requests
import pandas as pd
import os

# Dictionary of schemes
schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Save location
save_path = "data/raw"

# Create folder if not exists
os.makedirs(save_path, exist_ok=True)

# Fetch NAV data
for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"\nFetching data for {name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        # Convert NAV history to DataFrame
        nav_data = data.get("data", [])

        df = pd.DataFrame(nav_data)

        # Save CSV
        file_name = f"{name}_nav.csv"

        df.to_csv(os.path.join(save_path, file_name), index=False)

        print(f"{file_name} saved successfully")

    else:
        print(f"Failed to fetch {name}")