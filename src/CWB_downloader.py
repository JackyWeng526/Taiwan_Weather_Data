#%% 
# Import pakages
import pandas as pd
import numpy as np
import datetime
import json
import urllib
import os

# Connect to path direction
BATH_PATH = os.path.dirname(os.path.abspath(__file__))
etc_PATH = os.path.join(BATH_PATH, "..", "etc")
data_PATH = os.path.join(BATH_PATH, "..", "data")

# Import station information of Central Weather Bureau Taiwan
CWB_meta = json.load(open(os.path.join(etc_PATH, "CWB_meta.json")))
CWB_meta_df = pd.DataFrame.from_dict(CWB_meta[0])
CWB_meta_df

# %% 
# Gather hourly historical data of Taipei station
# Extract station number, station name, and datetime (Mandarin characters must be transcoded twice with urllib)
stnum = CWB_meta_df.iloc[4, 0]
stname = urllib.parse.quote(urllib.parse.quote(CWB_meta_df.iloc[4, 1]))
date = datetime.date(2020, 1, 1)

# Take 2020-01-01 as example
html_data = pd.read_html(F"https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={stnum}&stname={stname}&datepicker={date}")
data_table = html_data[1]
data_table

# %%
# Drop duplicate columns
data_table.columns = [i[2] for i in np.array(data_table.columns)]

# Insert datetime value
data_table.insert(loc=0, column="Date", value=date)
data_table

# %% 
%%time
# Use for-loop to download daily historical data of Taipei station
cwb_data = []
date_start = datetime.date(2020, 1, 1)
for i in range(366):
    date = date_start + datetime.timedelta(days=i)
    html_df = pd.read_html(F"https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker={date}")[1]
    html_df.columns = [i[2] for i in np.array(html_df.columns)]
    html_df.insert(loc=0, column="Date", value=date)
    cwb_data.append(html_df)
_df = pd.concat(cwb_data, axis=0)
_df

# %% 
# Save dataframe as csv file for advanced analysis and application
_df.to_csv(os.path.join(data_PATH, "Taipei_2020.csv"))
print("Taipei weather data in 2020 has been saved!")
# %%
