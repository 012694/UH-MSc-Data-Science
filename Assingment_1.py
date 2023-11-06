# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:29:17 2023

@author: dorothy
"""

"""
This assignment is to apply three types of visualisation methods (graphs) to
 extract meaningful information from data on the average annual gross wages of 
 graduates in the UK in 2017 by ages and highest qualifications.
"""

# Importing the libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Reading the annual gross wage csv file as a dataframe

grad_annual_wage = pd.read_csv('Grad_AnnualGrossWage_ByAge.csv')
print(grad_annual_wage)
print(grad_annual_wage.describe())


# Transposing annual gross wage file and printing

t_grad_annual_wage = grad_annual_wage.transpose()
print(t_grad_annual_wage)


"""
Writing the first line containing qualifications into header and
 removing first row. Setting the ages as int and not strings
"""

t_grad_annual_wage.columns = t_grad_annual_wage.iloc[0]
t_grad_annual_wage = t_grad_annual_wage.iloc[1:]
print(t_grad_annual_wage)
t_grad_annual_wage.index = t_grad_annual_wage.index.astype(int)


"""
Plotting the data as three different graphs to extract meaningful information.
 The graphs picked for visualisation are line plot, box plot and bar graph
"""
 
# Plotting the annual gross wages per qualifications by ages as a line graph

plt.figure()
plt.plot(t_grad_annual_wage.index[0::], t_grad_annual_wage['Graduates'], 
         label=('Graduate'))
plt.plot(t_grad_annual_wage.index[0::], t_grad_annual_wage['Apprenticeship'],
         label=('Apprenticeship'))
plt.plot(t_grad_annual_wage.index[0::], t_grad_annual_wage['A level'], 
         label=('A level'))
plt.plot(t_grad_annual_wage.index[0::], t_grad_annual_wage['A* to C grade GCSE'],
         label=('GCSE'))


# Setting the limits and ticks on the X axis for the graph 
plt.xlim(21, 30)
plt.ylim(10000, 40000)
x_ticks = np.arange(21, 70, 5)  
plt.xticks(x_ticks)


# Setting the legend and labels for the graph
plt.legend() 
plt.xlabel('Ages')
plt.ylabel('Annual Wages')
plt.title(' Average Salaries in UK(2017) by Ages and Highest Educ Qualification')
plt.savefig('Assign1_Lineplot.png')
plt.show()




"""
The second graph is a Box plot showing the median, modal and quartile salaries,
 for each qualification. The box plot also shows outlier salaries.
"""

# plotting a box plot of each qualification
plt.figure()                             
data = [t_grad_annual_wage['Graduates'], t_grad_annual_wage['Apprenticeship'],
        t_grad_annual_wage['A level'], t_grad_annual_wage['A* to C grade GCSE']]
       
qualifcations = ['Graduate', 'Apprenticeship', 'A level', 'GCSE']
plt.boxplot(data, labels = qualifcations )
plt.legend() 
plt.ylim(10000, 40000)
plt.title(' Box plot of Grad Salaries in UK(2017) per Highest Qualification')
plt.savefig('Assign1_Boxplot.png')
plt.show()




"""
The third graph shows the highest annual wage for each qualification as a 
bar graph. The maximum and minimum wages for each qualification is stored in a variable
"""

graduate_max = t_grad_annual_wage['Graduates'].max()
apprentice_max = t_grad_annual_wage['Apprenticeship'].max()
a_level_max = t_grad_annual_wage['A level'].max()
GCSE_max = t_grad_annual_wage['A* to C grade GCSE'].max()


graduate_min = t_grad_annual_wage['Graduates'].min()
apprentice_min = t_grad_annual_wage['Apprenticeship'].min()
a_level_min = t_grad_annual_wage['A level'].min()
GCSE_min = t_grad_annual_wage['A* to C grade GCSE'].min()


# The maximum annual wages are stored in an array as data
data_max = np.array([graduate_max,apprentice_max, a_level_max, GCSE_max])
data_min = np.array([graduate_min,apprentice_min, a_level_min, GCSE_min])


# Plotting the bar graph and adding the title

plt.figure(figsize=(7,5))

plt.ylim(0,40000)
plt.xticks(rotation=20)
plt.bar(qualifcations, data_max, label  = 'Highest Salaries', width = 0.5)
plt.bar(qualifcations, data_min, label = 'Lowest Salaries', color = 'brown', width = 0.5)
plt.legend()
plt.title('Highest and Lowest Annual Wages per Qualification')

plt.savefig('Assign1_Bargraph.png')

plt.show()





