"""
1.
Download a sample CSV file of IPL player stats (include columns like player name, runs, matches, and some missing values). Load it into a pandas DataFrame and use isnull() and notnull() to print how many missing values are present in each column.
2.
Using the loaded IPL player stats DataFrame, apply dropna(axis=0, how='any') to remove all rows with any missing data and display the shape of the DataFrame before and after dropping.
3.
For the 'runs' column in your IPL player stats DataFrame, use fillna() to replace missing values with the mean of the column. Print the updated column to verify the changes.
4.
Simulate a Zomato-style restaurant ratings dataset with some missing ratings. Use forward fill (method='ffill') to fill missing values in the ratings column, then use backward fill (method='bfill') for any remaining missing values. Show the before and after results.
5.
Pick any one column with missing values from your dataset and explain which missingness mechanism (MCAR, MAR, or MNAR) is most likely and why, using 2-3 sentences.<br><br><em><strong>Hint:</strong> Think about whether the missing data is random or related to other factors in the dataset.</em>
"""
import pandas as pd
import numpy as np
"""df = pd.read_csv("LIBRARY\\ASSIGNMENTS\\pandas\\IPL.csv")
# Missing values count for each column
missing_count = df.isnull().sum()

# Columns with null values
null_columns = missing_count[missing_count > 0]
print("\nColumns with Null Values:")
print(null_columns)

# Total missing values in the entire dataset
total_missing = df.isnull().sum().sum()
print("\nTotal Missing Values:", total_missing)


df = pd.read_csv("LIBRARY\\ASSIGNMENTS\\pandas\\IPL.csv")
original_rows = len(df)

df = df.dropna(axis=0)

new_rows = len(df)

print("Rows removed:", original_rows - new_rows)
print("Remaining rows:", new_rows)

df = pd.DataFrame({
    "Restaurant": [
        "Spice Villa",
        "Food Hub",
        "Pizza Point",
        "Royal Dine",
        "Burger Town",
        "Cafe Delight"
    ],
    "Rating": [np.nan, 4.2, 3.8, np.nan, np.nan, 4.5]
})

print("Before Filling:")
print(df)

print("Forward filling")
df['Rating']=df['Rating'].ffill()
print(df)

print("Backword Filling")
df["Rating"]=df["Rating"].bfill()
print(df)

"""


