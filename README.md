A quickly thrown together utility to visualize weather data from the canadian government.

By default it takes looks at average maximum temp for each month with a 10 year running average. Take a look in the code for how to chage this.


I used this command to get the data:
```bash
for year in `seq 1890 2018`;do for month in `seq 1 12`;do wget --content-disposition "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=4333&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" ;done;done
```

The ftp address is here:  
ftp://ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/


How-To:  

1. Downoad data into data folder
2. run format.py
3. run analyze.py