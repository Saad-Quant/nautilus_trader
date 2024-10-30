#Databento to csv conversion
import databento as db
import pandas as pd

dbn_file_path = './glbx-mdp3-20190821-20240820.ohlcv-1m_v2.dbn'
# output_csv_path = './nq_futures_data.csv'

# Open the DBN file
dbn = db.DBNStore.from_file(dbn_file_path)

metadata = dbn.metadata
print(f"Dataset: {metadata.dataset}")
print(f"Schema: {metadata.schema}")
print(f"Start: {metadata.start}")
print(f"End: {metadata.end}")

# Read the data into a pandas DataFrame
df = dbn.to_df()
#df.to_csv("./Nasdaq_1min_check.csv")
df
#=================================

#Csv data prerpocessing

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
