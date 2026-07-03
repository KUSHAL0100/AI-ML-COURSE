import pandas as pd

timestamps = [
    "2024-06-01 14:30",
    "2024-06-02 09:15",
    "2024-06-03 20:45"
]

dates = pd.to_datetime(timestamps)

print(dates)

df = pd.read_csv("LIBRARY/ASSIGNMENTS/pandas/flipkart_orders.csv")

# df["order_date"] = pd.to_datetime(df["order_date"])

# df["year"] = df["order_date"].dt.year
# df["month"] = df["order_date"].dt.month
# df["weekday"] = df["order_date"].dt.day_name()

# print(df[['year','month','weekday']])




# df["order_date"] = pd.to_datetime(df["order_date"])
# df.set_index("order_date", inplace=True)
# print(df.resample("W").size())


df = pd.read_csv("LIBRARY\ASSIGNMENTS\pandas\instagram_posts.csv")

df["posted_at"] = pd.to_datetime(df["posted_at"], utc=True)
df["posted_at"] = df["posted_at"].dt.tz_convert("Asia/Kolkata")

print(df.head())