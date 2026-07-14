"""
Bluestock Mutual Fund Analytics

File: live_nav_fetch.py

Purpose:
Fetch latest NAV data for mutual fund schemes
and update the local database.

Author: Nitan Sharma
"""
import requests
import pandas as pd

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

nav_data = data["data"]

df = pd.DataFrame(nav_data)

output_file = "data/raw/hdfc_top100_nav.csv"

df.to_csv(output_file, index=False)

print("NAV data saved successfully!")
