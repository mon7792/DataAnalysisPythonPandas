# program to store the content thats loaded from various server
#into a local binary file knows as pickle

import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

house_data_list = ['GICHSGFIN','GANESHHOUC','IBULHSGFIN']

#Load dataframe from pickle
#HPI data is for the whole year.
pickle_in = open('quandl.pickle','rb')
HPI_data = pickle.load(pickle_in)


# Produce a monthly sample for the HPI data
HPI_data['GIC']  = HPI_data['GICHSGFIN'].rolling(window=12).mean()
HPI_data['GICSTD']  = HPI_data['GICHSGFIN'].rolling(window=12).std()
# print(HPI_data[['GICHSGFIN','GIC','GICSTD']].head())



#Figures matplotlib
fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)

#Obtain corellation between two different housing information

GIC_GANESH_CORELLATION = HPI_data['GICHSGFIN'].rolling(window=12).corr(HPI_data['GANESHHOUC'])
# GIC_GANESH_CORELLATION = pd.rolling_corr(HPI_data['GICHSGFIN'], HPI_data['GANESHHOUC'], 12)
print(GIC_GANESH_CORELLATION)





#plot the values
# HPI_data['GICHSGFIN'].plot(ax=ax1)
# HPI_data['GIC'].plot(ax=ax1)
# HPI_data['GICSTD'].plot(ax=ax2)
#

HPI_data['GICHSGFIN'].plot(ax=ax1)
HPI_data['GANESHHOUC'].plot(ax=ax1)
GIC_GANESH_CORELLATION.plot(ax=ax2)

plt.legend()
plt.show()
