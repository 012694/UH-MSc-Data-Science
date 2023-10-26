# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:47:50 2023

@author: dorot
"""

# importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# defining the trigon1 function


def trigon1(a, b, j, t):
    y = np.cos(a*t)-np.cos(b*t)**j

    return y

# creating the trigon2 function
def trigon2(c, d, k, t):
    y = np.sin(c*t) - np.sin(d*t)**k
    return y


# creating an array with values from 0 to 2pi as my x values
t = np.linspace(0, 2*np.pi, 1000)

# calling the function y with given values
y = trigon1(1, 60, 3, t)
z = trigon2(1, 120, 4, t)
plt.figure(figsize=(10,10))

# showing the figure
plt.plot(y, z, label='X')
plt.xlabel('X axis')
plt.ylabel('Y axis')
#plt.savefig('\Users\Desktop\MSc_Data_Science\Semester_1\Applied_Data_Science_\myfi.png')

plt.show()
