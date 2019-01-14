import re
import re
r = re.compile(r'i love you')
test = '''hello i love you ,\n
hi i love you,\n
welcome to here,i love you'''
print(test)
result = r.findall(test)
print(result)