# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:29:17 2023

@author: dorothy
"""

"""
This assignment is to apply three types of visualisation methods (graphs) to
 extract meaningful information from data on the average annual wages of 
 graduates in the UK by ages and highest qualifications.
"""

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading the data graduate annual gross wage file as a dataframe

grad_annual_wage = pd.read_csv('Grad_AnnualGrossWage_ByAge.csv')
print(grad_annual_wage)
print(grad_annual_wage.describe())


# Transposing graduate annual gross wage file and printing

t_grad_annual_wage = grad_annual_wage.transpose()
print(t_grad_annual_wage)


