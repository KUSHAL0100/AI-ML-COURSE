"""
1.
Connect to a MySQL or PostgreSQL database using SQLAlchemy and pandas, then use pd.read_sql() to load the entire 'restaurants' table (imagine Zomato backend) into a DataFrame and display the first 5 rows.
2.
Use pd.read_sql_query() to fetch only the 'name' and 'rating' columns from a 'movies' table (think BookMyShow-like data) where rating is above 8, and print the resulting DataFrame.<br><br><em><strong>Hint:</strong> Write a custom SQL SELECT query as the first argument to pd.read_sql_query().</em>
3.
Read a JSON dataset from the URL https://jsonplaceholder.typicode.com/users using pandas, convert it into a DataFrame, and print the usernames column.<br><br><em><strong>Hint:</strong> Use pd.read_json() directly with the URL.</em>
4.
You have two CSV files: 'orders.csv' (order_id, user_id, amount) and 'users.csv' (user_id, username). Load both into DataFrames using pathlib for file paths, then merge them on 'user_id' to show a combined table with username and amount.
5.
Concatenate two DataFrames representing 'today_orders' and 'yesterday_orders' (each with columns: order_id, item, price), and display the combined DataFrame.<br><br><em><strong>Constraint:</strong> Use pd.concat() and reset the index after concatenation.</em>
"""
import pandas as pd

# df=pd.read_json("https://jsonplaceholder.typicode.com/users")
# print(df['username'])

# df1=pd.read_csv("LIBRARY/ASSIGNMENTS/pandas/orders.csv")
# df2=pd.read_csv("LIBRARY/ASSIGNMENTS/pandas/users.csv")

# merge_df=pd.merge(df1,df2)
# print(merge_df)

# DataFrame for today's orders
# today_orders = pd.DataFrame({
#     "order_id": [101, 102],
#     "item": ["Laptop", "Mouse"],
#     "price": [55000, 800]
# })

# # DataFrame for yesterday's orders
# yesterday_orders = pd.DataFrame({
#     "order_id": [99, 100],
#     "item": ["Keyboard", "Monitor"],
#     "price": [1500, 12000]
# })

# combined_orders=pd.concat((today_orders,yesterday_orders)).reset_index(drop=True)
# print(combined_orders)
