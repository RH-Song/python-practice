import copy
a = [1,2,3]
b = a
# id is the same for one thing
print 'id of a',id(a)
print 'id of b',id(b)

# when the id is the same, if I change a, b will be changed 
a[1] = 22
print 'We have change a[1] into 22'
print a
print b

# copy
c = [1,2,[3,4]]
d = copy.copy(c)
print 'id of c',id(c)
print 'id of d',id(d)

print 'But the list in list c wasn\'t copied'
print 'id of c[2] ',id(c[2])
print 'id of d[2] ',id(d[2])

# deep_copy
e = copy.deepcopy(c)

print 'id of c',id(c)
print 'id of e',id(e)
print 'The c has been totally copied'
print 'id of c[2] ',id(c[2])
print 'id of e[2] ',id(e[2])
