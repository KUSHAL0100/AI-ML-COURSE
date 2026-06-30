""""
Tasks
1.
Given a CSV file containing Zomato restaurant ratings, use pandas to detect outliers in the 'user_rating' column using the IQR method and print the indices of the detected outliers.a
2.
Create a boxplot for the 'order_amount' column from a Swiggy orders dataset using matplotlib, and visually identify any outliers present.<br><br><em><strong>Hint:</strong> Use plt.boxplot() and label your axes for clarity.</em>
3.
Apply winsorization to the 'transaction_amount' column in a Paytm transactions DataFrame to cap all values above the 95th percentile and below the 5th percentile, then display the updated column statistics.
4.
You have a DataFrame of Flipkart product prices stored as strings with currency symbols (e.g., '₹1,299'). Convert this column to numeric type using pandas, ensuring all non-numeric characters are removed.<br><br><em><strong>Hint:</strong> Use str.replace() and astype().</em>
5.
Fix the following code snippet where the 'is_premium' column in a Spotify user DataFrame is a mix of boolean, string, and integer types. Convert the entire column to boolean type, treating 'True', 1, and 'yes' as True, and everything else as False.
"""

import pandas as pd
import matplotlib.pyplot as plt
"""df=pd.read_csv("LIBRARY\\ASSIGNMENTS\\pandas\\zomato.csv")
Q1=df['user_rating'].quantile(0.25)
Q3=df['user_rating'].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1 - 1.5*IQR
upper_bound=Q3+ 1.5*IQR

outliers=df[
    (df['user_rating'] < lower_bound) |
    (df['user_rating'] > upper_bound)
]
print(outliers.index+1)

plt.boxplot(df['user_rating'])
plt.ylabel("Ratings")
plt.title("Ratings")
plt.show()"""



#WINSORIZATION
#2 WAYS
# df = pd.DataFrame({
#     "transaction_amount": [100, 250, 300, 450, 500, 600, 700, 800, 900, 1000, 5000]
# })
"""lower_limit = df["transaction_amount"].quantile(0.05)
upper_limit = df["transaction_amount"].quantile(0.95)

# Apply winsorization
df["transaction_amount"] = df["transaction_amount"].clip(
    lower=lower_limit,
    upper=upper_limit
)"""

# from scipy.stats.mstats import winsorize
# limits=[0.05, 0.05] means:
# Lower 5% values are capped at the 5th percentile
# Upper 5% values are capped at the 95th percentile
# df["transaction_amount"] = winsorize(
#     df["transaction_amount"],
#     limits=[0.05, 0.05]
# )


#QUESTION 4
"""df = pd.DataFrame({
    "product_name": ["Mobile", "Laptop", "Headphones", "Smartwatch"],
    "price": ["₹12,999", "₹54,999", "₹2,499", "₹7,999"]
})
df["price"]=(df["price"].str.replace("₹","").str.replace(",",""))

#df["price"] = df["price"].str.replace(r"\D", "", regex=True) regex =True and \D says remove every non-digit character,and regex=True means you want to match a pattern ,rather than exect number
pd.to_numeric(df['price'])
print(df)"""


#| If you're replacing...                     | Use           |
#| ------------------------------------------ | ------------- |
#| A fixed character/string (`₹`, `,`, `abc`) | `regex=False` |
#| A pattern (`\D`, `[A-Z]`, `\s+`)           | `regex=True`  |
#by default false j hoyy





#QUESTIN 5 WITH 3 METHODS
#ISIN,REPLACE,MAPPING
df = pd.DataFrame({
    "is_premium": [True, "True", 1, "yes", False, 0, "TRUE"]
})

df['is_premium']=(
    df["is_premium"].astype(str)
    .str.lower()
    .replace({
        'true':True,
        '1':True,
        "yes":True,
        "false":False,
        "0":False,
    })
    .astype(bool)
)

print(df)





"""
not a assignment question
df =pd.DataFrame({
    "id" :[1,2,3,4,5,6,7],
    "name" :["ram","sita","ravan","laxman","surekha","ravi","ramesh"],
    "status" :["True","False","True","False","True","False","True"],
    "experience":["2","4","1","5","7","9","3"],
    "city" :["ahm","ahmedabad","bombay","mumbai","delhi","pune","rajstan"]
})

df["city"]=df["city"].replace(["ahm","bombay"],["ahmedabad","mumbai"])
print(df)
"""

