import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv("MACHINE LEARNING/SUPERVISED LEARNING/ASSIGNMENT/ipl2.csv")
numeric_cols=['matches','runs','wickets','strike_rate']
scaler=StandardScaler()
df[numeric_cols]=scaler.fit_transform(df[numeric_cols])
df.to_csv("ipl_scaled.csv", index=False)
print(df.head())

# applies only on numeric cols
new_df=df[numeric_cols]
scaler1 =MinMaxScaler()
x_scaled1 = scaler1.fit_transform(new_df)
result1 =pd.DataFrame(x_scaled1,columns=new_df.columns)
print(result1)


