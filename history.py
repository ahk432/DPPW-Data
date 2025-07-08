i = app_a[
    (~app_a['PWS-Owned Service Line Material'].isin(['G', 'L'])) &
    (~app_a['Customer Side Service Line Material'].isin(['G', 'L']))
    ]
i.count
i.unique()
i['PWS-Owned Service Line Material'].unique()
i['Customer Side Service Line Material'].unique()
write('Master IEPA 2024 Final Material Inventory Template.xlsx', i, 'Appendix_A')
def write(file, new, name):
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        new.to_excel(writer, sheet_name=name, index=False)
write('Master IEPA 2024 Final Material Inventory Template.xlsx', i, 'Appendix_A')
a=(i['Service Address'].astype(str).str.split(', ',n = 6, expand = True)
    )
a=(i['Service Address'].astype(str).str.split(', ', expand = True)
    )
a=(i['Service Address'].astype(str).str.split(', ', expand = False)
    )
a=(i['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2024 Final Material Inventory Template.xlsx', a, 'Appendix_A')
write('Master IEPA 2024 Final Material Inventory Template.xlsx', a, 'Appendix__A')
attach_b = iepa[
    (iepa['PWS-Owned Service Line Material'].isin(['G', 'L'])) &
    (iepa['Customer Side Service Line Material'].isin(['G', 'L']))
    ]
attach_b = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'L') |
                    (iepa['Customer Side Service Line Material'] == 'L')]
b = (attach_b['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2024 Final Material Inventory Template.xlsx', b, 'Attachment B')
attach_b2 = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'G') |
                    (iepa['Customer Side Service Line Material'] == 'G')]
b2 = (attach_b2['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2024 Final Material Inventory Template.xlsx', b2, 'Attachment B Galv')
e = pd.read_excel('Master IEPA 2024 Final Material Inventory Template.xlsx', 'Sheet 1')
e = pd.read_excel('Master IEPA 2024 Final Material Inventory Template.xlsx', 'asdf')
e2 = e.loc[e['Is this a high-risk Facility or Area'] == Y]
e2 = e.loc[e['Is this a high-risk Facility or Area?'] == Y]
Y
e2 = e.loc[e['Is this a high-risk Facility or Area?'] == 'Y']
write('Master IEPA 2024 Final Material Inventory Template.xlsx', e2, 'Attachment E')
e2 = (e2['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2024 Final Material Inventory Template.xlsx', e2, 'Attachment E')
write('Master IEPA 2024 Final Material Inventory Template.xlsx', e2, 'Attachment E2')
match = iepa.loc[iepa['PWS-Owned Service Line Material'] == iepa['Customer Side Service Line Material']]
match = match[~match[['PWS-Owned Service Line Material'].isin(['C', 'O'])]]
for row in match:
    if (match['PWS-Owned Service Line Material'] == 'C'):
        continue
    elif match['PWS-Owned Service Line Material'] == 'O':
        continue
    else:
        print(row)
for row in match:
    if row in match['PWS-Owned Service Line Material'] == 'C':
        continue
    elif row in match['PWS-Owned Service Line Material'] == 'O':
        continue
    else:
        print(row)
i =[]
for row in match:
    if row in match['PWS-Owned Service Line Material'] == 'C':
        continue
    elif row in match['PWS-Owned Service Line Material'] == 'O':
        continue
    else:
        i.append(row)
for row in match:
    if row in match['PWS-Owned Service Line Material'] == 'G':
        i.append(row)
    elif row in match['PWS-Owned Service Line Material'] == 'U':
        i.append(row)
    elif row in match['PWS-Owned Service Line Material'] == 'L':
        i.append(row)
    else:
        continue
match.reset_index()
for index,row in match:
    if row in match['PWS-Owned Service Line Material'] in ('G', 'U', 'L'):
        i.append(row)
for index,row in match.iterrows():
    if row['PWS-Owned Service Line Material'] in ('G', 'U', 'L'):
        i.append(row)
i= match[match['PWS-Owned Service Line Material'].isin(['U', 'G', 'L'])]
i.reset_index()
filtered = match[match['PWS-Owned Service Line Material'].isin(['U','G','L'])]
filtered.reset_index()
filtered = filtered.reset_index()
filtered = filtered.reset_index(drop = True)
filtered = match[match['PWS-Owned Service Line Material'].isin(['U','G','L'])]
filtered = filtered.reset_index(drop = True)
write('Master IEPA 2024 Final Material Inventory Template.xlsx', filtered, 'filtered')
write('Master IEPA 2025 Service Line Inventory.xlsx',filtered,'filtered')

## ---(Wed Apr 16 14:59:38 2025)---
iepa = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Full Table')
import pandas as pd
import os

#File Path
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")
iepa = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Full Table')
app_a = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'U') |
                 (iepa['Customer Side Service Line Material'] == 'U')]
match = iepa.loc[iepa['PWS-Owned Service Line Material'] == iepa['Customer Side Service Line Material']]

match.reset_index()


filtered = match[match['PWS-Owned Service Line Material'].isin(['U','G','L'])]

filtered = filtered.reset_index(drop = True)

write('Master IEPA 2025 Service Line Inventory.xlsx',filtered,'filtered')
match = iepa.loc[iepa['PWS-Owned Service Line Material'] == iepa['Customer Side Service Line Material']]

match.reset_index()


filtered = match[match['PWS-Owned Service Line Material'].isin(['U','G','L'])]

filtered = filtered.reset_index(drop = True)
service = iepa[iepa['Classification for Entire Service Line'].isin(['U', 'L','GRR'])]
iepa = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Full Table')
service = iepa[iepa['Classification for Entire Service Line'].isin(['U', 'L','GRR'])]
service = iepa[iepa['Classification for Entire Service Line '].isin(['U', 'L','GRR'])]
service = iepa[iepa['Classification for Entire Serivice Line'].isin(['U', 'L','GRR'])]
service = service[['Service Address', 'PWS-Owned Service Line Material',
                   'Customer Side Service Line Material']]
write('Master IEPA 2025 Service Line Inventory.xlsx',service,'Repair Inventory')
def write(file, new, name):
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        new.to_excel(writer, sheet_name=name, index=False)
write('Master IEPA 2025 Service Line Inventory.xlsx',service,'Repair Inventory')

## ---(Thu Apr 17 09:22:16 2025)---
import pandas as pd
import os

#File Path
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")
iepa = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Full Table')


app_a = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'U') |
                 (iepa['Customer Side Service Line Material'] == 'U')]
attach_b = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'L') |
                    (iepa['Customer Side Service Line Material'] == 'L')]
iepa = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Just Lines')
attach_b = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'L') |
                    (iepa['Customer Side Service Line Material'] == 'L')]

