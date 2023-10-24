# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:51:37 2023

@author: dorot
"""

# importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading csv files of returns for Barclays, BP, Tesco and Vodaphone
x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 1000)

BCS = pd.read_csv('BCS_ann.csv')
BP = pd.read_csv('BP_ann.csv')
TS = pd.read_csv('TSCO_ann.csv')
Vod = pd.read_csv('VOD_ann.csv')

print(BCS)


#BCS = np.random.normal(-1.0, 1.0, 10000)
#sample2 = np.random.normal(1.0, 0.5, 10000)
#sample3 = np.random.normal(0.0, 1.5, 10000)
#sample4 = np.random.normal(-0.2, 2.0, 10000)




# plotting the returns as subplots

plt.figure()

plt.subplot(2, 2, 1)
plt.hist(BCS['ann_return'], label ='Barclays', density=True)
plt.legend()

plt.subplot(2, 2, 2)
plt.hist(BP['ann_return'], label ='BP', density=True)
plt.legend()

plt.subplot(2, 2, 3)
plt.hist(TS['ann_return'], label ='Tesco', density=True)
plt.legend()

plt.subplot(2, 2, 4)
plt.hist(Vod['ann_return'], label ='Vod', density=True)
plt.legend()

plt.show()


# plotting Barclays and BP stocks in one graph

plt.subplot(2, 2, 1)
plt.hist(BCS['ann_return'], label ='Barclays', alpha = 0.9)
plt.hist(BP['ann_return'], label ='BP', alpha = 0.3)
plt.legend()


# plotting a box plot of the returns
plt.figure()                             
data = [BCS['ann_return'], BP['ann_return'], TS['ann_return'], Vod['ann_return']]
label = ['Barclays', 'BP', 'Tesco', 'Vodaphone']
plt.boxplot(data ,labels = label )
plt.legend() 
plt.show()




# plotting graphs as pie chart

companies = ['Barclays', 'BP', 'Tesco', 'Vodaphone']
mkt_cap = np.array([33367, 68785, 20979, 29741])
plt.figure()
plt.pie(mkt_cap, labels = companies)
plt.show()



