# 生成一个随机矩阵
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 引入Dirac Delta function函数
from sympy import DiracDelta
from numpy import linalg as LA
def p(miu,n,w):
    sum = 0 
    for i in range(n):
        temp = miu - w[i]
        temp = DiracDelta(temp)
        sum = sum + temp
    return sum / n
n = 100
x = np.round(np.random.normal(0, 1, n*n), 2) 
M = x.reshape([n,n])
M = np.triu(M)
M += M.T - np.diag(M.diagonal())
print(M)
w, v = LA.eig(M)
print(w)
#d = DiracDelta(0) / 100
#print(p(0.3,n,w))
for j in [ i/(10**8) for i in range(10**8)]:
    a = p(j,n,w)
    if a != 0:
        print(a)