b = (attach_b['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2025 Service Line Inventory.xlsx', b, 'Attachment B2')
def write(file, new, name):
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        new.to_excel(writer, sheet_name=name, index=False)
write('Master IEPA 2025 Service Line Inventory.xlsx', b, 'Attachment B2')
attach_b2 = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'G') |
                    (iepa['Customer Side Service Line Material'] == 'G')]



b2 = (attach_b2['Service Address'].astype(str).str.split(', ', expand = True)
    )

write('Master IEPA 2025 Service Line Inventory.xlsx', b2, 'Attachment B Galv')
write('Master IEPA 2025 Service Line Inventory.xlsx', b2, 'Attachment B Galv2')
attach_b = iepa.loc[(iepa['Customer Side Service Line Material'] == 'L')]
b = (attach_b['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2025 Service Line Inventory.xlsx', b, 'Attachment B2')
attach_b2 = iepa.loc[(iepa['Customer Side Service Line Material'] == 'G')]
b2 = (attach_b2['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2025 Service Line Inventory.xlsx', b2, 'Attachment B Galv2')
actual_copper = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Full Table')
if actual_copper['Year PWS-Owned Service Line was Installed'] >= 2021:
    actual_copper['Customer Side Service Line Material'] == "C"
attach_b2 = iepa.loc[(iepa['Customer Side Service Line Material'] == 'G')]
attach_b = iepa.loc[(iepa['Customer Side Service Line Material'] == 'L')]

write('Master IEPA 2025 Service Line Inventory.xlsx', b, 'Attachment B2')
attach_b2 = iepa.loc[(iepa['Customer Side Service Line Material'] == 'G')]

write('Master IEPA 2025 Service Line Inventory.xlsx', attach_b2, 'Attachment B Galv2')
attach_b = iepa.loc[(iepa['Customer Side Service Line Material'] == 'L')]
write('Master IEPA 2025 Service Line Inventory.xlsx', b, 'Attachment B3')
write('Master IEPA 2025 Service Line Inventory.xlsx', attach_b, 'Attachment B4')

## ---(Fri Apr 25 13:05:08 2025)---
import pandas as pd
df = pd.read_excel('PWS Lines (Found through Plans)(1).xlsx', 'Sheet 2')
df = pd.read_excel('PWS Lines (Found through Plans) (1).xlsx', 'Sheet 2')
import os
os.getwd()
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")
df = pd.read_excel('PWS Lines (Found through Plans) (1).xlsx', 'Sheet 2')
df = pd.read_excel('PWS Lines (Found through Plans) (1).xlsx', 'a')
df = pd.read_excel('PWS Lines (Found through Plans)(1).xlsx', 'a')
df = pd.read_excel('PWS Lines (Found through Plans) (1).xlsx', 'a')
df2 = pd.read_excel('PWS Lines (Found Through Plans) (1).xlsx','b')
df3 = df.merge(df2)
df3 = df.merge(df2, how = 'left')
df3 = df.merge(df2, how = 'inner')
df3 = df.merge(df2, how = 'outer')
df3 = df.merge(df2, how = 'right', on = 'Service Address')
df3 = df.merge(df2, how = 'outer', on = 'Service Address')
df3 = df.merge(df2, how = 'inner', on = 'Service Address')
df3 = df.merge(df2, how = 'left', on = 'Service Address')
df3 = df.merge(df2, how = 'right', on = 'Service Address')
df3 = df.merge(df2, how = 'left', on = 'Service Address')
df = df[['Service Address','PWS-Owned Service Line Material','Customer Side Service Line Material']]
df2 = df2[['Service Address','PWS-Owned Service Line Material','Customer Side Service Line Material']]
df2 = df2[['Service Address','PWS-Owned Service Line Material','Current Customer Side Service Line Material']]
df3 = df.merge(df2, how = 'outer', on = 'Service Address')
df2 = pd.read_excel('PWS Lines (Found Through Plans) (1).xlsx','c')
df3 = df.merge(df2, how = 'left')
df3 = df.merge(df2, how = 'outer')
df2['Service Address'] = df2['Match_addr']
df3 = df.merge(df2, how = 'outer')
df3.loc[df3["Service Address"] == df3['Match_addr'], "PWS-Owned Service Line Material"] = 'C'
df3.loc[df3["Service Address"] == df3['Match_addr'], "Customer Side Service Line Material"] = 'C'
df = pd.read_excel('PWS Lines (Found through Plans) (1).xlsx', 'a')
df = df[['Service Address','PWS-Owned Service Line Material','Customer Side Service Line Material']]
df2 = pd.read_excel('PWS Lines (Found Through Plans) (1).xlsx','c')
df2['Service Address'] = df2['Match_addr']
df3 = df.merge(df2, how = 'outer')
df3.loc[df3["Service Address"] == df3['Match_addr'], "PWS-Owned Service Line Material"] = 'C'

df3.loc[df3["Service Address"] == df3['Match_addr'], "Customer Side Service Line Material"] = 'C'
def write(file, new, name):
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        new.to_excel(writer, sheet_name=name, index=False)
write('PWS Lines (Found Through Plans) (1).xlsx',df3,'d')

## ---(Tue May  6 13:33:46 2025)---
import pandas as pd
df = pd.read_excel('Points_meters')
df = pd.read_excel('Points_meters.xlsx')
import os
os.getcwd()
os.setwd('C:\\Users\\akim\\Downloads')
os.chdir('C:\\Users\\akim\\Downloads')
df = pd.read_excel('Points_meters.xlsx')

## ---(Fri May 16 08:34:16 2025)---
import pandas as pd
os.getcwd()
import pandas as pd
import os
os.getcwd()
os.chdir('C:\\Users\\akim\\Downloads')
df = read_excel('Seed and Sod Restorations - Open.xlsx')
df = pd.read_excel('Seed and Sod Restorations - Open.xlsx')
df2 = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'Sheet 2')
df2 = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'b')
df3 = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'c')
df.columns = df.iloc[6]
df = df[1:]
df = df[6:]
df = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'a')
df2 = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'b')
df3 = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'c')
ss2 = df.merge(df2)
ss = df + df2 + df3
ss = df + df2
df2 = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'b')
ss = df + df2
df = pd.read_excel('Seed and Sod Restorations - Open.xlsx', 'a')
df2 = pd.read_excel('Concrete Restorations - Open.xlsx')
df3 = pd.read_excel('Asphalt Restorations - Open.xlsx')
ac = df2 + df3
ac = pd.merge(df2, df3, on = 'Nearest Address', how = 'outer')
ac = df2.merge(df3, on = 'Nearest Address', how = 'outer')
ac = df3.merge(df2, on = 'Nearest Address', how = 'outer')
ac = pd.merge(df2, df3, on='Nearest Address', how='outer')
ac = pd.concat([df2, df3], ignore_index=True)
ss = pd.merge(df,ss, on = 'Nearest Address', how = 'left')
ss = pd.merge(df,ss, on = 'Nearest Address', how = 'outer')
ss = pd.merge(df,ss, on = 'Nearest Address', how = 'inner')
ss = pd.merge(df,ac, on = 'Nearest Address', how = 'inner')
def write(file, new, name):
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        new.to_excel(writer, sheet_name=name, index=False)
ss2 = pd.merge(df,ac, on = "Nearest Address", how = 'outer')
ss2 = pd.merge(df,ac, on = "Nearest Address", how = 'right')
ss2 = pd.merge(df,ac, on = "Nearest Address", how = 'left')
ss2 = pd.merge(df,ac, on = "Nearest Address", how = 'inner', indicator = True)
ss2 = pd.merge(df,ac, on = "Nearest Address", how = 'outer', indicator = True)
ss3 = ss2[ss2['_merge'] == 'left_only']
ss.to_excel("Both.xlsx") 

