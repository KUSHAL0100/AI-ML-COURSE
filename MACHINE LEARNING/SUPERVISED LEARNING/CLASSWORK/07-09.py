import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

df=pd.read_csv('MACHINE LEARNING/SUPERVISED LEARNING/CLASSWORK/housing.csv')
# print(df.isnull().sum())

df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())
# print(df.isnull().sum())
X=df[['housing_median_age','total_rooms','total_bedrooms','population','households','median_income']]
y=df['median_house_value']


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_predict=model.predict(X_test)
print("y predict: ",y_predict)

#intercept, and slope
print("intercept: ",model.intercept_)
print("Slope: ",model.coef_)

plt.plot(y_test.iloc[:50].values, label="Actual")
plt.plot(y_predict[:50], label="Predicted")

plt.xlabel("Test Data")
plt.ylabel("House Value")
plt.title("Actual vs Predicted - First 50")
plt.legend()
plt.grid(True)
plt.show()
