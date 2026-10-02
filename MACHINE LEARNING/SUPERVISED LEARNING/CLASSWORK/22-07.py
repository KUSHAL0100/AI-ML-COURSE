import numpy as np
import pandas as pd
from scipy.stats import zscore

df=pd.read_csv("MACHINE LEARNING/SUPERVISED LEARNING/CLASSWORK/customer_purchase_dataset.csv")
print(df)

df['z_score']=np.abs(zscore(df['Salary']))
print(df)
df=df[df['z_score']<2.5]
print(df)