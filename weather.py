import requests
import sys
import numpy as np
import matplotlib.pyplot as plt
from typing import Any
from datetime import date


# TODO: Add axis labels and units 
def find_item(list_to_check: list, target: Any) -> list:
    """
    Function used to return indexes of given element in list 
    """
    return [index for index, value in enumerate(list_to_check) if value == target]


def delete_item(list_to_check: list, targets: list) -> list:
    list_to_check = np.array(list_to_check)
    return list(np.delete(list_to_check, targets))


params = {
        'latitude': '51.10',
        'longitude': '17.03',
        'start_date': f'{date.today().year}-{date.today().month:02d}-{date.today().day:02d}',
        'end_date': str(date.today()),
        'timezone': 'auto',
        'daily': 'temperature_2m_mean',
        }

url = 'https://archive-api.open-meteo.com/v1/archive'

req = requests.get(url, params=params)

if req.status_code == 200:
    data = req.json()
else:
    print("Error: Check url!")
    sys.exit(1)

temp_data = data["daily"]["temperature_2m_mean"]

data_labels = data["daily"]["time"]

temp_data_empty = find_item(temp_data, None)

if temp_data_empty:
    print("Caution: Some data cells are empty!")
    print("Removing empty cells by force")
    temp_data = delete_item(temp_data, temp_data_empty)
    data_labels = delete_item(data_labels, temp_data_empty)

# WARN: Find better name!
# Days for pyplot (numbers)
day_number = [x for x in range(len(temp_data))]

if len(day_number) % 2 == 0:
    day_number_labels = data_labels[0::4]
    label_positions = day_number[0::4]
else:
    day_number_labels = data_labels[0::5]
    label_positions = day_number[0::5]

fig, ax = plt.subplots()

ax.plot(day_number, temp_data)
ax.grid()

ax.set_xticks(label_positions)
ax.set_xticklabels(day_number_labels)

print("Plotting...")
plt.savefig("weather_plot.png")

