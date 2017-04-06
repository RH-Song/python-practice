import numpy as np

a = np.array([2,23,4],dtype=np.int)
print a.dtype
print a

b = np.array([[1,3,5],
    [2,4,6]])
print b

c = np.zeros((3,4))
print c

d = np.ones((4,5))
print d

e = np.arange(1,20,2)
print e

f = np.arange(12).reshape((3,4))
print f

g = np.linspace(1,10,6).reshape((2,3))
print g
