clear; clc; close all

data = readtable('device_log.xlsx');
time = datetime(data.timestamp,'InputFormat', 'yyyy-MM-dd''T''HH:mm:ss.SSSSSSXXX','TimeZone', 'UTC');


t_start = datetime(2025,6,15,9,0,0, 'TimeZone', 'UTC');
t_end   = datetime(2025,6,15,11,0,0, 'TimeZone', 'UTC');


idx = (time >= t_start) & (time <= t_end);
time_filtered = time(idx);
temp_filtered = data.temperature_1(idx);
humi_filtered = data.relative_humidity_2(idx);
snr = data.snr(idx);
rssi = data.rssi(idx);


figure;
subplot(2,1,1)
plot(time_filtered, snr, '-o', 'LineWidth', 1.2);
xlabel('Time (UTC)');
ylabel('SNR');
title('SNR between 2025-06-15 09:00 and 11:00 (UTC)');
subplot(2,1,2)
plot(time_filtered, rssi, '-o', 'LineWidth', 1.2);
xlabel('Time (UTC)');
ylabel('RSSI');
title('RSSI between 2025-06-15 09:00 and 11:00 (UTC)');
grid on;
ax = gca;
ax.XAxis.TickLabelFormat = 'HH:mm:ss';

figure;
subplot(2,1,1)
plot(time_filtered, temp_filtered, '-o', 'LineWidth', 1.2);
xlabel('Time (UTC)');
ylabel('Temperature');
title('Temperature between 2025-06-15 09:00 and 11:00 (UTC)');
subplot(2,1,2)
plot(time_filtered, humi_filtered, '-o', 'LineWidth', 1.2);
xlabel('Time (UTC)');
ylabel('Humidity');
title('Humidity between 2025-06-15 09:00 and 11:00 (UTC)');
grid on;
ax = gca;
ax.XAxis.TickLabelFormat = 'HH:mm:ss';
