import numpy as np

a = np.array([1,2,3])
print "a ",a

b = np.array([4,5,6])
print "b ",b

c = a+b
print "c ",c

e = a-b
print "e ",e

d = a*b
print "d ",d

f = a**2
print "a^2: ",f

g = np.sin(a)
print "sin a: ",g

print "a = 3: ",a==3

# matrix
h = np.array([[1,2],
    [3,4]])
i = np.array([[2,2],
    [2,2]])
print "h ",h
print "i ",i

j = h*i
print "h*i: ",j

l = np.dot(h,i)
m = h.dot(i)
print "h dot i: \n"
print l
print m

print "sum of h: ",np.sum(h)
print "min of h: ",np.min(h)
print "max of h: ",np.max(h)
print "sum of h row: ",np.sum(h,axis=0)
print "sum of h columns: ",np.sum(h,axis=1)
