# zip
a = [1,2,3]
b = [4,5,6]
lz = list(zip(a,b))
print lz

# lambda
l = lambda x,y:x + y
print l(1,2)

# map
def fun(x,y):
    return x+y
print fun(1,2)
lm = list(map(fun,a,b))
print lm
