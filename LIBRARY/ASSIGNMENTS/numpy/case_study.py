from matplotlib import axis
import numpy as np

"""sales_data=np.random.randint(50,501,size=(30,5))
print(sales_data)
print(sales_data.shape)
print(sales_data.ndim)
print(sales_data.dtype)
# print(np.count_nonzero(sales_data))
print(sales_data.size)"""

df=np.loadtxt("LIBRARY/ASSIGNMENTS/numpy/retailcorp_sales_data.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4,5),dtype="int64")
print(df)
"""
new_col=df[:,0]
print(new_col)

new_col=df[10:21,:]
print(new_col)

print(np.sum(df,axis=0))
print(np.mean(df,axis=1))
print(np.argmax(df,axis=0))

print(np.std(df[:,0]))
print(np.std(df[:,1]))
print(np.std(df[:,2]))
print(np.std(df[:,3]))

print(np.median(df))
print(np.min(df))
print(np.max(df))

product3=df[:,2].copy()
product3.sort()
print(product3[-3:])

print(np.size(df[np.sum(df,axis=1)>1500])//4, "days has > 1500 sales")


df[df<60]=60
print(df)
# df=np.where(df<60,60,df)

product1=df[:,0].copy()
top5_indices = np.argsort(product1)[-5:]
print("DAYS:", top5_indices+1)
print("Values:", product1[top5_indices])

profit_margin=np.sum(df,axis=0)*[0.2,0.35,0.15,0.4,0.25]
print(profit_margin)
min=np.min(df,axis=0)
max=np.max(df,axis=0)

print(min)
normalized = (df - min) / (max - min)

print(normalized)
print(np.diff(df))

forecast = np.array([200, 310, 150, 420, 280])
df=np.vstack((df,forecast))
# print(df)
flattendata=df.flatten()
print(flattendata.size)
total_sales=np.sum(df,axis=1)
print("3 Days: ",df[np.argsort(total_sales)[-3:]])

total_bonus=df[np.sum(df,axis=1)>400]
total_bonus=np.sum(np.sum(total_bonus,axis=1)*0.10)
print(total_bonus)

flatten=df.flatten()
flatten=np.split(flatten,2) #REturns python list,not numpy array
flatten=np.mean(flatten,axis=1)
print(flatten)
"""

np.save("cleaned_sales.npy", df)
# Reload the array
loaded_data = np.load("cleaned_sales.npy")
print(loaded_data)