ss3.to_excel('Just Seed and Sod')
ss.to_excel("Both.xlsx") 

ss3.to_excel('Just Seed and Sod.xlsx')

## ---(Thu Jun 26 07:52:42 2025)---
import folium
import seaborn
import folium
import pandas as pd
import os
os.getcwd()
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")
df = read_excel("IND cons.xlsx")
df = pd.read_excel("IND cons.xlsx")
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")

df = pd.read_excel("IND cons.xlsx")
df = pd.read_excel("IND cons.csv")
df = pd.read_csv("IND cons.csv")
df = pd.read_csv("IND cons.csv", drop_index = True)
df = pd.read_csv("IND cons.csv", drop.index = True)
df = pd.read_csv("IND cons.csv", drop.index == True)
df = pd.read_csv("IND cons.csv" index == False)
df = pd.read_csv("IND cons.csv", index == False)
df = pd.read_csv("IND cons.csv", index_col == None)
df = pd.read_csv("IND cons.csv")
import folium
from folium.plugins import HeatMap
des_plaines_coords = [42.0334, -87.8834]

# Create a Folium map centered on Des Plaines
m = folium.Map(location=des_plaines_coords, zoom_start=13)
m.save("des_plaines_map.html")

min_lat, max_lat = 41.98, 42.08
min_lon, max_lon = -87.95, -87.80

df_filtered = df[(df['lat'] >= min_lat) & (df['lat'] <= max_lat) &
                 (df['lon'] >= min_lon) & (df['lon'] <= max_lon)]
df[['Latitude','Longitude']] = df['Latitude, Longitude'].str.split(", ",expand=True) 
df[['Latitude','Longitude']] = df['latitude, longitude'].str.split(", ",expand=True) 
df = df.reset_index(drop=False) 
df = df.reset_index(drop=True) 
df[['Latitude','Longitude']] = df['latitude, longitude'].str.split(", ",expand=True) 
df[['latitude','longitude']] = df['latitude, longitude'].str.split(", ",expand=True) 
df[['latitude','longitude']] = df['latitude, longitude'].str.split(",",expand=True) 
df_filtered = df[(df['latitude'] >= min_lat) & (df['latitude'] <= max_lat) &
                 (df['longitude'] >= min_lon) & (df['longitude'] <= max_lon)]
df['latitude'] = pd.to_numeric(df['latitude'])
df['longitude'] = pd.to_numeric(df['longitude'])
df_filtered = df[(df['latitude'] >= min_lat) & (df['latitude'] <= max_lat) &
                 (df['longitude'] >= min_lon) & (df['longitude'] <= max_lon)]
m = folium.Map(location=des_plaines_coords, zoom_start=13)

# Add heatmap
HeatMap(data=df_filtered[['lat', 'lon']].values, radius=12).add_to(m)
m = folium.Map(location=des_plaines_coords, zoom_start=13)

# Add heatmap
HeatMap(data=df_filtered[['latitude', 'longitude']].values, radius=12).add_to(m)
m.save("des_plaines_heatmap.html")
import numpy as np
df['Below Avg'] = np.where(df['consumption'] < df['consumption'].mean(), 1,0)
heat_data = [[row['latitude'], row['longitude'], row['Below Avg']] for index, row in df.iterrows()]

HeatMap(heat_data, radius=15).add_to(m)
HeatMap(heat_data, radius=12).add_to(m)
df = pd.read_csv("IND cons.csv")
des_plaines_coords = [42.0334, -87.8834]
m = folium.Map(location=des_plaines_coords, zoom_start=13)
min_lat, max_lat = 41.98, 42.08
min_lon, max_lon = -87.95, -87.80
df = df.reset_index(drop=True) 
df[['latitude','longitude']] = df['latitude, longitude'].str.split(",",expand=True) 
df['latitude'] = pd.to_numeric(df['latitude'])
df['longitude'] = pd.to_numeric(df['longitude'])
df_filtered = df[(df['latitude'] >= min_lat) & (df['latitude'] <= max_lat) &
                 (df['longitude'] >= min_lon) & (df['longitude'] <= max_lon)]
m = folium.Map(location=des_plaines_coords, zoom_start=13)
HeatMap(data=df_filtered[['latitude', 'longitude']].values, radius=12).add_to(m)
m.save("des_plaines_heatmap.html")
df['Below Avg'] = np.where(df['consumption'] < df['consumption'].mean(), 1,0)
heat_data = [[row['latitude'], row['longitude'], row['Below Avg']] for index, row in df.iterrows()]
HeatMap(heat_data, radius=15).add_to(m)
m.save("weighted_heatmap.html")
df['Below Avg'] = np.where(df['consumption'] < df['consumption'].median(), 1,0)
heat_data = [[row['latitude'], row['longitude'], row['Below Avg']] for index, row in df.iterrows()]
HeatMap(heat_data, radius=15).add_to(m)
m.save("weighted_heatmap.html")
res = pd.read_excel("Anomalous Consumption.xlsx", 'Residential', usecols = "A, B, D, F, J, K")
res = pd.read_excel("Anomalous Consumption.xlsx", 'Residential', usecols = "A, B, C, D, F, J, K")
res_filtered = res[(res['Latitude'] >= min_lat) & (res['Latitude'] <= max_lat) &
                 (res['Longitude'] >= min_lon) & (res['Longitude'] <= max_lon)]
res_filtered = res[(res['latitude'] >= min_lat) & (res['latitude'] <= max_lat) &
                 (res['longitude'] >= min_lon) & (res['longitude'] <= max_lon)]
