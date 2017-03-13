list_int = [1,2,2,2,3,3,4,4,5,5,6]
s = set(list_int)
s.add(7)
s.remove(1)
print s
# remove a non exist member, will produce an exception
# s.remove(10)

s.discard(3)
# discard a nonexist member, it is ok.
s.discard(10)
print s
s.clear()
print s
