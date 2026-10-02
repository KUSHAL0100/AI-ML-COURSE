from re import X

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

df=pd.read_csv("MACHINE LEARNING/SUPERVISED LEARNING/CLASSWORK/student_marks_small.csv")
print(df)
plt.scatter(
    data=df,
    x="StudyHours",
    y="Marks"
)
plt.title("studyhours and marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
# plt.show()

x=df[['StudyHours']]
y=df['Marks']
x_train, x_test, y_train, y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
# print(x_train,x_test,y_train,y_test)
# create model : 
model = LinearRegression()
#train model
model.fit(x_train,y_train) 

# slope , intercept :
print("model slope :",model.coef_[0])
print("model intercept :",model.intercept_)

# prediction  : 
y_pred = model.predict(x_test)
print("predicted value :",y_pred) 


# comparison :   actual value and  predicted value
comparison = pd.DataFrame({'Actual value':y_test.values,
                           'Predicted value':y_pred})
print(comparison)

# regression  line  :  actual , predict 
plt.figure(figsize=(10,6))

plt.scatter(
    x,
    y,
    color='blue',
    label='Actual value'
    
)
# plt.show()
plt.plot(
    x,
    model.predict(x),
    color='red',
    label='regression line'
)
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study hour vs Marks')
plt.legend()
plt.grid(True)
# plt.show()

# predict new  data  : 

exper = [[8.5]]
predict_marks = model.predict(exper)
print("predict salary :",predict_marks[0])