class Calculator:
    name = 'Raphael'
    def __init__(self,name = 'RH'):
        self.name = name
    def add(self,x,y):
        print self.name
        result = x + y
        print result

calcul = Calculator('rh')
c = Calculator()
print c.name
calcul.add(1,2)
