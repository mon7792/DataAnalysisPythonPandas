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
HPI_data['GIC']  = HPI_data['GICHSGFIN'].resample('M').mean()

# DataFrame  to store the percentage in value
# HPI = HPI_data.pct_change()

# HPI_data['GICHSGFIN'].plot()
# GIC.plot()
#
# plt.legend()
# plt.show()

print(HPI_data[['GICHSGFIN','GIC']].head())
# Processing to remove the NaN values
# HPI_data.dropna(how = 'all', inplace=True)
# HPI_data.fillna(method='bfill', inplace=True)
HPI_data.fillna(value=-999999, inplace=True)
print(HPI_data[['GICHSGFIN','GIC']].head())

#plot the values

HPI_data[['GICHSGFIN','GIC']].plot()
plt.legend()
plt.show()
