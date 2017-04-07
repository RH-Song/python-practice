import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B))
print C

D = np.hstack((A,B))
print D

E = A[:,np.newaxis]
F = B[:,np.newaxis]
G = np.hstack((E,F))
print G

H = np.concatenate((A,B,A,B),axis=0)
I = np.concatenate((A,B,A,B))
print H
print I
