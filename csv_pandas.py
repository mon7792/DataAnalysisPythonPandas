import pandas as pd
import matplotlib.pyplot as plt

# read from the csv file
df = pd.read_csv('ZILLOW-N12_MLPF3B.csv')
print(df.head())

# Set the index and save the data to new csv file
df.set_index('Date', inplace=True)
df.to_csv('newcsv1.csv')


# Read from csv
df = pd.read_csv('newcsv1.csv')
print(df.head())

# Read from csv and set the index
df = pd.read_csv('newcsv1.csv', index_col=0)
print(df.head())

#Rename the column and , Remember: the index is not included
df.columns = ['Austin_HPI']
print(df.head())

# Save the csv file without header
df.to_csv('newcsv3.csv', header=False)

# Add column header to csv file without the csv
df = pd.read_csv('newcsv3.csv', names = ['Date', 'Austin_HPI'])

# Convert csv file to html

df.to_html('example.html')

# rename the single column
df.rename(columns={'Austin_HPI':'54781'}, inplace=True)
print(df.head())
