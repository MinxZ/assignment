# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:28:16 2016

@author: Z
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

t = np.array([22,25,28,31,34,38,40,44,47,50])
cr = np.array([6.80,6.90,7.00,7.00,7.10,7.27,7.32,7.42,7.48,7.59])
cr -= 0.19


plt.plot(t,cr)
coefs = poly.polyfit(t, cr, 1)
ffit = poly.polyval(t, coefs)
print(coefs )
plt.plot(t, ffit)