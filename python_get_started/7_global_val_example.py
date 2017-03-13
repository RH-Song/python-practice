a = None
def fun():
    global a
    a = 20
    return a+20

print fun()
print a
