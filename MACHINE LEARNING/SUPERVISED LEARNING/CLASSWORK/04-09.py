
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

data={
    "spend":[10,20,30,40,50,60,70,80],
    "sales":[25,32,40,48,55,65,72,85]
}

df=pd.DataFrame(data)
print(df)

X=df[['spend']]
y=df['sales']

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_predict=model.predict(X_test)
print("y_predict: ",y_predict)

# intercept , slope :
print("intercept :",model.intercept_)
print("slope :",model.coef_)

new_data=[[45]]
model_predict=model.predict(new_data)
print("New Predict: ",model_predict)

plt.scatter(X,y,marker='o',color='red',label='actual')
plt.plot(X,model.predict(X),color='blue',label='linear regression')
plt.title("linear regression  graph")
plt.xlabel("Spend")
plt.ylabel("Sales")
plt.grid(True)
plt.show()