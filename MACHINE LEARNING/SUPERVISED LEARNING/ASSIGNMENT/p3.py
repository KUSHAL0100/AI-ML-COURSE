"""
1.
Download a small sample of IPL match data (CSV) with some missing values in player stats. Load it using pandas and print the number of missing values in each column.
2.
For the 'player_age' column in your IPL dataset, fill all missing values with the median age using pandas' fillna() method and display the updated column.
3.
Suppose the 'team' column in your IPL dataset contains missing values. Replace all missing team names with the constant value 'Unknown' and print the first 10 rows.
4.
Take the 'venue' column (categorical) from your IPL dataset and apply one-hot encoding using pandas' get_dummies(). Show the resulting DataFrame with the new columns.
5.
Use LabelEncoder from sklearn to encode the 'player_role' column (e.g., Batsman, Bowler, Allrounder) in your IPL dataset, and display the mapping from original roles to encoded values.<br><br><em><strong>Hint:</strong> Use LabelEncoder's classes_ attribute to see the mapping.</em>
"""
import pandas as pd

df = pd.read_csv("MACHINE LEARNING/SUPERVISED LEARNING/ASSIGNMENT/ipl.csv")

print(df.isnull().sum())

df['player_age']=df['player_age'].fillna(df['player_age'].median())
print(df['player_age'])
df['team']=df['team'].fillna('Unknown')
print(df['team'])


venue_encoded = pd.get_dummies(df, columns=["venue"])

print(venue_encoded)