# Program to give a comparison operator

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

#intial bridge reading
bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
df = pd.DataFrame(bridge_height)
print(df)

#bridge standard deviation reading
df['STD'] = df['meters'].rolling(window=2).std()
print(df)

print("......")
#store the standard deviation of the meters column in the df_std
#It will be used for calculations
df_std = df.describe()
print(df_std['meters']['std'])
df_std = df_std['meters']['std']
# print(type(df_std['meters']['std']))
# use comparison operator to remove the outlier

df = df[(df['STD']<df_std)]

print(df)

df['meters'].plot()
plt.show()


#
# df.plot()
# plt.show()
