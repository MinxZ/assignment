# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:05:03 2016

@author: Z
"""
import numpy as np

h = 6.626e-34 # J s
c = 2.998e8 # m/s
e = 1.602e-19 # c
m_e = 9.1094e-31 # kg
e_0 = 8.8542e-12 # epicilon
N_a = 6.02e23 # Na
f = 1.602*10**(-19)
k_b = 1.38e-23

def E(lamda):
    J = h*c/(lamda*10**(-9))
    eV = J/f
    print(J,'J',eV,'eV')

def lam(eV):
    l = h*c/(eV*10**(-9)*f)
    print(l)

def E_n(n):
    E_n = -((m_e*e**4)/(8*e_0**2*h**2))*(1/n**2)
    print(E_n,E_n*N_a/1000,'KJ/mol')

def de(e,l):
    l = l*10**(-10)
    de = ((e+1)*(h**2)/(8*m_e*l**2*f))
    print(de)

l = 7.4e-10
m = 1/N_a/1000
n = (0.5*k_b*300*8*m*l**2/h**2)**0.5

n2 = n**2

nn = np.array([1,2,3,4,5,6,7,8,9,10])
nn = nn**2
nn3 = []
for i in [0,1,2,3,4,5,6,7,8,9]:
    for j in [0,1,2,3,4,5,6,7,8,9]:
        #for k in [0,1,2,3,4,5,6,7,8,9]:
            nnn = nn[i]+nn[j]
            if  13<nnn<20:
                print nnn,i+1,j+1
                
print n2        

      

            
