import requests
import json

# Fetch the official UK bank holidays
r = requests.get("https://www.gov.uk/bank-holidays.json")
r.raise_for_status()
all_data = r.json()

# Write out the full, original JSON (all regions, all dates)
with open("bank-holidays.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2)
