import math
from math import sqrt

# 我的学号是03163079
numberSushuSet = set()  # 创建空集合
dictabc = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
           'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
           'z': 25}
dicttrans = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
             12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w',
             23: 'x', 24: 'y', 25: 'z'}


# di = {}
# j = 0
# for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#           'w', 'x', 'y', 'z']:
#     di.update({i: j})
#     j += 1
#
# print(di)


def getsushu():
    # 生成素数
    # 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
    for i in range(2, 102):
        if (i % 2 != 0):
            i = i
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                numberSushuSet.add(i)


def findsushu(number):
    numberSushuSet.add(number)  # 用集合排序
    li = list(numberSushuSet)  # 列表索引离他最近的素数
    indexnumber = li.index(number)
    if abs(li[indexnumber - 1] - number) < abs(li[indexnumber + 1] - number):
        return li[indexnumber - 1]
    else:
        return li[indexnumber + 1]


number = input("输入你的学号:")
number = int(number[-2] + number[-1])
getsushu()
k2 = findsushu(number)
k1 = number
stringlist = list(input("请输入要加密的字符串:"))

stringNumber = ''
for i in stringlist:
    result = dictabc[i] * k2 + k1
    transNumber = int(math.fmod(result, 26))
    print(transNumber)
    stringNumber = stringNumber+str(transNumber)

print(stringNumber)
