# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 10:54:40 2023

@author: dorot
"""

# importing libraries

import numpy as np
import matplotlib.pyplot as plt


# creating my x axis with range 0 to 2pi

x = np.linspace(0, 2*np.pi, 10000)


# defining my function trigon1(a, b, j)

def trigon1(a, b, j, t):
   
    y = np.cos(a*t) - np.cos(b*t)**j;

    return y

# defining the second function trigon2(c,d,k)

def trigon2(c, d, k, t):
    
    y = np.sin(c*t) - np.sin(d*t)**k
    
    return y


# calling the functions with given values

trig1 = trigon1(1, 60, 3, x)
trig2 = trigon2(1, 120, 4, x)

plt.figure()

# plotting the function

plt.plot(trig1, trig2)

         
#plt.xlim(-2.0, 2*np.pi)
plt.xlabel('X axis')
plt.ylabel('Y axis')
#plt.reshape(10,10)

plt.show()


