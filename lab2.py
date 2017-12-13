from scipy import stats
import numpy as nm
from math import sqrt

# take arrays
with open('vpp_y.txt') as file:
    a1 = [row.strip() for row in file]

y = []
for i in a1:
    y.append(float(i))

with open('ors_x1.txt') as file:
    a2 = [row.strip() for row in file]

x1 = []
for i in a2:
    x1.append(float(i))

with open('k_x2.txt') as file:
    a3 = [row.strip() for row in file]

x2 = []
for i in a3:
    x2.append(float(i))

# A

print('Correlation coefficient', stats.pearsonr(y, x1)[0])
print('Correlation coefficient', stats.pearsonr(y, x2)[0])

# B

# creating X matrix
X = []
for i in range(len(x1)):
    X.append([])
    X[i].append(1)
    X[i].append(x1[i])
    X[i].append(x2[i])

X = nm.array(X)
print('\nX = ')
print(X)

XT = X.T

print('\n(XT*X)^(-1) = ')
X = nm.linalg.inv(nm.dot(XT, X))
print(X)

a = nm.dot(nm.dot(X, XT), y)
print('\nbt =',a)

ny = []
for i in range(len(y)):
    ny.append(a[0] + a[1] * x1[i] + a[2] * x2[i])

print('\nresult_y:', ny)

print('R^2 = ', nm.var(ny)/nm.var(y))

J = 0
for i in range(len(y)):
    J =+ pow(y[i]-ny[i],2)
print('J = ', J)

oe = sqrt(J/(len(y)-3))

print('t = [',end = ' ')
for i in range(len(a)):
    print(a[i]/(oe*X[i][i]),end=' ')
print(']')


