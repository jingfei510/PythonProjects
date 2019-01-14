class Person:
    __name = 'bob'

p = Person()
#p.__name
#p.getname()
p._Person__name

class TrueFather:
    money = 1000
    __name = 123
    __privateMoney = 0
    def fanc(self):
        print('I can drive a car!')

f = TrueFather()
print(f._TrueFather__privateMoney)