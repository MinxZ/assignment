# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:24:10 2016

@author: Z
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,2, dtype=np.float)
k1 = (-1*20.0)/200
b = np.exp(k1*a)
ab = a*b

k2 = -1/(8.617e-5*200)
state = np.exp(k2*a)
energy = np.exp(k2*a)*a


print state
print energy/sum(energy)

plt.plot(a,state)
plt.xlabel('Energy')
plt.ylabel('N')
plt.title('Population of states')
plt.show()


plt.plot(a,energy/sum(energy))
plt.xlabel('Energy')
plt.ylabel('E %')
plt.title('Distribution of energy over the states')
plt.show()
