import requests
import pandas as pd

base_url = "https://gi3.gis.lrg.tum.de/frost/v1.1/Things(529)/Datastreams(1440)/Observations?$orderby=%40iot.id+asc"

results = []
times = []

url = base_url
while url:
    print(f"Fetching: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break

    data = response.json()
    for obs in data.get("value", []):
        results.append(obs.get("result"))
        times.append(obs.get("phenomenonTime"))

    url = data.get("@iot.nextLink")


df = pd.DataFrame({
    "phenomenonTime": times,
    "result": results
})

#  Save as Excel
output_file = "observations.xlsx"
df.to_excel(output_file, index=False)
print(f"Saved to {output_file}")