# Add heatmap
HeatMap(data=res_filtered[['latitude', 'longitude']].values, radius=12).add_to(m)
m.save("residential_heatmap.html")
res['Below Avg'] = np.where(res['consumption'] < res['consumption'].mean(),1,0)
res_filtered = res[(res['latitude'] >= min_lat) & (res['latitude'] <= max_lat) &
(res['longitude'] >= min_lon) & (res['longitude'] <= max_lon)]
res_filtered = res[(res['latitude'] >= min_lat) & (res['latitude'] <= max_lat) &
                 (res['longitude'] >= min_lon) & (res['longitude'] <= max_lon)]
HeatMap(data=res_filtered[['latitude', 'longitude']].values, radius=12).add_to(m)
m.save("residential_heatmap.html")
res['Below Avg'] = np.where(res['consumption'] < res['consumption'].median(),1,0)
res_filtered = res[(res['latitude'] >= min_lat) & (res['latitude'] <= max_lat) &
                 (res['longitude'] >= min_lon) & (res['longitude'] <= max_lon)]

HeatMap(data=res_filtered[['latitude', 'longitude']].values, radius=12).add_to(m)

m.save("residential_heatmap.html")
res_data = [[row['latitude'], row['longitude'], row['Below Avg']] for index, row in df.iterrows()]
HeatMap(res _data, radius=15).add_to(m)
m.save("res weight.html")
res.groupby('meter_id')['consumption'].median()
res.groupby('meter_id')['Below Avg'].sum()
a = res.groupby('meter_id')['Below Avg'].sum()
a = res.groupby('meter_id', 'address', 'latitude', 'longitude')['Below Avg'].sum()
a = res.groupby(res['meter_id', 'address', 'latitude', 'longitude'])['Below Avg'].sum()
a = res.groupby(res[['meter_id', 'address', 'latitude', 'longitude']])['Below Avg'].sum()
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude'])['Below Avg'].sum()
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])['Below Avg'].sum()
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])[['Below Avg', 'consumption']].sum().reset_index()
folium.Choropleth(
    geo_data=folium.Map(location=des_plaines_coords, zoom_start=13),
    data=a,
    columns=["address", "consumption"],
    key_on="Below Avg",
    fill_color="YlOrRd"
)
from geopy.geocoders import ArcGIS
geolocator_arcgis = ArcGIS()
mask = res['latitude'].isna() | res['longitude'].isna()
def service_geocode(g_locator, address):
    location = g_locator.geocode(address)
    if location!=None:
      return (location.latitude, location.longitude)
    else:
      return np.NaN
mask = res['latitude'].isna() | res['longitude'].isna()

res.loc[mask, 'LAT_LON'] = res.loc[mask, 'address'].apply(
    lambda x: service_geocode(geolocator_arcgis, x)
)

# Step 3: Split LAT_LON into two separate columns
lat_lon_split = res.loc[missing_mask, 'LAT_LON'].apply(pd.Series)
lat_lon_split.columns = ['latitude_filled', 'longitude_filled']

# Step 4: Fill only the missing rows
res.loc[missing_mask, 'latitude'] = lat_lon_split['latitude_filled']
res.loc[missing_mask, 'longitude'] = lat_lon_split['longitude_filled']

# Optional cleanup
res.drop(columns='LAT_LON', inplace=True)
def service_geocode(g_locator, address):
    location = g_locator.geocode(address)
    if location!=None:
      return (location.latitude, location.longitude)
    else:
      return np.NaN
mask = res['latitude'].isna() | res['longitude'].isna()
res.loc[mask, 'LAT_LON'] = res.loc[mask, 'address'].apply(
    lambda x: service_geocode(geolocator_arcgis, x)
)
lat_lon_split = res.loc[mask, 'LAT_LON'].apply(pd.Series)
lat_lon_split.columns = ['latitude_filled', 'longitude_filled']

# Step 4: Fill only the missing rows
res.loc[mask, 'latitude'] = lat_lon_split['latitude_filled']
res.loc[mask, 'longitude'] = lat_lon_split['longitude_filled']

# Optional cleanup
res.drop(columns='LAT_LON', inplace=True)
res.loc[mask, 'LAT_LON'] = res.loc[mask, 'address'].apply(
    lambda x: service_geocode(geolocator_arcgis, x)
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])[['Below Avg', 'consumption']].sum().reset_index()
folium.Choropleth(
    geo_data=folium.Map(location=des_plaines_coords, zoom_start=13),
    data=a,
    columns=["address", "consumption"],
    key_on="Below Avg",
    fill_color="YlOrRd"
)
a = a.dropna(subset = ['latitude', 'longitude'])
folium.Choropleth(
    geo_data=folium.Map(location=des_plaines_coords, zoom_start=13),
    data=a,
    columns=["address", "consumption"],
    key_on="Below Avg",
    fill_color="YlOrRd"
)
import geopandas as gpd
geo = [Point(xy) for xy in zip(a['longitude'], a['latitude'])
geo = [Point(xy) for xy in zip(a['longitude'], a['latitude'])]
from shapely.geometry import Point
geo = [Point(xy) for xy in zip(a['longitude'], a['latitude'])]
gdf = gpd.GeoDataFrame(geo, geometry=a)]
gdf = gpd.GeoDataFrame(geo, geometry=a)
gdf = gpd.GeoDataFrame(geo, geometry=geometry)
gdf = gpd.GeoDataFrame(a, geometry=geo )
gdf.to_file("points.geojson", driver="GeoJSON")
gdf.set_crs(epsg=4326, inplace=True)
gdf.to_file("points.geojson", driver="GeoJSON")
folium.Choropleth(
    geo_data="points.geojson",
    data=a,
    columns=["address", "consumption"],
    key_on="Below Avg",
    fill_color="YlOrRd"
)
folium.Choropleth(
    geo_data="points.geojson",
    data=a,
    columns=["address", "consumption"],
    key_on="featire.properties.Below Avg",
    fill_color="YlOrRd"
)
folium.Choropleth(
    geo_data="points.geojson",
    data=a,
    columns=["address", "consumption"],
    key_on="feature.properties.Below Avg",
    fill_color="YlOrRd"
)
m.save("choropleth_map.html")
m = folium.Map(location=[42.0334, -87.8834], zoom_start=11)
folium.Choropleth(
    geo_data="points.geojson",
    data=a,
    columns=["address", "consumption"],
    key_on="feature.properties.Below Avg",
    fill_color="YlOrRd"
)
m.save("choropleth_map.html")
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])[['Below Avg', 'consumption']].sum().reset_index()
a = a.dropna(subset = ['latitude', 'longitude'])
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])[['Below Avg', 'consumption']].sum().reset_index()
a = a.dropna(subset = ['latitude', 'longitude'])
m = folium.Map(location=[42.0334, -87.8834], zoom_start=11)
folium.Choropleth(
    geo_data="points.geojson",
    data=a,
    columns=["address", "consumption"],
    key_on="feature.properties.Below Avg",
    fill_color="YlOrRd"
)

