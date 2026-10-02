"""
1.
Download the 'Spotify Top 50 Songs' dataset from Kaggle, load it into a pandas DataFrame, and identify which columns should be used as features and which as the label if you want to predict a song's popularity score.
2.
Split the loaded Spotify dataset into training and test sets using sklearn's train_test_split function, with 80% for training and 20% for testing. Print the number of rows in each set.
3.
Given a simple linear regression model predicting song popularity from danceability, intentionally use only 5% of the data for training and 95% for testing. Observe the model's performance and explain whether this is likely to cause underfitting or overfitting.<br><br><em><strong>Hint:</strong> Look at the accuracy or error on both train and test sets to support your answer.</em>
4.
Draw or find a graph online that visually explains the bias–variance tradeoff, and write a short note describing how this tradeoff would affect predictions in a Zomato restaurant rating predictor app.
5.
Give a real example (outside of healthcare/hospital) of overfitting from any app you use (e.g., Instagram, Flipkart, Swiggy), and explain in 2-3 lines why it might happen in that scenario.
"""

"""#1.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df=pd.read_csv("MACHINE LEARNING/SUPERVISED LEARNING/ASSIGNMENT/spotify_top50_2021.csv")
# print(df.columns)
X = df[['danceability',
        'energy',
        'key',
        'loudness',
        'mode',
        'speechiness',
        'acousticness',
        'instrumentalness',
        'liveness',
        'valence',
        'tempo',
        'duration_ms',
        'time_signature']]  

X=df.drop(columns=['popularity','track_name','artist_name'])
y=df['popularity']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("Train Rows: ",X_train.shape[0])
print("Test Rows: ",X_test.shape[0])

#3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load the dataset
df = pd.read_csv("MACHINE LEARNING/SUPERVISED LEARNING/ASSIGNMENT/spotify_top50_2021.csv")   # Change filename if needed
# Feature and Label
X = df[["danceability"]]
y = df["popularity"]

# 5% training, 95% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    train_size=0.05,
    test_size=0.95,
    random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Compare actual and predicted values
result = pd.DataFrame({
    "Actual Popularity": y_test.values,
    "Predicted Popularity": predictions
})

print(result.head(10))
"""

#4
from cProfile import label

import matplotlib.pyplot as plt
from numpy import var

# Sample values
complexity = [1, 2, 3, 4, 5]
bias = [9, 6, 4, 2, 1]
variance = [1, 2, 4, 6, 9]
total_error = [10, 8, 6, 8, 10]
plt.plot(complexity,bias,label="Bias")
plt.plot(complexity,variance,label="Variance")
plt.plot(complexity,total_error,label="Total Error")
plt.title("Bias-Variance Tradeoff")
plt.xlabel("Model Complexity")
plt.ylabel("Error")
plt.legend()
plt.grid(True)

plt.show()



#Q-5
#This happens because the model becomes too focused on the training data and fails to generalize to the user's broader interests, resulting in overfitting.