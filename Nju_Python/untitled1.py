# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:05:58 2016

@author: Z
"""

def my_power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s
    
print my_power(3,3)