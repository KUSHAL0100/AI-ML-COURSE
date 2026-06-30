import pandas as pd

# Mock Zomato order history
# df = pd.DataFrame({
#     "restaurant_name": ["Pizza Hut", "Domino's", "Pizza Hut", "KFC", "Domino's"],
#     "order_date": ["2026-06-25", "2026-06-26", "2026-06-25", "2026-06-27", "2026-06-26"]
# })

# duplicates = df[df.duplicated(subset=["restaurant_name", "order_date"])]
# print(duplicates)

# df = pd.DataFrame({
#     "review": [
#         "Good product",
#         "Excellent",
#         "Good product",
#         "Worth buying",
#         "Excellent",
#         "Excellent",
#         "Nice quality"
#     ]
# })

# # Count reviews
# top_reviews = df["review"].value_counts().head(3)

# print(top_reviews) 


# df = pd.DataFrame({
#     "playlist_name": ["Workout", "Chill", "Workout", "Party", "Party"],
#     "creator": ["Rahul", "Priya", "Rahul", "Amit", "Amit"]
# })

# # Remove duplicates
# df = df.drop_duplicates()

# print(df)


# df = pd.DataFrame({
#     "username": [
#         "insta_queen",
#         "insta-queen",
#         "instaqueen",
#         "insta_queen",
#         "insta-queen"
#     ]
# })

# df["username"] = df["username"].replace({
#     "insta_queen": "instaqueen",
#     "insta-queen": "instaqueen"
# })

# print(df)


df = pd.DataFrame({
    "payment_status": [
        "Yes",
        " yes ",
        "Y",
        "No",
        " no ",
        "N",
        "Yes "
    ]
})


# df['payment_status']=df['payment_status'].str.strip()
# # print(df)
# df["payment_status"]=df["payment_status"].str.lower()
# print(df)
# df["payment_status"]=(df["payment_status"].map({
#     'yes':1,
#     'y':1,
#     'n':0,
#     "no":0
# }))
# #map and areplace vache no dif ee ke,replace ma koi scenario rahi jay,to ee evo ne evo rehse,map ma ene NaN kri deva ma avse
# print(df)