import pandas as pd

timestamps = [
    "2024-06-01 14:30",
    "2024-06-02 09:15",
    "2024-06-03 20:45"
]

dates = pd.to_datetime(timestamps)

print(dates)