m.save("choropleth_map.html")
import plotly.express as px
a.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)
a.dropna(
    axis=0,
    how='any',
    subset=None,
    inplace=True
)
color_scale = [(0, 'orange'), (1,'red')]
fig = px.scatter_mapbox(df, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Avg"],
                        color="Below Avg",
                        color_continuous_scale=color_scale,
                        size="Below Avg",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
fig = px.scatter_mapbox(a, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Avg"],
                        color="Below Avg",
                        color_continuous_scale=color_scale,
                        size="Below Avg",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
color_scale = [(0, 'orange'), (1,'red')]

fig = px.scatter_mapbox(a, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Avg"],
                        color="Below Avg",
                        color_continuous_scale=color_scale,
                        size="Below Avg",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
px.renderers.default = "browser"
import plotly.io as pio
pio.renderers.default = "browser"
fig.show()
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])[['Below Avg', 'consumption']].sum().reset_index()
a.dropna(
    axis=0,
    how='any',
    subset=None,
    inplace=True
)
below_avg_res = a[a['consumption'] < a['consumption'].mean()].index
below_avg_res = a[a['consumption'] < a['consumption'].mean()]
print(a['consumption'].mean())
print(a['consumption'].median())
below_avg_res = a[a['consumption'] < a['consumption'].median()]
pio.renderers.default = "browser"
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Avg"],
                        color="Below Avg",
                        color_continuous_scale=color_scale,
                        size="Below Avg",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
res['Below Med'] = np.where(res['consumption'] < res['consumption'].median(),1,0)
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])[['Below Med', 'consumption']].sum().reset_index()
below_avg_res = a[a['consumption'] < a['consumption'].median()]

color_scale = [(0, 'orange'), (1,'red')]

pio.renderers.default = "browser"
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Avg",
                        color_continuous_scale=color_scale,
                        size="Below Avg",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
color_scale = [(0, 'green'), (1,'blue')]

pio.renderers.default = "browser"
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Avg",
                        color_continuous_scale=color_scale,
                        size="Below Avg",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
color_scale = [(0, 'green'), (1,'blue')]

pio.renderers.default = "browser"
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale=color_scale,
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":0,"l":0,"b":0})
fig.show()
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()
color_scale = [(0, 'green'), (1,'blue'),
               (2,'purple'),(3,'yellow'),
               (4,'orange'),(5,'red'),
               (6,'black')]
