# import numpy
import numpy
data = numpy.array([1, 2, 3])
print(data)

# NumPy is usually imported under the np alias.
import numpy as np
data = np.array([1, 2, 3, 4])
print(data)

# Checking NumPy Version
import numpy as np
print(np.__version__)

# Create a NumPy ndarray Object
import numpy as np
data = np.array([1, 2, 3, 4])
print(data)
print(type(data))

"""
To create an ndarray, we can pass a list, tuple or
any array-like object into the array() method, 
and it will be converted into an ndarray:
"""
import numpy as np
data = np.array((1, 2, 3, 4))
print(data)
print(type(data))

# 0-D Arrays
import numpy as np
data = np.array(1)
print(data)

# 1-D Arrays
import numpy as np
data = np.array([1, 2, 3, 4])
print(data)

# 2-D Arrays
import numpy as np
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(data)

# 3-D arrays
import numpy as np
data = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(data)

# Check how many dimensions the arrays have:
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

"""
Higher Dimensional Arrays
An array can have any number of dimensions.
When the array is created, you can define the number of dimensions by using the ndmin argument.
"""
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=8)
print(arr)
print('number of dimensions :', arr.ndim)

# Access Array Elements
import numpy as np
data = np.array([1, 2, 3, 4])
print(data[2])
print(data[1] + data[3])

# Access 2-D Arrays
import numpy as np
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(" 3 element of 2 rows", data[1,2])

# Access 3-D Arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Negative Indexing
# Use negative indexing to access an array from the end.
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Slicing arrays
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7])
print(data[1:5])
print(data[2:])
print(data[:3])
print(data[-2:-1])

# STEP
# Use the step value to determine the step of the slicing:
print(data[1:5:2])
print(data[::2])

# Slicing 2-D Arrays
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])

"""
Data Types in NumPy
The NumPy array object has a property called 
dtype that returns the data type of the array:
"""
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Get the data type of an array containing strings:
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# Creating Arrays With a Defined Data Type
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
arr = np.array([1, 2, 3, 4], dtype='i')
print(arr)
print(arr.dtype)

"""
Converting Data Type on Existing Arrays
Change data type from float to integer by using 'i' as parameter value:
"""
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# NumPy Array Copy vs View
# Make a copy, change the original array, and display both arrays:
import numpy as np
data = np.array([1, 3, 5, 9])
a = data.copy()
data[1] = 25
print(data)
print(a)

# Make a view, change the original array, and display both arrays:
import numpy as np
data = np.array([1, 3, 5, 9])
a = data.view()
data[1] = 25
print(data)
print(a)

# Make a view, change the view, and display both arrays:
import numpy as np
data = np.array([1, 3, 5, 9])
a = data.view()
a[2] = 45
print(data)
print(a)

# Check if Array Owns its Data
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

# Shape of an Array
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# Reshape From 1-D to 2-D
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
a = data.reshape(2, 4)
print(a)

# Reshape From 1-D to 3-D
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
a = data.reshape(2, 3, 2)
print(a)

# Returns Copy or View?
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(data.reshape(2, 4).base)

"""
Flattening array means converting a multidimensional array into a 1D array.
We can use reshape(-1) to do this.
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

# Iterating Arrays
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for x in data:
    print(x)

# Iterating 2-D Arrays
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(arr)

# Iterate on each scalar element of the 2-D array:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)

# Iterating 3-D Arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using nditer()
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types
import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Enumerated Iteration Using ndenumerate()
# Enumerate on following 1D arrays elements:
import numpy as np
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Enumerate on following 2D array's elements:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Joining NumPy Arrays
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Join two 2-D arrays along rows (axis=1):
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# Joining Arrays Using Stack Functions
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# NumPy provides a helper function: hstack() to stack along rows.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

# NumPy provides a helper function: vstack()  to stack along columns.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)

# Splitting NumPy Arrays. We use array_split() method
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
newdata1 = np.array_split(data, 3)
newdata2 = np.array_split(data, 5)
""" newdata3 = np.split(data, 5) 
Note: We also have the method split() available but it will not adjust the elements 
when elements are less in source array for
splitting like in example above, array_split() 
worked properly but split() would fail.
"""
print(newdata1)
print(newdata2)
# print(newdata3)

# Access the splitted arrays:
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
newdata = np.array_split(data, 4)
print(newdata[0])
print(newdata[1])
print(newdata[2])
print(newdata[3])

# print(newdata[0])
import numpy as np
data = np.array([[1, 2], [3, 4], [5, 6]])
newdata = np.array_split(data, 2)
print(newdata)

# The example below also returns three 2-D arrays, but they are split along the row (axis=1).
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# An alternate solution is using hsplit() opposite of hstack()
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

"""
Note: Similar alternates to vstack() and dstack() 
are available as vsplit() and dsplit().
"""

# Searching Arrays
# To search an array, use the where() method.
# Find the indexes where the value is 4:
import numpy as np
data = np.array([1, 2, 3, 3, 4, 3, 5, 3])
newdata = np.where(data == 3)
print(newdata)

# Find the indexes where the values are even:
import numpy as np
data = np.array([1, 2, 6, 3, 4, 8, 5, 3])
newdata = np.where(data%2== 0)
print(newdata)

# Find the indexes where the values are odd:
import numpy as np
data = np.array([1, 2, 6, 3, 4, 8, 5, 3])
newdata = np.where(data%2== 1)
print(newdata)

"""
The searchsorted() method is assumed to be used on sorted arrays.
Find the indexes where the value 5 should be inserted:
"""
import numpy as np
data = np.array([1, 2, 6, 3, 4, 8, 5, 3])
newdata = np.searchsorted(data, 5)
print(newdata)

# Search From the Right Side use side='right'
import numpy as np
data = np.array([6, 7, 8, 9])
newdata = np.searchsorted(data, 7, side='right')
print(newdata)

# To search for more than one value, use an array with the specified values.
# Find the indexes where the values 2, 4, and 6 should be inserted:
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

# Sorting Arrays we use sort() method
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

# Sort the array alphabetically:
import numpy as np
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

# Sort a boolean array:
import numpy as np
arr = np.array([True, False, True])
print(np.sort(arr))

# Sort a 2-D array:
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
newarr = np.sort(arr)
print(newarr)

# Filtering Arrays
# In NumPy, you filter an array using a boolean index list.
import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# Create a filter array that will return only values higher than 42:
import numpy as np
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Creating Filter Directly From Array
import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
