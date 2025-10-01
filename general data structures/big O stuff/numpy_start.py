import numpy as np

aray = np.array([0,1,2,3,4,5,6,7,8,9])
print(aray)
ranged = np.arange(0,10)
print(ranged)
denanda = np.zeros(100)
print(denanda)
other = denanda.copy()
print(other)
other[len(other)-1] = 1
print(other)
sliced = ranged[1:6]
print(sliced)