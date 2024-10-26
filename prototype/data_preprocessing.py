
import pandas as pd
data = pd.read_csv("Nasdaq_1min_dbn.csv")
def extract_date(x):
    return x[0:10]
def extract_time(x):
    return x[11:19]
data = data[~data['symbol'].str.contains("-")] # Removing spreads

data['Date'] = data['ts_event'].apply(extract_date)
data['Time'] = data['ts_event'].apply(extract_time)
data['Date'] = pd.to_datetime(data['Date'])

data=data.sort_values(by=['ts_event','symbol']).reset_index(drop=True) # Removing other contracts data by intelligently sorting
data = data.drop_duplicates(subset=['ts_event']).reset_index(drop=True)
data
