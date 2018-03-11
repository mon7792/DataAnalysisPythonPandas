import quandl
import pandas as pd

api_key = open('apiKey.txt','r').read()
df = quandl.get("NSE/GICHSGFIN", authtoken=api_key)

print(df.head())
