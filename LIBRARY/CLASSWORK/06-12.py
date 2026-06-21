import numpy as np
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1 


"""arr=np.ones(25,dtype=np.int64).reshape(5,5)
arr[1:4,1:4]=0
arr[2,2]=9
print(arr)"""

"""arr=np.arange(1,31).reshape(6,5)
print(arr[2:4,0:2])
"""

"""arr=np.arange(1,31).reshape(5,6)
print(arr[:-1,1])"""

arr=np.arange(1,31).reshape(5,6)
print(arr[[0,3,4]][:,3:5])
# all rows,then start:stop for [:,3:5]
