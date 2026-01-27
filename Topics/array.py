#Note: This page shows you how to use LISTS as ARRAYS, however, 
# to work with arrays in Python you will have to import a library, like the NumPy library.
import numpy as np
list1=[1,2,3,4]
arr=np.array ([1,2,3,4,])

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)



arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)



arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

    import numpy as np

a = np.arange(4)
for x in np.nditer(a, op_dtypes=['float']):
    print(x)
