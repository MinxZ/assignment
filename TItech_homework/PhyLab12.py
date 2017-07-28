# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:50:13 2016

@author: Z
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

t = np.array([22,25,28,31,34,37,40,43,46,50])

tt = 1/(t+273.15)
#tt = tt*10000
tt = tt[::-1]

ct = np.array([2329,1901,1701,1541,1391,1241,1102,1001,901,785])
ct = ct[::-1]
ct = np.log10(ct)

t = np.array([232,-196,100,326])
v = np.array([11.0014,-5.5,4.2313,16.154])
tt = v/t

coefs = poly.polyfit(t, tt, 1)
ffit = poly.polyval(t, coefs)
print(coefs )
plt.plot(t, ffit)
plt.plot(t,tt)