
import pandas as pd
import numpy as np

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

# print(df.isna().sum())
# print(df.isna().mean()*100)

"""print("Before removing null customer name: ",df.shape[0])
# df['customer_name'].dropna(inplace=True) WON'T WORK
df.dropna(subset=['customer_name'],inplace=True)
print("After removing null customer name: ",df.shape[0])"""

#GREAT ALTERNATIVES
#df = df[df["customer_name"].notna()]  BOOLEAN INDEXING
#df = df.loc[df["customer_name"].notna()] SAME



# df=df.dropna(thresh=(df.isna().sum().mean()<0.4)) won't work

# print(df[(df.isna().sum(axis=0)) > (df.shape[0]/100*40)]) won't work
"""
print(df.shape[1])
df = df.drop(columns=df.columns[df.isna().mean() > 0.40])
print(df.shape[1])

df['age']=df['age'].fillna(df['age'].median())
df['city']=df['city'].fillna('unknown')
# df['rating']=df['rating'].fillna(df.groupby('category')['rating'].mean()) WON'T WORKKK
df['rating']=df['rating'].fillna(df.groupby('category')['rating'].transform('mean')) 

"""
# df['delivery_date']=df['delivery_date'].ffill()
# print(df['delivery_date'])

# df['review']=df['review'].fillna('no review')
# print(df['review'])

# print("Duplicate rows: ",df.duplicated().sum())


# print("Before removing duplicates:", df.shape)

# df = df.drop_duplicates()

# print("After removing duplicates:", df.shape)


# duplicates = df.duplicated(subset=["order_id"]).sum()
# print("Duplicate order_id:", duplicates)
# df = df.drop_duplicates(subset=["order_id"])
# print("Rows removed:", duplicates)
# print("Remaining rows:", df.shape[0])
"""
Q1 = df["revenue"].quantile(0.25)
Q3 = df["revenue"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
"""

"""Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]

print("Number of Outliers:", outliers.shape)"""

"""mean = df["revenue"].mean()
std = df["revenue"].std()
z_score = (df["revenue"] - mean) / std
outliers = df[(z_score > 3) | (z_score < -3)]
print(outliers)"""

"""# Calculate 5th and 95th percentile
lower = df["revenue"].quantile(0.05)
upper = df["revenue"].quantile(0.95)

# Cap the outliers
df["revenue"] = df["revenue"].clip(lower=lower, upper=upper)
print(df["revenue"].describe())"""

"""df["revenue_correct"] = df["revenue"] == (df["discounted_price"] * df["quantity"])

print(df[["discounted_price", "quantity", "revenue", "revenue_correct"]].head())

df["final_price"] = df["discounted_price"] * df["quantity"]

print(df[["discounted_price", "quantity", "final_price"]].head())


df["is_high_value"] = (df["revenue"] > 5000) & (df["order_status"] == "Delivered")

print(df[["revenue", "order_status", "is_high_value"]].head())

df['category']=df['category'].str.lower()
df['customer_name']=df['customer_name'].str.title()
# print("Before: ",df['order_status'])
df['order_status']=df['order_status'].str.replace("Delivered","Completed")
# print("After: ",df['order_status'])



order_number = df['order_id'].str.split('D', expand=True)
order_number[1] = order_number[1].astype('int64')
df['order_number']=order_number[1]

# print(df)

recommended_orders = df[df['review'].str.contains('recommended', case=False, na=False)]
print(recommended_orders)

count = df['customer_name'].str.startswith('R').sum()
print(count)

df['order_date'] = pd.to_datetime(df['order_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['day'] = df['order_date'].dt.day

# print(df[['order_date','year','month','day']].head())

count=df['month'].value_counts().sort_index()
print(count)

df['calc_delivery_days'] = (df['delivery_date'] - df['order_date']).dt.days #first step convert krna ,in df.date_time first 

print(df[['delivery_days','calc_delivery_days']].head())

orders_2023 = df[df['order_date'].dt.year == 2023]

print(orders_2023)

orders = df[
    (df['order_date'] >= '2023-01-01') &
    (df['order_date'] <= '2023-03-31')
]
print(orders)

print(df['order_date'].dt.day_name().value_counts())

df['category']=df['category'].str.lower()
delivered = df[df['order_status'] == 'Delivered']
print(delivered.groupby('category')['delivery_days'].mean())

df_customer = df[['customer_id', 'customer_name', 'age', 'city', 'state']]
df_order = df[['order_id', 'customer_id', 'product_name', 'category', 'revenue', 'order_status']]
merged_df = pd.merge(df_customer, df_order, on='customer_id', how='inner')

# print(merged_df.head())
print(merged_df.shape)
left_join = pd.merge(df_order, df_customer,
                     on='customer_id',
                     how='left')
print(left_join.shape)

# print(df['city'].value_counts())
city_tier = pd.DataFrame({
    'city': [
        'Ahmedabad', 'Surat', 'Mumbai', 'Delhi', 'Bengaluru',
        'Chennai', 'Hyderabad', 'Kolkata', 'Pune',
        'Jaipur', 'Lucknow', 'Nagpur', 'Indore'
    ],
    'tier': [
        'Tier 1', 'Tier 2', 'Tier 1', 'Tier 1', 'Tier 1',
        'Tier 1', 'Tier 1', 'Tier 1', 'Tier 1',
        'Tier 2', 'Tier 2', 'Tier 2', 'Tier 2'
    ]
})
merged = pd.merge(df, city_tier,
                  on='city',
                  how='left')
print(merged.groupby('tier')['revenue'].mean())


before_2023 = df[df['order_date'] < '2023-01-01']
after_2023 = df[df['order_date'] >= '2023-01-01']
new_df = pd.concat([before_2023, after_2023],
                   ignore_index=True)
print(df.shape)
print(new_df.shape)

summary = df.groupby('product_name').agg(
    avg_rating=('rating', 'mean'),
    total_orders=('order_id', 'count')
).reset_index()
print(summary)
merged = pd.merge(df,
                  summary,
                  on='product_name',
                  how='left')

top = summary.sort_values('avg_rating',
                          ascending=False).head()
print(top)


outer_df = pd.merge(
    df_customer,
    df_order,
    on='customer_id',
    how='outer'
)

print(outer_df.head())
"""