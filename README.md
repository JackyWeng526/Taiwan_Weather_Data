# Taiwan Weather Data Downloader
Download Taiwan local weather data for advanced analysis and application.

## Instal packages and libraries
Install python libraries with requirements.txt in src folder.

```bash
  pip install -r requirements.txt
```

## Weather Station Information
You can reach the information table of CWB stations on [CWB e-service](https://e-service.cwb.gov.tw/wdps/obs/state.htm).

Get the station number and the station name you need.
![information table](https://github.com/JackyWeng526/Taiwan_Weather_Data/blob/main/docs/station_info_table.PNG)

## Read hourly weather data
Take the date-time, station number and the station name with the url below.

Then, you will gather the data of 2020-01-01 at Taipei station.
* The Mandarin characters in the station name must be transcoded twice with urllib.

```bash
  stnum = "466920"
  stname = urllib.parse.quote(urllib.parse.quote("臺北"))
  date = datetime.date(2020, 1, 1)
  altitude = "1017.5m"
  
  html_data = pd.read_html(F"https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={stnum}&stname={stname}&datepicker={date}&altitude={altitude}")
```
![hourly data](https://github.com/JackyWeng526/Taiwan_Weather_Data/blob/main/docs/Taipei_weather_data_20200101_table.PNG)

## Gather annual data
Use a for-loop to download the rest data of 2020.
![annual data](https://github.com/JackyWeng526/Taiwan_Weather_Data/blob/main/docs/Taipei_weather_data_2020_table.PNG)

Check the weather data with a chain chart.
![chain chart](https://github.com/JackyWeng526/Taiwan_Weather_Data/blob/main/docs/Taipei_weather_data_plot.PNG)

Now, you have the hourly data of 2020 at Taipei for analysis and advanced application to other fields.

## Author
[@Jacky Weng](https://github.com/JackyWeng526)

## Reference
[CWB Observation Data Inquire System](https://e-service.cwb.gov.tw/HistoryDataQuery/).
