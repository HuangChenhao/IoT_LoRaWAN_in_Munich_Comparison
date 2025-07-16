import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta, timezone
# from backports.zoneinfo import ZoneInfo   # for Python 3.8, if higher version, use the codes of the following line
from zoneinfo import ZoneInfo   # import Zoneinfo for python version higher than 3.9
import time

# set Timezone as local time
local_tz = ZoneInfo("Europe/Berlin")

URL = "https://gi3.gis.lrg.tum.de/log/all"
POLL_INTERVAL = 30
SAMPLE_INTERVAL = 20
LAT_TOL = 1.0001
LON_TOL = 1.0001

# Input DevEUIs and set their names and colors

# TTN DevEUIs
DEVICES = {
    "8765182202E81E1E": "TTN1-SF12",
    "8765182202E81E02": "TTN2-SF07"
}
# SWM DevEUIs
# DEVICES = {
#     "0009296F1A9F134F": "SWM1-SF12",
#     "00876EA598282BF6": "SWM2-SF07"
# }

# Helium DevEUIs
# DEVICES = {
#     "xxxxxxxxxxxxxxxx": "Helium1-SF12",
#     "xxxxxxxxxxxxxxxx": "Helium2-SF07"
# }


DEVICE_COLORS = {
    "8765182202E81E1E": "skyblue",  # TTN-SF12
    "8765182202E81E02": "orange"    # TTN-SF07
    # "0009296F1A9F134F": "skyblue",  # SWM-SF12
    # "00876EA598282BF6": "orange"    # SWM-SF07
}



REFERENCE_COORDS = {}
all_data_dict = {dev_eui: pd.DataFrame() for dev_eui in DEVICES.keys()}

plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

def fetch_data():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return []

def filter_data(data):
    filtered_dict = {dev_eui: [] for dev_eui in DEVICES.keys()}
    today_local = datetime.now(local_tz).date()

    for item in data:
        dev_eui = item.get("dev_eui")
        if dev_eui not in DEVICES:
            continue

        ts_str = item.get("ts", "")
        try:
            ts_dt_utc = pd.to_datetime(ts_str, utc=True)
            ts_dt_local = ts_dt_utc.astimezone(local_tz)
        except Exception as e:
            print(f"Invalid timestamp: {ts_str}, error: {e}")
            continue

        if ts_dt_local.date() != today_local:
            continue

        lat = item.get("lat")
        lon = item.get("lon")
        if lat is None or lon is None:
            continue

        if dev_eui not in REFERENCE_COORDS:
            REFERENCE_COORDS[dev_eui] = (lat, lon)

        ref_lat, ref_lon = REFERENCE_COORDS[dev_eui]
        if abs(lat - ref_lat) > LAT_TOL or abs(lon - ref_lon) > LON_TOL:
            continue

        filtered_dict[dev_eui].append({
            "dev_eui": dev_eui,
            "timestamp": ts_dt_utc,
            "timestamp_local": ts_dt_local,
            "snr": item.get("snr"),
            "rssi": item.get("rssi"),
            "temperature": item.get("temperature_1"),
            "relative_humidity": item.get("relative_humidity_2")
        })

    return filtered_dict

def update_plot(all_data_dict, success_dict):
    ax[0].clear()
    ax[1].clear()

    for dev_eui in DEVICES.keys():
        df = all_data_dict[dev_eui]
        if df.empty:
            continue

        df_sorted = df.sort_values("timestamp_local")
        label = DEVICES[dev_eui]
        color = DEVICE_COLORS.get(dev_eui, "gray")

        ax[0].plot(df_sorted["timestamp_local"], df_sorted["snr"], marker='o', label=label, color=color)
        ax[1].plot(df_sorted["timestamp_local"], df_sorted["rssi"], marker='o', label=label, color=color)

    ax[0].set_title("SNR over time (Local time)")
    ax[0].set_ylabel("SNR (dB)")
    ax[0].legend()

    ax[1].set_title("RSSI over time (Local time)")
    ax[1].set_ylabel("RSSI (dBm)")
    ax[1].legend()

    time_format = mdates.DateFormatter('%H:%M:%S', tz=local_tz)
    ax[0].xaxis.set_major_formatter(time_format)
    ax[1].xaxis.set_major_formatter(time_format)

    summary = "\n".join([
        f"{DEVICES[dev]} Successful Rate Overall: {success_dict[dev]['overall']:.2%}, 5min: {success_dict[dev]['recent']:.2%}"
        for dev in DEVICES.keys()
    ])
    fig.suptitle(f"TTN LoRaWAN Connection\n{summary}", fontsize=14)
    # fig.suptitle(f"SWM LoRaWAN Connection\n{summary}", fontsize=14)
    # fig.suptitle(f"Helium LoRaWAN Connection\n{summary}", fontsize=14)
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

while True:
    data = fetch_data()
    records_dict = filter_data(data)

    for dev_eui in DEVICES.keys():
        records = records_dict.get(dev_eui, [])
        if records:
            df_new = pd.DataFrame(records)
            all_data_dict[dev_eui] = pd.concat([all_data_dict[dev_eui], df_new]).drop_duplicates(subset=["timestamp"])

    success_dict = {}

    for dev_eui in DEVICES.keys():
        df = all_data_dict[dev_eui]
        if df.empty:
            continue

        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

        # Overall successful rate
        start_ts_overall = df["timestamp"].min()
        latest_ts = df["timestamp"].max()
        elapsed_overall = (latest_ts - start_ts_overall).total_seconds()
        expected_overall = elapsed_overall / SAMPLE_INTERVAL
        actual_overall = len(df)
        success_overall = actual_overall / expected_overall if expected_overall > 0 else 0

        # 5 minutes' successful rate
        start_ts_recent = datetime.now(timezone.utc) - timedelta(minutes=5)
        df_recent = df[df["timestamp"] >= start_ts_recent]
        if not df_recent.empty:
            latest_recent_ts = df_recent["timestamp"].max()
            elapsed_recent = (latest_recent_ts - start_ts_recent).total_seconds()
            expected_recent = elapsed_recent / SAMPLE_INTERVAL
            actual_recent = len(df_recent)
            success_recent = actual_recent / expected_recent if expected_recent > 0 else 0
        else:
            success_recent = 0

        print(f"[{DEVICES[dev_eui]}] Overall: {success_overall:.2%}, 5min: {success_recent:.2%}")
        print(f"Latest packet UTC: {latest_ts}, Local: {latest_ts.astimezone(local_tz)}")

        success_dict[dev_eui] = {"overall": success_overall, "recent": success_recent}

    update_plot(all_data_dict, success_dict)
    time.sleep(POLL_INTERVAL)
