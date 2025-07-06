import requests
import json

# Fetch the official UK bank holidays
r = requests.get("https://www.gov.uk/bank-holidays.json")
r.raise_for_status()
all_data = r.json()

# Filter just England and Wales (edit as needed)
events = all_data['england-and-wales']['events']

# Only keep *future* holidays
from datetime import datetime
now = datetime.utcnow().isoformat()
future_events = [e for e in events if e['date'] >= now[:10]]

# Write out a simple, clean JSON
with open("bank-holidays.json", "w", encoding="utf-8") as f:
    json.dump(future_events, f, indent=2)
