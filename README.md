# Diaspora Data
This repository collects diaspora data and related visualization.

I will add to this as my own use cases increase and I understand the data better.

Project #1 - Visualizing United States (US) Diaspora data

1. B05006 Place of Birth for the Foreign-Born Population (Diaspora data)

The United States Census Bureau releases [B05006 Place of Birth for the Foreign-Born Population](https://data.census.gov/table/ACSDT5YSPT2021.B05006?q=Place%20of%20Birth&t=-04&g=010XX00US$0600000). You can download the raw data from that link or use the use modified CSV file [slightly modified csv file](data/B05006Raw.csv) I modified GEO_ID column to remove the a prefix as well as pad any codes with only 9 digits with a leading zero so all GEO_IDs are 10 digits long so they can be easily joined later.

Note: If you are looking at broader race like Asian, instead of individual countries of origin, like Thailand, census does have that down to the census block level as can be seen [here](https://bestneighborhood.org/race-in-los-angeles-ca/). However, you gain the detail at smaller units but lose the ability to be able to seperate out the country of origins.

2. TIGER/Line Shapefiles (Geo Data)

Because "B05006 Place of Birth for the Foreign-Born Population" is indexed by GEO_ID column, we need to join this with the Census Bureau's [TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2021.html#list-tab-790442341). The shape files on the server are broken into small files, I extracted all the shp files, loaded them into QGIS program and exported the entire US Census County Divisions data into one file, you can download that [here](data/merged2021.7z).  Unzipped, the file is quite large (800MB) and will need a computer with enough CPU and RAM to handle. 

3. Generate Country based Diaspora Data (Diaspora data)

  * This intrim step involvoes opening the B050056Raw.csv file in Excel
  * Filter by POPGROUP column, which is Race/Ethnic Group, e.g. a value of 16 means "Chinese alone"
  * Export that as a CSV file [example](data/Japanese.csv)

4. Combine country based diaspora data with Geo Data

Because GeoJson data (what we obtained in step 2) is what Google Map works with, we need to add the country and population data. Since we already separated the Diaspora data by country, we can generate now country based GeoJson data to be fed into Google Map.

Claude.ai helped me write a Python script to match/filter the country based diapora data with the GeoJson data, it is [here](data/importjson.py)
The output is something like this [example](data/Japanese.geojson)

5. Display country based diaspora data with Google maps

Claude.ai also helped me to plot the geoJson file generated in the last step in Google Maps, with ability to mouse over individual blocks and see the : [running example](https://rdai.github.io/DiasporaData/) [code](index.html)



