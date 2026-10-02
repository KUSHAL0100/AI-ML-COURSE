import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet


df=pd.read_csv('MACHINE LEARNING/SUPERVISED LEARNING/CLASSWORK/CAR DETAILS FROM CAR DEKHO.csv')

# print(df.isna().sum())
# print(df['owner'].unique())
# owner ne 1,2,3,4 ma convert kri daiye
df['owner']=df['owner'].map({
    'Fourth & Above Owner':1,
    'Third Owner':2,
    'Second Owner' :3,
    'First Owner': 4 ,
    'Test Drive Car': 0
})

X=df[['year','km_driven','owner']]
y=df['selling_price']

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


#scale
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
x_test_scaled=scaler.transform(X_test)

# print(np.isnan(X_train_scaled).sum())


#model
model=LinearRegression()
model.fit(X_train_scaled,y_train)

#predict
y_predict=model.predict(x_test_scaled)
# print("PRedicted value: ",y_predict)

# r2 score : 
R2_score = r2_score(y_test,y_predict)
print("R2 score :",R2_score)
print("mSE: ",mean_squared_error(y_test,y_predict))
print("mAE: ",mean_absolute_error(y_test,y_predict))

#ridge
ridge=Ridge(alpha=1)
ridge.fit(X_train_scaled,y_train)
y_pred_ridge = ridge.predict(x_test_scaled)
r2_ridge=r2_score(y_test, y_pred_ridge)
print("Ridge")
print("MSE:", mean_squared_error(y_test, y_pred_ridge))
print("MAE:", mean_absolute_error(y_test, y_pred_ridge))
print("R2:", r2_ridge)


#Lasso
lasso=Lasso(alpha=1.0)
lasso.fit(X_train_scaled,y_train)
y_pred_lasso=lasso.predict(x_test_scaled)
r2_lasso=r2_score(y_test, y_pred_lasso)
print("Ridge")
print("MSE:", mean_squared_error(y_test, y_pred_lasso))
print("MAE:", mean_absolute_error(y_test, y_pred_lasso))
print("R2:", r2_lasso)

#elasticnet
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic.fit(X_train_scaled, y_train)
y_pred_elastic = elastic.predict(x_test_scaled)
r2_elasitc=r2_score(y_test, y_pred_elastic)
print("Elastic Net")
print("MSE:", mean_squared_error(y_test, y_pred_elastic))
print("MAE:", mean_absolute_error(y_test, y_pred_elastic))
print("R2:", r2_elasitc)



if r2_ridge <r2_lasso:
    if r2_ridge<r2_elasitc:
        print("Ridge is better model to use")
    else:
        print("Elastic is better to use")
else:
    if r2_lasso < r2_elasitc:
        print("Lasso is better to use")
    else:
        print("Elastic is better to use")