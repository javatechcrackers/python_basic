import numpy as np

n1 = np.array([10,20,30])
n1 = n1 +1
print(n1)

n2 = n1*2
print(n2)

n3 = n1-1
print(n3)

n4 = n1/2
print(n4)

print(np.mean(n3))
print(np.std(n3))
print(np.median(n3))


#save and load in file
np.save('my_numpy', n3)
n4 = np.load('my_numpy.npy')
print(n4)

