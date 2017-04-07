import numpy as np

A = np.arange(2,14).reshape((3,4))

print A

print np.argmin(A)
print np.argmax(A)
print np.mean(A)
print np.mean(A,axis=0)
print np.median(A)

print np.cumsum(A)
print np.diff(A)

B = np.array([[3,0],
    [1,5]])
print B
print np.nonzero(B)
print "sort: ",np.sort(B)

C = np.transpose(B)
D = B.T
print C
print D

print np.clip(A,3,4)
