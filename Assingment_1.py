# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:29:17 2023

@author: dorothy
"""

"""
This assignment is applying three types of visualisation methods (graphs) to
 extract meaningful information from data on the average annual gross wages of 
 graduates in the UK in 2017 by ages and highest qualifications.
"""


# Importing the libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def grad_line_graph(df):
    
    
    """
    This function plots a line graph of the annual wages per qualifications.
    
    The function takes a dataframe and returns a line plot of the annual 
    salaries for the qualifications
    """
    

    plt.figure(figsize=(12,6))
    
    #This part of the code plots wages for all ages against each qualification
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

    # Setting the legend, title and labels for the graph
    plt.legend() 
    plt.xlabel('Ages')
    plt.ylabel('Annual Wages')
    plt.title(' Annual Wages By Ages Per Highest Qualification')
    plt.savefig('Assign1_Lineplot.png')
    plt.show()
    return 


def grad_box_plot(dt, header):

    
    """
    This function plots a box plot of all the qualifications by the ages and 
    annual wages. Function returns a box plot of annual wages for qualifications
    
    Parameter
    dt : a list of the annual wages for all qualifications over the ages
    header : the headings or labels for each qualification
    """


    plt.figure(figsize=(12,6))                             

    #Plotting the data frame against the labels
    plt.boxplot(data, labels=qualifcations)
    plt.legend() 
      
    # Setting the titles, labels and limits for the axes
    plt.ylim(10000, 40000)
    plt.title(' Box plot of Annual Wages per Highest Qualification')
    plt.ylabel('Annual Wages')
    plt.xlabel('Qualifications')
    plt.savefig('Assign1_Boxplot.png')
    plt.show()
    return


def grad_bar_plot(min_array, max_array):
    
    
    """
    This function plots a bar graph of the highest and lowest annual wages for
    each qualification. 
    
    Parameters
    min_array : an array of the minimum wages for each qualificaton
    max_array : an array of the maximum wages for each qualification
    
    """
    
    
    plt.figure(figsize=(12,6))
   
    # Setting the limits and plotting the bar graph
    plt.ylim(0,40000)
    plt.bar(qualifcations, max_array, label='Highest Salaries', width=0.5)
    plt.bar(qualifcations, min_array, label='Lowest Salaries', 
            color='brown', width=0.5)
    plt.legend()
    plt.title('Highest and Lowest Annual Wages per Qualification')
    plt.xlabel('Qualifications')
    plt.ylabel('Annual Wages')
    
    plt.savefig('Assign1_Bargraph.png')
    plt.show()
    return


# Reading my data, annual gross wage csv file as a dataframe
grad_annual_wage = pd.read_csv('Grad_AnnualGrossWage_ByAge.csv')
print(grad_annual_wage)
print(grad_annual_wage.describe())

# Transposing annual gross wage file and printing
t_grad_annual_wage = grad_annual_wage.transpose()
print(t_grad_annual_wage)


"""
Writing the first line containing qualifications into header and removing 
 first row. Setting the ages as int and not strings
"""


t_grad_annual_wage.columns = t_grad_annual_wage.iloc[0]
t_grad_annual_wage = t_grad_annual_wage.iloc[1:]
print(t_grad_annual_wage)
t_grad_annual_wage.index = t_grad_annual_wage.index.astype(int)


"""
The next part of the code will be plotting the data as three different graphs 
 to extract meaningful information.The graphs picked for visualisation are
 Line plot, Box plot and Bar graph
"""
 

# Calling the function grad_line_graph to plot the line graph  
grad_line_graph(t_grad_annual_wage)


"""
The next part of the code plots the second graph - Box plot for  all
 qualifications showing the distributions for each qualification. 
"""


# Defining values of data as wages over ages per qualification 
data = [t_grad_annual_wage['Graduates'], t_grad_annual_wage['Apprenticeship'],
       t_grad_annual_wage['A level'], t_grad_annual_wage['A* to C grade GCSE']]
  
# Defining values of header as list of headers and storing in qualifications  
qualifcations = ['Graduate', 'Apprenticeship', 'A level', 'GCSE']

# Calling the function grad_box_plot with data and qualifications
grad_box_plot(data, qualifcations)
 


"""
The third graph is a bar graph of the highest and lowest annual wages for 
 each qualification.
"""


# Calling the max() function to get the maximum wage for each qualification
graduate_max = t_grad_annual_wage['Graduates'].max()
apprentice_max = t_grad_annual_wage['Apprenticeship'].max()
a_level_max = t_grad_annual_wage['A level'].max()
GCSE_max = t_grad_annual_wage['A* to C grade GCSE'].max()

# Calling the min() function to get the minimum wages for each qualification
graduate_min = t_grad_annual_wage['Graduates'].min()
apprentice_min = t_grad_annual_wage['Apprenticeship'].min()
a_level_min = t_grad_annual_wage['A level'].min()
GCSE_min = t_grad_annual_wage['A* to C grade GCSE'].min()

# Storing the maximum and minimum annual wages are stored as arrays 
data_max = np.array([graduate_max,apprentice_max, a_level_max, GCSE_max])
data_min = np.array([graduate_min,apprentice_min, a_level_min, GCSE_min])

# Calling the function grad bar plot which takes the min and max arrays
grad_bar_plot(data_min, data_max)

