import random
def suiJi():
    x = random.randint(48,122)
    if x>=58 and x<=64:
        x = x+7
    elif x>=91 and x<=96:
        x = x+6
    return chr(x)
l = [suiJi(),suiJi(),suiJi(),suiJi()]
l = ''.join(l)
print('验证码:%s'%l)
