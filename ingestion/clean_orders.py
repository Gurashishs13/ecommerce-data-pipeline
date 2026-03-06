import pandas as pd

df = pd.read_csv("data/orders_raw.csv")

print("Raw data preview")
print(df.head())

df = df.drop_duplicates()

df['order_date'] = pd.to_datetime(df['order_date'])

df['total_price'] = df['price'] * df['quantity']

df.to_csv("data/orders_clean.csv", index=False)

print("Clean data saved")