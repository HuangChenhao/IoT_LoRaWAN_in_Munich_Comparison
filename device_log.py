import requests
import pandas as pd


url = "https://gi3.gis.lrg.tum.de/log/all?dev_eui=eq.8765182202E81E1E"    # TTN
# url = "https://gi3.gis.lrg.tum.de/log/all?dev_eui=eq.0009296F1A9F134F"  # SWM

response = requests.get(url)
if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    exit()

data = response.json()

records = []
for item in data:
    decoded = item.get("decoded_payload", {})
    records.append({
        "network": item.get("network"),
        "temperature_1": decoded.get("temperature_1"),
        "relative_humidity_2": decoded.get("relative_humidity_2"),
        "spreading_factor": item.get("spreading_factor"),
        "snr": item.get("snr"),
        "rssi": item.get("rssi"),
        "lat": item.get("lat"),

        
        "lon": item.get("lon"),
        "timestamp": item.get("ts")
    })

df = pd.DataFrame(records)

output_file = "TTN_device_log.xlsx"
# output_file = "SWM_device_log.xlsx"
df.to_excel(output_file, index=False)
print(f"Data saved {output_file}")
