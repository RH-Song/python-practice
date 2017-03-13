a = [1,3,2,4,6,5]

a.append(0)
# insert(index, val)
a.insert(1,0)
# remove(val) remove the value at the first time
a.remove(2)

print a
print a[0]
print a[-1]
print a[0:3]
print a[3:5]
print a.index(5)
print a.count(1)

a.sort()
print a
a.sort(reverse=True)
print a
