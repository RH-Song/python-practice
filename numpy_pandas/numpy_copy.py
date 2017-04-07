import numpy as np

# just copy

a = np.arange(4)
b = a
print "a ",a
print "b ",b

b[0] = 9
print "change b\n"
print "a ",a
print "b ",b

a[1] = 10
print "change a\n"
print "a ",a
print "b ",b

# deep copy

c = a.copy()

print "a ",a
print "c ",c

c[0] = 11
print "change c\n"
print "a ",a
print "c ",c

a[1] = 15
print "change a\n"
print "a ",a
print "c ",c
