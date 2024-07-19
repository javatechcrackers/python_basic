import numpy as np

n1 = np.array([1,2,3,4])
n2 = np.array([5,6,7,8])

print(np.vstack((n1, n2)))

print(np.hstack((n1,n2)))

print(np.column_stack((n1, n2)))