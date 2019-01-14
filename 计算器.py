print('input cacl or exit')
iz = input()
while iz == 'cacl':
    print("begin input")
    x = int(input('first:'))
    o = input('operater')
    y = int(input('second:'))
    operater = {
             '+':x+y,
             '-':x-y,
             '/':x/y,
             '*':x*y
             }
    result = operater.get(o,'plaese inout +|-|/|*')
    print('result=:',result)

    

