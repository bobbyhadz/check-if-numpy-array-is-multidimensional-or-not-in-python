# How to check if a NumPy Array is multidimensional or 1D

import numpy as np

arr1 = np.array([2, 4, 6, 8])
print(arr1.ndim)  # 👉️ 1

print('-' * 50)

if arr1.ndim == 1:
    # 👇️ this runs
    print('The array is one-dimensional')
else:
    print('The array is multidimensional')

print('-' * 50)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.ndim)  # 👉️ 2