import pandas as pd


# read data from csv

main_df = pd.DataFrame()

df1 = pd.read_csv('quandl/NSE-GANESHHOUC.csv')
df1.set_index('Date', inplace = True)
print("DataFrame 1")
df1=df1[['High']]0
df1.rename(columns={'High':'GANESH'}, inplace=True)
print(df1.tail())

df2 = pd.read_csv('quandl/NSE-GICHSGFIN.csv')
df2.set_index('Date', inplace = True)
print("DataFrame 2")
df2 = df2[['High']]
df2.rename(columns={'High':'GIC'}, inplace=True)
print(df2.tail())

df3 = pd.read_csv('quandl/NSE-IBULHSGFIN.csv')
df3.set_index('Date', inplace = True)
print("DataFrame 3")
df3 = df3[['High']]
df3.rename(columns={'High':'IBUL'}, inplace=True)
print(df3.tail())


# join the data frame


main_df = df1.join(df3, how='inner')
# main_df = main_df.join(df3)
print("It..")
print(main_df)
