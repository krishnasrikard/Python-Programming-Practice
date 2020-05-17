# Source: https://www.johndcook.com/blog/2015/08/04/last-digits-fibonacci-numbers/

from sympy import fibonacci as f
import numpy as np
import matplotlib.pyplot as plt

def period(b):
    for i in range(1, b*b+1):
        if f(i)%b == 0 and f(i+1)%b == 1:
            return(i)

n = np.arange(100)
Period = np.zeros(n.shape)

for i in range(n.shape[0]):
	Period[i] = period(n[i])

plt.plot(n, Period)
plt.grid()
plt.title('Period of $F_{i} \equiv$ p $mod(n)$')
plt.xlabel('n')
plt.ylabel('Period')
plt.show()
