#%% Import pakages
import pandas as pd
import json
import os

# Create path and list website link
BATH_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BATH_PATH, "..", "data")
webpage = "https://e-service.cwb.gov.tw/wdps/obs/state.htm"


# %% Read webpage
# Read html content as DataFrame
read_html = pd.read_html(webpage)
html_table = read_html[0] # Another table is for removed stations.

# Extract columns of station number, station id, altitude (meter), city, lontitude, latitude, and station address
html_df = html_table.loc[:, ["站號", "站名", "海拔高度(m)", "城市", "經度", "緯度", "地址"]]
html_df.dropna(inplace=True)
display(html_df)


# %% Save as csv file 
html_df.to_csv(os.path.join(DATA_PATH, "CWB_meta.csv"))


# %% Save as json file
html_dict = html_df.to_dict()
display(html_dict)

# Decode Mandarin characters 
with open(os.path.join(DATA_PATH, "CWB_meta_decode.json"), "w", encoding="utf-8") as f:
    json.dump([html_dict], f, ensure_ascii=False)

# For Ascii of Mandarin characters
with open(os.path.join(DATA_PATH, "CWB_meta.json"), "w", encoding="utf-8") as f:
    json.dump([html_dict], f)
