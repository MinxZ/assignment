# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:36:54 2016

@author: Z
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

t = np.array([0,10,20,30,46,51,61])
vc = 16.21
vif = 15.81
v = np.array([8.14,8.45,8.74,9.24,10.16,10.43,10.67])

vp = np.log(vc - v)
vpi = np.log(vif - v)
coefs = poly.polyfit(t[1:], vp[1:], 1)
coefsi = poly.polyfit(t[1:], vpi[1:], 1)


plt.plot(t,vp)
plt.plot(t,vpi)

ffit = poly.polyval(t, coefs)
ffiti = poly.polyval(t, coefsi)


plt.plot(t, ffit)
plt.plot(t, ffiti)

print(vp)
print(ffit)
print(vpi)
print(ffiti)

 