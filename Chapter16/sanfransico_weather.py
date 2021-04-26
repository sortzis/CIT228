import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'Chapter16/history_data.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[1], '%m/%d/%y')
        try:
            high = int(row[2])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('fast')
fig, ax = plt.subplots()
ax.plot(dates, highs, c="orange", alpha=0.5)
ax.plot(dates, lows, c="green", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

ax.set_title("Daily high and low temperatures, 2/1/2021 to 4/24/2021", fontsize=20)
ax.set_xlabel('', fontsize=12)
ax.set_ylabel("Temperatures (F)", fontsize=12)
fig.autofmt_xdate()
ax.tick_params(axis='both',which='major',labelsize=12)
plt.show()