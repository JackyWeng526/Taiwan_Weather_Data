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


class CWB_downloader:
    def __init__(self, station_number, date_start, date_end):
        self.stn = station_number
        self.date_start = date_start
        self.date_end = date_end
        self.st_name = self.CWB_station_name()
        self.time_period = self.download_time_period()

    def CWB_station_name(self):
        # Get station name from station information of Central Weather Bureau Taiwan
        CWB_meta = json.load(open(os.path.join(etc_PATH, "CWB_meta.json")))
        CWB_meta_df = pd.DataFrame.from_dict(CWB_meta[0])
        st_name = CWB_meta_df.loc[CWB_meta_df["站號"]==self.stn, "站名"].values[0]
        return st_name

    def download_time_period(self):
        date_start = self.date_start
        date_end = self.date_end
        date_delta = (date_end - date_start).days + 1
        return date_delta

    def data_downloader(self):
        cwb_data = []
        date_start = self.date_start
        date_delta = self.time_period
        stn = self.stn
        st_name = urllib.parse.quote(urllib.parse.quote(self.st_name))
        for d in range(date_delta):
            date = date_start + datetime.timedelta(days=d)
            html_df = pd.read_html(F"https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={stn}&stname={st_name}&datepicker={date}")[1]
            html_df.columns = [i[2] for i in np.array(html_df.columns)]
            html_df.insert(loc=0, column="Date", value=date)
            cwb_data.append(html_df)
        _df = pd.concat(cwb_data, axis=0)
        print(F"{self.st_name} weather data between {self.date_start} and {self.date_end} has been downloaded!")
        return _df        

    def data_saver(self):
        _df = self.data_downloader()
        _df.to_csv(os.path.join(data_PATH, F"{self.st_name}_{self.date_start}_{self.date_end}.csv"))
        print("Weather data has been saved!")


if __name__ == "__main__":
    station_number = 466920
    date_start = datetime.date(2020, 1, 1)
    date_end = datetime.date(2020, 1, 2)
    CWB_downloader(station_number, date_start, date_end).data_saver()