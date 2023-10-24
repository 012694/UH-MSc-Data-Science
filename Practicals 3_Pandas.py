# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:51:24 2023

@author: dorot
"""

# importing libraries

import pandas as pd
import matplotlib.pyplot as plt


# reading csv file into a pandas data frame

top10_countries = pd.read_csv('countries_top10.csv')

#print(top10_countries)

pdf_top10_countries = pd.DataFrame(data= top10_countries, columns= ('Country', 
                                                                        'Population', 'Area', 'GDP'))
print(pdf_top10_countries)

# creating new columns population per km2 and GDP per head

pdf_top10_countries['Pop/km2'] = pdf_top10_countries['Population']/ pdf_top10_countries['Area']
pdf_top10_countries['GDP/Pop'] = pdf_top10_countries['GDP'] / pdf_top10_countries['Population']

#new_top10_countries = pd.DataFrame(data=top10_countries, columns=('Country', 
                                                                    #  'Pop/km2', 'GDP/Pop'))
print(pdf_top10_countries.head())


# doing the second question

# reading the GDP 2015 dollars file

GDP_dollar = pd.read_csv('GDP_2015dollars.csv')
#print(GDP_dollar)

# plotting the data as four time series

plt.figure()

plt.plot(GDP_dollar['Year'], GDP_dollar['China'], label = 'China')
plt.plot(GDP_dollar['Year'], GDP_dollar['Germany'], label = 'Germany')
plt.plot(GDP_dollar['Year'], GDP_dollar['Japan'], label = 'Japan')
plt.plot(GDP_dollar['Year'], GDP_dollar['United States'], label = 'United States')

plt.xlabel('year')
plt.ylabel('GDP')
plt.legend()

plt.show()


# creating new columns by dividing gdp of countries by GDP of USA

GDP_dollar['China/USA'] = GDP_dollar['China'] / GDP_dollar['United States'] * 100
GDP_dollar['Germany/USA'] = GDP_dollar['Germany'] / GDP_dollar['United States'] * 100
GDP_dollar['Japan/USA'] = GDP_dollar['Japan'] / GDP_dollar['United States'] * 100

print(GDP_dollar.head())

# plotting the new columns as a function of time

plt.plot(GDP_dollar['Year'], GDP_dollar['China/USA'], label = 'China/USA')
plt.plot(GDP_dollar['Year'], GDP_dollar['Germany/USA'], label = 'Germany/USA')
plt.plot(GDP_dollar['Year'], GDP_dollar['Japan/USA'], label = 'Japan/USA')

plt.xlabel('year')
plt.ylabel('GDP')
plt.legend()


# extracting and printing data for the year 2011 to 2020

print(GDP_dollar.iloc[-10:])



