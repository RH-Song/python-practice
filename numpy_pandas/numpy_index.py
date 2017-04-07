import numpy as np

A = np.arange(3,15).reshape((3,4))
print A
print A[2]
print A[2][1]
print A[2,1]

print A[2,:]
print A[1,1:3]

for column in A.T:
    print column
    print "Good"

print A.flatten()
for item in A.flat:
    print item
