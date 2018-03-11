#code to introduce to basic pandas
#import the libraries
import pandas as pd
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib as style


#start date and end date datetime

start = datetime.datetime(2010, 1 , 1)
end = datetime.datetime(2015, 8, 22)

#Create a dataframe consist of EXXOM from yahoo data api from the web

df = web.get_data_yahoo("XOM", start, end)

# print dataframe

print(df.head())

df['High'].plot()
plt.legend()
plt.show()
