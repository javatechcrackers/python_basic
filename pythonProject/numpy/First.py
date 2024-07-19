import numpy as np

l1 = [1,2,3,4]
n1 = np.array(l1)

print(type(n1))
print(n1)

n2 = np.array([[1,2,3,4],[5,6,7,8]])
print(n2)
print(type(n2))

#create an array
n3 = np.zeros((5,5))
print(n3)

n4 = np.full((2,2), 10)
print(n4)

#initialize array within a range
n5 = np.arange(10,20)
print(n5)

#initialize array within a range with gap of 10
n6 = np.arange(10,200, 10)
print(n6)