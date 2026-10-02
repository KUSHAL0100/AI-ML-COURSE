import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score,root_mean_squared_error    

df=pd.read_csv("MACHINE LEARNING/SUPERVISED LEARNING/CLASSWORK/salary_data (1).csv")
print(df)
X=df[['YearsExperience']]
y=df['Salary']

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,   # 80 % train 20 % test
    random_state=42
)

# create model : 
model = LinearRegression()

# train model :
model.fit(X_train,y_train) 

# slope , intercept :
print("model slope :",model.coef_[0])
print("model intercept :",model.intercept_)

# prediction  : 
y_pred = model.predict(X_test)
print("predicted value :",y_pred) 

# comparison :   actual value and  predicted value
comparison = pd.DataFrame({'Actual value':y_test.values,
                           'Predicted value':y_pred})

print(comparison)

mse=mean_squared_error(y_test,y_pred)
print("mse: ",mse)
rmse=np.sqrt(mse)
print("rmse: ",rmse)
mae=mean_absolute_error(y_test,y_pred)
print("mae: ",mae)
r2=r2_score(y_test,y_pred)
print("r2 score: ",r2)