# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:33:37 2016

@author: Z
"""

import numpy as np
import matplotlib.pyplot as plt

t = 200
dt = 20
i = np.arange(0,50, dtype=np.float)
# i = [0,1,2...,49]

k_b = 1.381e-23

n = np.exp(-i*dt/t)
# n = exp(-i*k_b*dt/k_b*t)

np = n/sum(n)
E = k_b*n*i*dt
E_all = k_b*t
Ep = E/E_all


plt.plot(i*dt,np*100)
plt.xlabel('Energy')
plt.ylabel('N %')
plt.title('Population of states')
plt.show()

plt.plot(i*dt,Ep*100)
plt.xlabel('Energy')
plt.ylabel('E %')
plt.title('Distribution of energy over the states')
plt.show()

print np*100
print Ep*100
