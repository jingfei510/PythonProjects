import math
import numpy as np

y=np.matrix([[10,5,12],[3,14,21],[8,9,11]])
inv=np.linalg.inv
inv(y)#x的逆矩阵
y.I #也是x的逆矩阵
det=np.linalg.det
det(y)#行列式
m=np.dot(np.linalg.det(y),np.linalg.inv(y))#伴随矩阵
