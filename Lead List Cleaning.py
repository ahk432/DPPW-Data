import pandas as pd
import os
import numpy as np

#File Path
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")

###Cleaning

#Reading Master list
df = pd.read_excel("IEPA Lead Line Master List.xlsx", "Master List")

#Reading Public lines found through plans 
df2 = pd.read_excel("PWS Lines (Found Through Plans) (1).xlsx", "Found Lines")


#Merging two dataframes together
df3 = df.merge(df2, how = 'left')


#Dropping unnecessary columns
df3 = df3.drop(['Comments', 'Document'], axis = 1)

# New dataframe
lines = df3[['GEODBID','FEATUREID', 'Account Number', 'Meter Number',
             'Service Address', 'PWS-Owned Service Line Material', 
             'Current Customer Side Service Line Material']]

#Creating a new column that indicates 1 for when both PW and Customer lines are copper and 0 for when at least one is not
condition = (lines['PWS-Owned Service Line Material'] == 'C') & (lines['Current Customer Side Service Line Material'] == 'C')

lines['No Work'] = np.where(condition,1,0)


#Creating new dataframe for all of the mismatches (where either PW and/or customer lines are not copper)
l = lines[lines['No Work'] == 0]

l = l.drop(['No Work'], axis = 1)

#Finding all instances of U, L, and G in PWS dataframe
PWS = l.loc[(l['PWS-Owned Service Line Material'] == 'U') |
            (l['PWS-Owned Service Line Material'] == 'L') |
            (l['PWS-Owned Service Line Material'] == 'G')]

PWS = PWS.reset_index(drop = True)

#Finding all instances of U, L, and G in customer dataframe
Cust = l.loc[(l['Current Customer Side Service Line Material'] == 'U') |
            (l['Current Customer Side Service Line Material'] == 'L') |
            (l['Current Customer Side Service Line Material'] == 'G')]

Cust = Cust.reset_index(drop = True)

PWS.to_excel("Needs Work.xlsx")

def write(file, new, name):
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        new.to_excel(writer, sheet_name=name, index=False)
write('PWS Lines (Found Through Plans).xlsx', PWS, 'PWS_Needs_Replace.xlsx')
write('PWS Lines (Found Through Plans).xlsx', Cust, "Customer_Needs_Replace.xlsx")


###Geolocating
from geopy.geocoders import ArcGIS
geolocator_arcgis = ArcGIS()

geo = df3[['GEODBID','FEATUREID', 'Account Number', 'Meter Number',
           'Service Address', 'PWS-Owned Service Line Material', 
            'Current Customer Side Service Line Material']]
#Creating separate columns for both City and State, then combining them
#with service address column into a separate column
geo['City'] = "Des Plaines"
geo['State'] = 'IL'
geo['Country'] = 'USA'
cols = ['City', 'State', 'Country']
geo['unique_address'] = geo['Service Address'].str.cat(others=geo[cols], sep=', ',na_rep='')

#Function that matches an address with its latitude and longitude coords
def service_geocode(g_locator, address):
    location = g_locator.geocode(address)
    if location!=None:
      return (location.latitude, location.longitude)
    else:
      return np.NaN

#Applying the above function onto every row
#takes around 2 hours to process 
#https://www.datacamp.com/tutorial/geocoding-for-data-scientists
geo['LAT_LON'] = geo['unique_address'].apply(lambda x:service_geocode(geolocator_arcgis,x))


##Plotting
import geopandas as gpd
from shapely.geometry import Point

#Removing parentheses and putting latitude and longitude coords into diff columns
geo['LAT_LON2'] = geo['LAT_LON'].astype(str).str.replace('(','').str.replace(')','')


geo[['Latitude', 'Longitude']] = (
    geo['LAT_LON2'].astype(str).str.split(', ', expand = True).astype(float)
    )

#Creating a new df that converts the coords into point data 
#https://medium.com/@ianforrest11/graphing-latitudes-and-longitudes-on-a-map-bf64d5fca391
crs = {'init':'EPSG:4326'}
geometry = [Point(xy) for xy in zip(geo['Latitude'], geo['Longitude'])]
geo_df = gpd.GeoDataFrame(geo, crs = crs, geometry = geometry)

l2 = geo_df.merge(lines, how = 'right')

l2 = l2.drop(['City', 'State', 'Country', 'unique_address', 
              'LAT_LON', 'No Work'], axis = 1)

PWS2 = l2.loc[(l2['PWS-Owned Service Line Material'] == 'U') |
              (l2['PWS-Owned Service Line Material'] == 'L') |
              (l2['PWS-Owned Service Line Material'] == 'G')]

Cust2 = l2.loc[(l2['Current Customer Side Service Line Material'] == 'U') |
               (l2['Current Customer Side Service Line Material'] == 'L') |
               (l2['Current Customer Side Service Line Material'] == 'G')]

write('PWS Lines (Found Through Plans) (1).xlsx', PWS2, 'PWS_Needs_Replace2')
write('PWS Lines (Found Through Plans) (1).xlsx', Cust2, 'Cust_Needs_Replace2')


geo_df.to_excel('Points_meters.xlsx')