# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:09:48 2023

@author: dorot
"""

# importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading the file uk cities

ukcities = pd.read_csv('UK_cities.txt', sep='\s+')
print(ukcities.head())

print(ukcities.describe())


# Calculating the median and average population

ukcities_med = ukcities['Population'].median()

print('\nThe median population of uk cities is\n', ukcities_med)

ukcities_avg = ukcities['Population'].mean()
print('The average population of UK cities is', ukcities_avg)


# Calculating Pearson's and kendall's correlation

print(ukcities.corr(method='kendall'))
print(ukcities.corr())


# Creating a new columns with population in thousands

ukcities['K_Population'] = ukcities['Population'] / 1000
print(ukcities)


# using groupby to sum up populations of the different Nation/Region

sum_pop = ukcities['Population'].groupby(ukcities['Nation/Region']).sum()
print(sum_pop)

print(ukcities.columns)


# Creating new dataframes of old and new cities

old_city = ukcities[ukcities['Year granted']< 1888]
print(old_city)

new_city = ukcities[ukcities['Year granted'] > 1888]
print(new_city)


# Working on the second task
# Reading the file energy per head


energy = pd.read_csv('energy_per_head.csv')
print(energy)


# Transposing the energy per head file
t_energy = energy.transpose()
print(t_energy)


# Writing the first line containing country names into header and removing first two lines

t_energy.columns = t_energy.iloc[0]
print (t_energy)


t_energy_remove2rows = t_energy.iloc[2:]
print(t_energy_remove2rows)


# Removing NaNs for Brazil and China entries
t_energy_remove2rows = t_energy_remove2rows.dropna(subset=['China', 'Brazil'])
print(t_energy_remove2rows)


# Plotting Brazil and China agaisnt year

plt.figure()
plt.bar(t_energy_remove2rows.index[0::],t_energy_remove2rows['China'], label=('China'))
plt.bar(t_energy_remove2rows.index[0::],t_energy_remove2rows['Brazil'], label=('Brazil'))
plt.legend() 
plt.xlim(0,10)
plt.show()

#ataframe.index = dataframe.index.astype(int)
plt.figure()
plt.plot(t_energy_remove2rows.index[0::],t_energy_remove2rows['China'], label=('China'))
plt.plot(t_energy_remove2rows.index[0::],t_energy_remove2rows['Brazil'], label=('Brazil'))
plt.legend() 
plt.xlim(1,50)
plt.show()

