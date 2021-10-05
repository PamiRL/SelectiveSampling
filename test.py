import numpy as np

arr = np.ones((100,2))
for i in range(100):
    value = np.random.randn(2)
    arr[i] = value
# print(arr)