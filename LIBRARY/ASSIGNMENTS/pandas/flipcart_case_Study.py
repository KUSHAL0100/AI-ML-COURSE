import pandas as pd
import numpy as np
from sympy import false

df=pd.read_csv("LIBRARY/ASSIGNMENTS/pandas/flipkart_orders.csv")
# revenue=pd.Series(df['revenue'])
# print(revenue.head(10))

# category=pd.Series(df['category'])
# print(category.unique())
# print("total count of each category: ",category.value_counts())

# new_df=df[['product_name','category','price','quantity','revenue']]

# df.info()
# print(df)
# new_df=df[['product_name','revenue']]
# print(type(new_df))

# print(df.head(8))
# print(df.tail(6))
# print(df.info())
# print(df.describe(include='all'))
# df.to_csv("flipkart_cleaned.csv",index=False)


# new_df=df[['order_id','product_name','category','revenue']]
# print(df.iloc[50:61,0:5])
# delivered_orders = df.loc[df["order_status"] == "Delivered"]

# print(delivered_orders)
# high_revenue = df[df["revenue"] > 10000]

# print(high_revenue)

# electronics_mumbai = df[(df["category"] == "Electronics") & (df["city"] == "Mumbai")]

# print(electronics_mumbai)

# discount_delivered = df.loc[
#     (df["discount_pct"] == 50) & (df["order_status"] == "Delivered")
# ]

# print(discount_delivered)

# high_rated = df[(df["rating"] > 4.0) & (df["category"] == "Electronics")]

# print(high_rated)

# Count the number of such orders
# print("Total Orders:", len(high_rated))
# print("Total Orders:", high_rated["rating"].count()) #ALT
# print("Total Orders:", high_rated.shape[0]) #ALT

# upi_orders = df.query("age > 40 and payment_method == 'UPI'")

# print(upi_orders)

# desc_order=df.sort_values(by="price",ascending=False)
# print(desc_order.head(10))


# earliest_orders = df.sort_values(by="order_date", ascending=True)
# print(earliest_orders.head())

# sorted_data = df.sort_values(
#     by=["category", "revenue"],
#     ascending=[True, False]
# )
# sorted_data=sorted_data
# print(sorted_data)

# top_rated = df.sort_values(
#     by="rating",
#     ascending=False
# )

# print(top_rated.head(10))
# df.index = range(1001, 1001 + len(df)) #df.shape[0] bhi chalat

# print(df.head())

print(df.isna().sum())
print(df.isna().mean()*100)