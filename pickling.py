# program to store the content thats loaded from various server
#into a local binary file knows as pickle

import pandas as pd
import quandl
import pickle

house_data_list = ['GICHSGFIN','GANESHHOUC','IBULHSGFIN']

#store the api key in the text file
api_key  = open('apiKey.txt','r').read()
#
# df = quandl.get("NSE/GICHSGFIN", authtoken=api_key)
# print(df['Open'].head())

# create a main dataframe which will store all the queried dataframe

def grab_initial_state():
    main_df = pd.DataFrame()
    for data in house_data_list:
        print(data)
        # Build a query
        query = "NSE/" + str(data)
        print(query)

        # Create a dataframe from the above query to quandl database
        df = quandl.get(query, authtoken=api_key)
        df = df[['Close']]
        df.columns = [data]
        print(df.head())
        print("..........................")



        # start the join process
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how="inner")


    print(main_df.head())

    pickle_out = open('quandl.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# grab_initial_state()


pickle_in = open('quandl.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)
