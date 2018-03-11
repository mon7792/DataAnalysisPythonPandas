import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# make the graph more applealing
from matplotlib import style
style.use('ggplot')

web_stats = { 'Day' : [1,2,3,4,5,6],
                'Visitors' : [43, 53, 34, 45, 64, 34],
                'Bounce_Rate':[65,72,62,64,54,66]}

# Create a data frame
df = pd.DataFrame(web_stats)

# set index to dataframe
# print(df.set_index('Day'))

# store the data frame in new variable
df2 =  df.set_index('Day')



print(df2.head())

# reference a multiple column
print(df2['Visitors'])
print(df2[['Bounce_Rate','Visitors']])

# convert single column to list

print(df2['Visitors'].tolist())

# Numpy is required to convert the multi dimentional array to
print(np.array(df2[['Bounce_Rate','Visitors']]))

# Store the np array data into new data frame

df3 = pd.DataFrame(np.array(df2[['Bounce_Rate','Visitors']]))
print("DF3")
print(df3.head())
