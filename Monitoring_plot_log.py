# This Python script continuously fetches LoRaWAN log data from the TUM GIS server every 30 seconds. 
# It filters records for a specific device and location, and plots SNR and RSSI over time using Berlin local time. 
# The script also calculates and displays the overall and recent 5-minute success rates, 
# showing how many packets were successfully received compared to the expected number based on a 20-second sampling interval.

import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

local_tz = ZoneInfo("Europe/Berlin")

import time

URL = "https://gi3.gis.lrg.tum.de/log/all"
# DEV_EUI = "0009296F1A9F134F"
# DEV_EUI = "8765182202E81E1E"
DEV_EUI = "8765182202E81E02"
LAT_TOL = 1.0001
LON_TOL = 1.0001
POLL_INTERVAL = 30
REFERENCE_LAT = None
REFERENCE_LON = None

SAMPLE_INTERVAL = 20

plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
all_data = pd.DataFrame()

def fetch_data():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return []

def filter_data(data):
    filtered = []
    today_local = datetime.now(local_tz).date()
    global REFERENCE_LAT, REFERENCE_LON
    
    for item in data:
        if item.get("dev_eui") != DEV_EUI:
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
        
        if REFERENCE_LAT is None:
            REFERENCE_LAT = lat
            REFERENCE_LON = lon
        
        if abs(lat - REFERENCE_LAT) > LAT_TOL or abs(lon - REFERENCE_LON) > LON_TOL:
            continue
        
        filtered.append({
            "timestamp": ts_dt_utc,
            "timestamp_local": ts_dt_local,
            "snr": item.get("snr"),
            "rssi": item.get("rssi"),
            "temperature": item.get("temperature_1"),
            "relative_humidity": item.get("relative_humidity_2")
        })
    return filtered

def update_plot(df, overall_rate, recent_rate):
    ax[0].clear()
    ax[1].clear()
    
    if df.empty:
        print("Currently no useful data")
        return
    
    df_sorted = df.sort_values("timestamp_local")
    ax[0].plot(df_sorted["timestamp_local"], df_sorted["snr"], marker='o')
    ax[0].set_title(f"SNR over time (Local time)")
    ax[0].set_ylabel("SNR (dB)")
    
    ax[1].plot(df_sorted["timestamp_local"], df_sorted["rssi"], marker='o', color='orange')
    ax[1].set_title(f"RSSI over time (Local time)")
    ax[1].set_ylabel("RSSI (dBm)")

    # time_format = mdates.DateFormatter('%H:%M:%S')
    time_format = mdates.DateFormatter('%H:%M:%S', tz=local_tz)

    ax[0].xaxis.set_major_formatter(time_format)
    ax[1].xaxis.set_major_formatter(time_format)

    # fig.suptitle(f"SWM LoRaWAN Connection \n Successful Rate Overall: {overall_rate:.2%}, 5min: {recent_rate:.2%}", fontsize=14)
    fig.suptitle(f"TTN LoRaWAN Connection \n Successful Rate Overall: {overall_rate:.2%}, 5min: {recent_rate:.2%}", fontsize=14)

    
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

while True:
    data = fetch_data()
    records = filter_data(data)
    if records:
        df_new = pd.DataFrame(records)
        all_data = pd.concat([all_data, df_new]).drop_duplicates(subset=["timestamp"])
    
    if not all_data.empty:
        all_data["timestamp"] = pd.to_datetime(all_data["timestamp"], utc=True)
        if "timestamp_local" not in all_data.columns:
            all_data["timestamp_local"] = all_data["timestamp"].dt.tz_convert(local_tz)

        # Overall success rate
        start_ts_overall = all_data["timestamp"].min()
        latest_ts = all_data["timestamp"].max()
        elapsed_overall = (latest_ts - start_ts_overall).total_seconds()
        expected_overall = elapsed_overall / SAMPLE_INTERVAL
        actual_overall = len(all_data)
        success_overall = actual_overall / expected_overall if expected_overall > 0 else 0

        # 5 min window success rate
        start_ts_recent = datetime.now(timezone.utc) - timedelta(minutes=5)
        df_recent = all_data[all_data["timestamp"] >= start_ts_recent]
        if not df_recent.empty:
            latest_recent_ts = df_recent["timestamp"].max()
            elapsed_recent = (latest_recent_ts - start_ts_recent).total_seconds()
            expected_recent = elapsed_recent / SAMPLE_INTERVAL
            actual_recent = len(df_recent)
            success_recent = actual_recent / expected_recent if expected_recent > 0 else 0
        else:
            elapsed_recent = 0
            expected_recent = 0
            actual_recent = 0
            success_recent = 0

        print(f"[Overall] Elapsed: {elapsed_overall:.1f}s, Expected: {expected_overall:.1f}, Actual: {actual_overall}, Success: {success_overall:.2%}")
        print(f"[5min]    Elapsed: {elapsed_recent:.1f}s, Expected: {expected_recent:.1f}, Actual: {actual_recent}, Success: {success_recent:.2%}")
        print(f"Latest packet UTC: {latest_ts}, Local: {latest_ts.astimezone(local_tz)}")

        update_plot(all_data, success_overall, success_recent)
    
    time.sleep(POLL_INTERVAL)
