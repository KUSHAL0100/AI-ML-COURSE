from unittest import result

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Temperature":np.array([15,18,20,22,25,28,30,32,35]),
    "Sales" : np.array([100,130,160,200,270,350,420,500,650])
})

print(data)

X=data[['Temperature']]
y=data['Sales']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model=LinearRegression()
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)
print("predicted sales :",y_predict)


result=pd.DataFrame({
    'Actual':y_test.values,
    'Predicted':y_predict
})

R2_score=r2_score(y_test,y_predict)
print("R2 score: ",R2_score)

#polynomial features:
ploy=PolynomialFeatures(degree=2)
X_ploy=ploy.fit_transform(X)

#model
poly_model=LinearRegression()
poly_model.fit(X_ploy,y)

#predict
y_predict_poly = poly_model.predict(X_ploy)
print("predicted sales :",y_predict_poly)

# r2 score  : 
R2_score_poly = r2_score(y,y_predict_poly)
print("R2 score :",R2_score_poly)


"""result1 = pd.DataFrame({
    'Actual':y_test.values,
    'Predicted':y_predict_poly
})
print("polynomial features :",result1.head())"""

if R2_score < R2_score_poly:
    print("\nPolynomial Regression performs better because the relationship between Temp and sales  is nonlinear.")
else:
    print("\nLinear Regression performs better.")

plt.figure(figsize=(10,10))
plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Linear Regression")
plt.plot(X, y_predict_poly, label="Polynomial Regression")
plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.grid()
plt.show()