##for i in range(2,1000):
##   for j in range(2,i):
##      if(i%j==0):
##         break
##   else:
##      print(i,end=' ')
##





##from math import sqrt
##import time
##start = time.time()
##for i in range(2,100000):
##    for j in range(2, int(sqrt(i) ) + 1):
##        if i % j == 0:
##            break
##    else:
##       print(i)
##end = time.time()
##print(end-start)



from math import sqrt
import time
start = time.time()
count=0
for i in range(2,110):
   if (i%2 != 0):
      i = i
      for j in range(2, int(sqrt(i) ) + 1):
         if i % j == 0:
            break
      else:
         print(i)
         count+=1
end = time.time()
print(end-start)
print(count)
