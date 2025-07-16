import requests
import pandas as pd
from datetime import datetime
from dateutil import parser, tz

start_time = datetime(2025, 7, 13, 19, 30, 0, tzinfo=tz.UTC)  # Time limit, 2 hours differences between UTC and Munich
end_time = datetime(2025, 7, 13, 20, 30, 0, tzinfo=tz.UTC)

API_URL = "https://gi3.gis.lrg.tum.de/log/all?dev_eui=eq.00876EA598282BF6"  # Use url based on DevEUI
# 0009296F1A9F134F  SWM 1
# 00876EA598282BF6  SWM 2
# 8765182202E81E1E  TTN 1
# 8765182202E81E02  TTN 2

response = requests.get(API_URL)
if response.status_code != 200:
    raise Exception(f"Failed to get: {response.status_code}")

data = response.json()

filtered = []
for entry in data:
    ts = parser.isoparse(entry["ts"])  
    if start_time <= ts <= end_time:
        filtered.append({
            "ts": ts.isoformat(),
            "dev_eui": entry.get("dev_eui"),
            "network": entry.get("network"),
            "snr": entry.get("snr"),
            "rssi": entry.get("rssi"),
            "spreading_factor": entry.get("spreading_factor"),
            "bandwidth": entry.get("bandwidth"),
            "gateway_eui": entry.get("gateway_eui"),
            "lat": entry.get("lat"),
            "lon": entry.get("lon"),
        })

df = pd.DataFrame(filtered)
df.sort_values(by="ts", inplace=True)


output_file = "lorawan_data_20250713_swm07_Olympia.xlsx"
df.to_excel(output_file, index=False)

print(f"In total {len(df)} data are saved into {output_file}")