pio.renderers.default = "browser"
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale=color_scale,
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()
color_scale = [(0, 'green'), (1,'agsunset')]
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale=color_scale,
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()
color_scale = [(0, 'green'), (1,'red')]
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='agsunset',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.show()
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='agsunset',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()
import plotly
plotly.offline.plot(fig, filename='Below Median Residential.html')
ind = pd.read_excel("Anomalous Consumption.xlsx", 'Industrial', usecols = "A, C, D, I, J")
ind['Below Med'] = np.where(ind['consumption'] < ind['consumption'].median(), 1,0)
ind_group = ind.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()
ind_below_med = ind_group[ind_group['consumption'] < ind_group['consumption'].median()]
print(ind_below_med.median())
print(ind_below_med['consumption'].median())
print(ind_below_med['consumption'].mean())
fig = px.scatter_mapbox(below_avg_res, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median Industrial.html')
fig = px.scatter_mapbox(ind_below_med, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median Industrial.html')
ins = pd.read_excel("Anomalous Consumption.xlsx", 'Institutional', usecols = "A, C, D, I, J")
ins['Below Med'] = np.where(ins['consumption'] < ins['consumption'].median(), 1,0)
ins_group = ins.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()
ins_below_med = ins_group[ins_group['consumption'] < ins_group['consumption'].median()]
fig = px.scatter_mapbox(ins_below_med, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median Institutional.html')
print(ins_group['Below Med'].mean())
print(ins_group['Consumption'].mean())
print(ins_group['consumption'].mean())
print(ins_group['consumption'].median())
gov = pd.read_excel("Anomalous Consumption.xlsx", 'Government', usecols = "A, C, D, I, J")

gov['Below Med'] = np.where(gov['consumption'] < gov['consumption'].median(), 1,0)

gov_group = gov.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

gov_below_med = gov_group[gov_group['consumption'] < gov_group['consumption'].median()]
color_scale = [(0, 'green'), (1,'red')]
print(gov_group['Below Med'].mean())
fig = px.scatter_mapbox(gov_below_med, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median Government.html')
coub = pd.read_excel("Anomalous Consumption.xlsx", 'City-Owned UnBilled', usecols = "A, C, D, I, J")

coub['Below Med'] = np.where(coub['consumption'] < coub['consumption'].median(), 1,0)

coub_group = coub.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

coub_below_med = coub_group[coub_group['consumption'] < coub_group['consumption'].median()]
color_scale = [(0, 'green'), (1,'red')]
print(coub_group['consumption'].mean())
print(coub_group['consumption'].median())
fig = px.scatter_mapbox(coub_below_med, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median COUB.html')

com = pd.read_excel("Anomalous Consumption.xlsx", 'Commercial', usecols = "A, C, D, I, J")

com['Below Med'] = np.where(com['consumption'] < com['consumption'].median(), 1,0)

com_group = com.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

com_below_med = com_group[com_group['consumption'] < com_group['consumption'].median()]
com = pd.read_excel("Anomalous Consumption.xlsx", 'Commercial', usecols = "A, C, D, I, J")

com['Below Med'] = np.where(com['consumption'] < com['consumption'].median(), 1,0)

com_group = com.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

com_below_med = com_group[com_group['consumption'] < com_group['consumption'].median()]

print(com_group['consumption'].mean())
print(com_group['consumption'].median())
fig = px.scatter_mapbox(com_below_med, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median Commercial.html')
ilam = pd.read_excel("Anomalous Consumption.xlsx", 'ILAM Water', usecols = "A, C, D, I, J")

ilam['Below Med'] = np.where(ilam['consumption'] < ilam['consumption'].median(), 1,0)

ilam_group = ilam.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

ilam_below_med = ilam_group[ilam_group['consumption'] < ilam_group['consumption'].median()]
ilam = pd.read_excel("Anomalous Consumption.xlsx", 'ILAM Water', usecols = "A, C, D, J, K")

ilam['Below Med'] = np.where(ilam['consumption'] < ilam['consumption'].median(), 1,0)

ilam_group = ilam.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

ilam_below_med = ilam_group[ilam_group['consumption'] < ilam_group['consumption'].median()]
print(ilam_group['consumption'].())
print(ilam_group['consumption'].mean())
print(ilam_group['consumption'].median())
fig = px.scatter_mapbox(ilam_below_med, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median ILAM.html')

fig = px.scatter_mapbox(ilam_below_med, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "Below Med"],
                        color="Below Med",
                        color_continuous_scale='portland',
                        size="Below Med",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()

plotly.offline.plot(fig, filename='Below Median ILAM.html')
ilam['Below Med'].sum()

## ---(Mon Jun 30 07:50:19 2025)---
zero = pd.read_excel("Anomalous Consumption.xlsx", 'Zero Consumption', usecols = "A, B, D, E")
import pandas as pd
zero = pd.read_excel("Anomalous Consumption.xlsx", 'Zero Consumption', usecols = "A, B, D, E")
os.getcwd()
import os
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")
zero = pd.read_excel("Anomalous Consumption.xlsx", 'Zero Consumption', usecols = "A, B, D, E")
zero_group = zero.groupby(['meter_id', 'address', 'latitude', 'longitude']).count().reset_index(name ='count')
zero_group = zero.groupby(['meter id', 'address', 'latitude', 'longitude']).count().reset_index(name ='count')
zero = pd.read_excel("Anomalous Consumption.xlsx", 'Zero Consumption', usecols = "A, B, D, E")
zero_group = zero.groupby(['meter id', 'address', 'latitude', 'longitude']).count().reset_index(name ='count')
zero_group = zero.groupby(['meter_id', 'address', 'latitude', 'longitude']).count().reset_index(name ='count')
zero_group = zero.groupby(['meter_id', 'address', 'latitude', 'longitude']).count().reset_index(name = "count")
zero_group = zero.groupby(['meter_id', 'address', 'latitude', 'longitude']).count().reset_index()
zero_group = zero.groupby(['meter_id', 'address', 'latitude', 'longitude']).count().reset_index(name = "count")

zero_group = zero.groupby(['meter_id', 'address', 'latitude', 'longitude']) \
                 .size() \
                 .reset_index(name='count')
fig = px.scatter_mapbox(zero_group, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "count"],
                        color="count",
                        color_continuous_scale='portland',
                        size="count",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()
import plotly.express as px
import plotly.io as pio
import plotly
fig = px.scatter_mapbox(zero_group, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="address", 
                        hover_data=["address", "count"],
                        color="count",
                        color_continuous_scale='portland',
                        size="count",
                        zoom=8, 
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":5,"t":100,"l":0,"b":0})
fig.show()
fig.show()
plotly.offline.plot(fig, filename='Below Median COUB.html')
plotly.offline.plot(fig, filename='zero_consumption.html')
res = pd.read_excel("Anomalous Consumption.xlsx", 'Residential', usecols = "A, B, C, D, F, J, K")
res['Below Med'] = np.where(res['consumption'] < res['consumption'].median(),1,0)
import numpy as np
res = pd.read_excel("Anomalous Consumption.xlsx", 'Residential', usecols = "A, B, C, D, F, J, K")
res['Below Med'] = np.where(res['consumption'] < res['consumption'].median(),1,0)
a = res.groupby(['meter_id', 'address', 'latitude', 'longitude', 'device_status'])[['Below Med', 'consumption']].sum().reset_index()

a.dropna(
    axis=0,
    how='any',
    subset=None,
    inplace=True
)
print(a['consumption'].median())
below_avg_res = a[a['consumption'] < a['consumption'].median()]

color_scale = [(0, 'green'), (1,'red')]

pio.renderers.default = "browser"
below_avg_res.to_excel("res.xlsx")
ind = pd.read_excel("Anomalous Consumption.xlsx", 'Industrial', usecols = "A, C, D, I, J")

ind['Below Med'] = np.where(ind['consumption'] < ind['consumption'].median(), 1,0)

ind_group = ind.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

ind_below_med = ind_group[ind_group['consumption'] < ind_group['consumption'].median()]
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    df1.to_excel(writer, sheet_name='Industrial')
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    ind_below_med.to_excel(writer, sheet_name='Industrial')
ins = pd.read_excel("Anomalous Consumption.xlsx", 'Institutional', usecols = "A, C, D, I, J")

ins['Below Med'] = np.where(ins['consumption'] < ins['consumption'].median(), 1,0)

ins_group = ins.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

ins_below_med = ins_group[ins_group['consumption'] < ins_group['consumption'].median()]
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    ins_below_med.to_excel(writer, sheet_name='Institutional')
gov = pd.read_excel("Anomalous Consumption.xlsx", 'Government', usecols = "A, C, D, I, J")

gov['Below Med'] = np.where(gov['consumption'] < gov['consumption'].median(), 1,0)

gov_group = gov.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

gov_below_med = gov_group[gov_group['consumption'] < gov_group['consumption'].median()]
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    gov_below_med.to_excel(writer, sheet_name='Government')
coub = pd.read_excel("Anomalous Consumption.xlsx", 'City-Owned UnBilled', usecols = "A, C, D, I, J")

coub['Below Med'] = np.where(coub['consumption'] < coub['consumption'].median(), 1,0)

coub_group = coub.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

coub_below_med = coub_group[coub_group['consumption'] < coub_group['consumption'].median()]
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    coub_below_med.to_excel(writer, sheet_name='City-Owned UnBilled')
com = pd.read_excel("Anomalous Consumption.xlsx", 'Commercial', usecols = "A, C, D, I, J")

com['Below Med'] = np.where(com['consumption'] < com['consumption'].median(), 1,0)

com_group = com.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

com_below_med = com_group[com_group['consumption'] < com_group['consumption'].median()]
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    com_below_med.to_excel(writer, sheet_name='Commercial')
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    ilam.to_excel(writer, sheet_name='ILAM')
with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    zero_group.to_excel(writer, sheet_name='Zero Consumption')
df = pd.read_csv("sqllab_copy_of_untitled_query_1_20250630T155302.csv")
df2 = pd.read_excel('All meters.csv')
df2 = pd.read_excel('All meters.xlsx')
df2 = pd.read_excel('All meters .xlsx')
merged = pd.merge(df, df2, on = 'meter_id', how = 'outer')
import numpy as np
merged['status match'] = np.where(merged['a'] == merged['device_status'], 1, 0)
merged['status match'] = np.where(merged['a'] == merged['device_status_y'], 1, 0)
merged.unique
merged['status match'] = np.where(merged['a'] == merged['device_status_x'], 1, 0)
merged = pd.merge(df, df2, on = 'meter_id', how = 'inner')
merged = pd.merge(df, df2, on = 'meter_id', how = 'right')
merged = pd.merge(df, df2, on = 'meter_id', how = 'left')
merged = pd.merge(df, df2, on = 'meter_id', how = 'outer')
merged = pd.merge(df, df2, on = ['meter_id', 'device_id', 'address'], how = 'outer')
merged = pd.merge(df, df2, on = ['meter_id', 'device_id', 'asset_address'], how = 'outer')
merged = pd.merge(df, df2, on = 'meter_id', how = 'outer')
merged['status match'] = np.where(merged['a'] == merged['device_status_x'], 1, 0)
df = pd.read_csv("sqllab_copy_of_untitled_query_1_20250630T155302.csv")
df2 = pd.read_excel('All meters .xlsx')
merged = pd.merge(df, df2, on = 'meter_id', how = 'outer')

merged['status match'] = np.where(merged['a'] == merged['device_status_x'], 1, 0)
df2 = pd.read_excel('All meters .xlsx')
merged = pd.merge(df, df2, on = 'meter_id', how = 'outer')
df2 = pd.read_excel('All meters .xlsx')
df2['check'] = np.where(df2['device_id'] == df2['device_id_'], 1,0)
df2['check'].count()
df2['check'].count(0)
df2 = pd.read_excel('All meters .xlsx')
df2['check'] = np.where(df2['device_id'] == df2['device_id_'], 1,0)
df2 = pd.read_excel('All meters .xlsx')

df2['check'] = np.where(df2['device_id'] == df2['device_id_'], 1,0)
data = df2['device_id_'] <= "2025-06-25 00:00:00"
data = df2['end_read_time_local_'] <= "2025-06-25 00:00:00"
df2['time'] = df2['end_read_time_local_'] <= "2025-06-25 00:00:00"
df2['time'] = np.where(df2['end_read_time_local_'] <= "2025-06-25 00:00:00", 1,0)
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
    df2.to_excel(writer, sheet_name='No Read List')
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
c['match'] = np.where(c['meter_id'] == c['meter_id_'], 1,0)
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
c['match'] = np.where(c['meter_id'] == c['meter_id_'], 1,0)
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
c['match'] = np.where(c['meter_id'] == c['meter_id_'], 1,0)
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
c['match'] = np.where(c['meter_id_'] == c['device_id'], 1,0)
c['match'] = np.where(c['meter_id'] == c['device_id_'], 1,0)
d = pd.read_csv('sqllab_untitled_query_1_20250701T173146.csv')
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
d = pd.read_csv('sqllab_untitled_query_1_20250701T173146.csv')
e = c.merge(d, on = 'Device ID', how = 'outer')
e = c.merge(d, on = ['Device ID', 'Address'], how = 'outer')
e = e.dropna(subset = ['Average'])
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
d = pd.read_csv('sqllab_untitled_query_1_20250701T173146.csv')

e = c.merge(d, on = ['Device ID', 'Address'], how = 'outer'
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
d = pd.read_csv('sqllab_untitled_query_1_20250701T173146.csv')

e = c.merge(d, on = ['Device ID', 'Address'], how = 'outer')
e = c.merge(d, on = ['Device ID', 'Address'], how = 'right')
e = c.merge(d, on = ['Device ID', 'Address'], how = 'left')
e = c.merge(d, on = ['Device ID', 'Address'], how = 'inner')
e = pd.merge(c,d on = ['Device ID', 'Address'], how = 'left')
e = pd.merge(c,d, on = ['Device ID', 'Address'], how = 'left')
e = pd.merge(c,d, on = 'Device ID', how = 'left')
print(d['device_id'].dtype)
c.dtypes
d.dtypes
e['Device ID'].astype(int)
e['Device ID'].astype(float)
c['Device ID'] = d['Device ID'].astype(str).str.strip()
c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()
c['Device ID'] = c['Device ID'].astype(float)
d['Device ID'] = d['Device ID'].astype(float)
c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()
c['Device ID'] = c['Device ID'].astype(float)
d['Device ID'] = d['Device ID'].astype(float)
c['Device ID'] = c['Device ID'].astype(float)
c['Device ID'] = c['Device ID'].astype(int)
c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
d = pd.read_csv('sqllab_untitled_query_1_20250701T173146.csv')
e = pd.merge(c,d, on = 'Device ID', how = 'outer')
c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()
e = pd.merge(c,d, on = 'Device ID', how = 'outer')
e = pd.merge(c,d, on = ['Device ID','Address'], how = 'outer')
med = pd.read_csv('sqllab_untitled_query_2_20250701T181745.csv')
med['Device ID'] = med['Device ID'].astype(str).str.strip()
med = pd.read_csv('sqllab_untitled_query_2_20250701T181745.csv')
med['Device ID'] = med['Device ID'].astype(str).str.strip()
am = pd.merge(e, med, on = ['Device ID', 'Address'], how = 'outer')
med = pd.read_csv('sqllab_avg_consumption_by_meter_20250702T132336.csv')
d = pd.read_csv('sqllab_copy_of_untitled_query_1_20250702T131911.csv')
c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()
c['device iD'] = c['device iD'].astype(str).str.strip()
d['device iD'] = d['device iD'].astype(str).str.strip()
c['device id'] = c['device id'].astype(str).str.strip()
d['device id'] = d['device id'].astype(str).str.strip()
e = pd.merge(c,d, on = ['device id','address'], how = 'outer')
d = pd.read_csv('sqllab_copy_of_untitled_query_1_20250702T131911.csv')
c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()
e = pd.merge(c,d, on = ['Device ID','Address'], how = 'outer')
med = pd.read_csv('sqllab_avg_consumption_by_meter_20250702T132336.csv')
med['Device ID'] = med['Device ID'].astype(str).str.strip()
am = pd.merge(e, med, on = ['Device ID', 'Address'], how = 'outer')
am['time'] = np.where(am['End Read Time Local'] <= "2025-06-25 00:00:00", 1,0)
am = pd.merge(e, med, on = ['Device ID', 'Address'], how = 'outer')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
    am.to_excel(writer, sheet_name='Avg & Med')
d = pd.read_csv('sqllab_avg_consumption_by_meter_20250702T145428.csv')
c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()
e = pd.merge(c,d, on = ['Device ID','Address'], how = 'outer')

med = pd.read_csv('sqllab_avg_consumption_by_meter_20250702T150011.csv')
med['Device ID'] = med['Device ID'].astype(str).str.strip()

am = pd.merge(e, med, on = ['Device ID', 'Address'], how = 'outer')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
    am.to_excel(writer, sheet_name='Avg & Med')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
    am.to_excel(writer, sheet_name='Avg & Med2')
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')
p = p['Device ID', 'Address']
p = p[p['Device ID', 'Address']]
p = p[['Device ID', 'Address']]
r = pd.merge(q, p, on = 'Device ID', 'Address', how = 'outer')
r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()
r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
p.replace('Des Plaines', '')
p = p.replace('Des Plaines', '')
p = p['Address'].replace('Des Plaines', '')
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')
p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()
p.dtypes
p['Address'].str.replace('Des Plaines', '')
p = p['Address'].str.replace('Des Plaines', '')
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')
q['Device ID'] = q['Device ID'].astype(str).str.strip()
p = p.str.replace('Des Plaines', '')
p.replace('Des Plaines', '')
p['Address'].str.replace('Des Plaines', '')
p['Address'] = p['Address'].str.replace('Des Plaines', '')
r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
q.dtypes
p.dtypes
q['Device ID'] = q['Device ID'].astype(str).str.strip()
r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
p.dtypes
q.dtypes
q['Device ID'] = q['Device ID'].astype(str).str.strip()
r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
p.dtypes
p['Device ID'] = p['Device ID'].astype(str).str.strip()
p.dtypes
r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     r.to_excel(writer, sheet_name='Missing')
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')

p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()
p['Address'] = p['Address'].str.replace('Des Plaines', '')


r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
p = p['Device ID', 'Address']
p = p[['Device ID', 'Address']]
r = pd.merge(q, p, on = ['Device ID', 'Address'], how = 'outer')
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')

p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()

p = p[['Device ID', 'Address']]

p['Address'] = p['Address'].str.replace('Des Plaines', '')


r = pd.merge(p, q, on = ['Device ID'], how = 'outer')
s = pd.read_csv('watermain_break.csv')
s = pd.read_csv('Watermain Breaks.csv')
s['actualfinishdate'] = pd.to_datetime(s['actualfinishdate'])
s['year'] = s['actualfinishdate'].dt.year
s['month']=s['actualfinishdate'].dt.month
s['year'].count
s['year'].unique()
s['year'].value_counts()
b = pd.read_csv('sqllab_avg_consumption_by_meter_20250708T153428.csv')
b['Device ID'] = b['Device ID'].astype(str).str.strip()
b = pd.read_csv('sqllab_avg_consumption_by_meter_20250708T153428.csv')
b['Device ID'] = b['Device ID'].astype(str).str.strip()
b = pd.read_csv('sqllab_avg_consumption_by_meter_20250708T153428.csv')

b['Device ID'] = b['Device ID'].astype(str).str.strip()
f =pd.merge(b,c, on = ['Device ID', 'Address'], how = 'outer')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     f.to_excel(writer, sheet_name='Avg & Med2')
p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()
r = pd.merge(p, q, on = ['Device ID'], how = 'outer')
r = pd.merge(p, q, on = ['Device ID', 'Address'], how = 'outer')
p['Address'] = p['Address'].astype(str).str.strip()
q['Address'] = q['Address'].astype(str).str.strip()
r = pd.merge(p, q, on = ['Device ID', 'Address'], how = 'outer')
d = pd.read_csv('sqllab_avg_consumption_by_meter_20250702T145428.csv')
c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()
e = pd.merge(c,d, on = ['Device ID','Address'], how = 'outer')
b = pd.read_csv('sqllab_avg_consumption_by_meter_20250708T153428.csv')
b['Device ID'] = b['Device ID'].astype(str).str.strip()
f =pd.merge(b,c, on = ['Device ID', 'Address'], how = 'outer')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     f.to_excel(writer, sheet_name='Avg & Med2')
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')

p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()

p = p[['Device ID', 'Address']]

p['Address'] = p['Address'].str.replace('Des Plaines', '')

p['Address'] = p['Address'].astype(str).str.strip()
q['Address'] = q['Address'].astype(str).str.strip()


r = pd.merge(p, q, on = ['Device ID', 'Address'], how = 'outer')

with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     r.to_excel(writer, sheet_name='Missing')
t = pd.merge(f, q, on = ['Device ID', 'Address'], how = 'inner')
t = pd.merge(f, q, on = ['Device ID', 'Address'], how = 'right')
f['Average Consumption'] = f['Average Consumption']/10
f['Median Consumption'] = f['Median Consumption']/10
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     f.to_excel(writer, sheet_name='Avg & Med2')
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')

p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()

p = p[['Device ID', 'Address']]
p['Address'] = p['Address'].str.replace('Des Plaines', '')

p['Address'] = p['Address'].astype(str).str.strip()
q['Address'] = q['Address'].astype(str).str.strip()
t = pd.merge(f, q, on = ['Device ID', 'Address'], how = 'right')
t = pd.merge(f, q, on = ['Device ID', 'Address'], how = 'outer')
t = pd.merge(f, q, on = ['Device ID', 'Address'], how = 'inner')
t = pd.merge(f, r, on = ['Device ID', 'Address'], how = 'inner')
r = pd.merge(p, q, on = ['Device ID', 'Address'], how = 'outer')
t = pd.merge(f, r, on = ['Device ID', 'Address'], how = 'inner')
t = pd.merge(f, r, on = ['Device ID', 'Address'], how = 'right')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     t.to_excel(writer, sheet_name='Missing')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     t.to_excel(writer, sheet_name='Missing2')
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')

p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()

p = p[['Device ID', 'Address']]

p['Address'] = p['Address'].str.replace('Des Plaines', '')

p['Address'] = p['Address'].astype(str).str.strip()
q['Address'] = q['Address'].astype(str).str.strip()
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'inner')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'left')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'right')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'outer')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'inner')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'left')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'inner')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'left')
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')

p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()

p = p[['Device ID', 'Address']]

p['Address'] = p['Address'].str.replace('Des Plaines', '')

p['Address'] = p['Address'].astype(str).str.strip()
q['Address'] = q['Address'].astype(str).str.strip()
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'inner')
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')
p['Device ID'] = p['Device ID'].astype(str).str.strip()
p['Address'] = p['Address'].str.replace('Des Plaines', '')
p['Address'] = p['Address'].astype(str).str.strip()
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'inner')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'left')
p = pd.read_csv('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.csv')
p['Device ID'] = p['Device ID'].astype(str).str.strip()
p['Address'] = p['Address'].str.replace('Des Plaines', '')
p['Address'] = p['Address'].astype(str).str.strip()
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'inner')
p = pd.read_excel('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.xlsx')
p['Device ID'] = p['Device ID'].astype(str).str.strip()
p['Address'] = p['Address'].str.replace('Des Plaines', '')
p['Address'] = p['Address'].astype(str).str.strip()
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'inner')
u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'left')
p = pd.read_excel('METER_INSIGHT_NO_READ_Mon Jun 30 05_00_00 UTC 2025.xlsx')
p = pd.read_excel('no read.xlsx')
r = pd.merge(u, q, on = ['Device ID', 'Address'], how = 'outer')
t = pd.merge(f, r, on = ['Device ID', 'Address'], how = 'right')
with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     t.to_excel(writer, sheet_name='Missing2')