import folium
from folium.plugins import HeatMap
import pandas as pd
import os
import numpy as np

os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")

df = pd.read_csv("IND cons.csv")

def new(data, sheet, column):
    df = pd.read_excel(data, sheet)
    df

###########################################################################
## Folium heat map

des_plaines_coords = [42.0334, -87.8834]

# Create a Folium map centered on Des Plaines
m = folium.Map(location=des_plaines_coords, zoom_start=13)

# Save or display
m.save("des_plaines_map.html")

min_lat, max_lat = 41.98, 42.08
min_lon, max_lon = -87.95, -87.80

df = df.reset_index(drop=True) 
df[['latitude','longitude']] = df['latitude, longitude'].str.split(",",expand=True) 

df['latitude'] = pd.to_numeric(df['latitude'])
df['longitude'] = pd.to_numeric(df['longitude'])

df_filtered = df[(df['latitude'] >= min_lat) & (df['latitude'] <= max_lat) &
                 (df['longitude'] >= min_lon) & (df['longitude'] <= max_lon)]

m = folium.Map(location=des_plaines_coords, zoom_start=13)

# Add heatmap
HeatMap(data=df_filtered[['latitude', 'longitude']].values, radius=12).add_to(m)

m.save("des_plaines_heatmap.html")

df['Below Avg'] = np.where(df['consumption'] < df['consumption'].median(), 1,0)

heat_data = [[row['latitude'], row['longitude'], row['Below Avg']] for index, row in df.iterrows()]


# Add weighted heatmap
HeatMap(heat_data, radius=15).add_to(m)

# Save or show map
m.save("weighted_heatmap.html")

res = pd.read_excel("Anomalous Consumption.xlsx", 'Residential', usecols = "A, B, C, D, F, J, K")
res['Below Med'] = np.where(res['consumption'] < res['consumption'].median(),1,0)
res_filtered = res[(res['latitude'] >= min_lat) & (res['latitude'] <= max_lat) &
                 (res['longitude'] >= min_lon) & (res['longitude'] <= max_lon)]
res_data = [[row['latitude'], row['longitude'], row['Below Avg']] for index, row in df.iterrows()]
HeatMap(res_data, radius=15).add_to(m)
m.save("res weight.html")


m.save("residential_heatmap.html")





######################################################################################
## Plotting points on map to show where below avg/median consumption is (Residential)
######################################################################################

import plotly.express as px
import plotly.io as pio
import plotly

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

below_avg_res.to_excel("res.xlsx")

plotly.offline.plot(fig, filename='Below Median Residential.html')





######################################################################################
## Plotting points on map to show where below avg/median consumption is (IND)
######################################################################################

ind = pd.read_excel("Anomalous Consumption.xlsx", 'Industrial', usecols = "A, C, D, I, J")

ind['Below Med'] = np.where(ind['consumption'] < ind['consumption'].median(), 1,0)

ind_group = ind.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

ind_below_med = ind_group[ind_group['consumption'] < ind_group['consumption'].median()]

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

with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    ind_below_med.to_excel(writer, sheet_name='Industrial')

plotly.offline.plot(fig, filename='Below Median Industrial.html')





######################################################################################
## Plotting points on map to show where below avg/median consumption is (INS)
######################################################################################

ins = pd.read_excel("Anomalous Consumption.xlsx", 'Institutional', usecols = "A, C, D, I, J")

ins['Below Med'] = np.where(ins['consumption'] < ins['consumption'].median(), 1,0)

ins_group = ins.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

ins_below_med = ins_group[ins_group['consumption'] < ins_group['consumption'].median()]

print(ins_group['Below Med'].mean())

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

with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    ins_below_med.to_excel(writer, sheet_name='Institutional')

plotly.offline.plot(fig, filename='Below Median Institutional.html')





######################################################################################
## Plotting points on map to show where below avg/median consumption is (GOV)
######################################################################################

gov = pd.read_excel("Anomalous Consumption.xlsx", 'Government', usecols = "A, C, D, I, J")

gov['Below Med'] = np.where(gov['consumption'] < gov['consumption'].median(), 1,0)

gov_group = gov.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

gov_below_med = gov_group[gov_group['consumption'] < gov_group['consumption'].median()]

print(gov_group['consumption'].mean())

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

with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    gov_below_med.to_excel(writer, sheet_name='Government')

plotly.offline.plot(fig, filename='Below Median Government.html')





######################################################################################
## Plotting points on map to show where below avg/median consumption is (COUB)
######################################################################################

coub = pd.read_excel("Anomalous Consumption.xlsx", 'City-Owned UnBilled', usecols = "A, C, D, I, J")

coub['Below Med'] = np.where(coub['consumption'] < coub['consumption'].median(), 1,0)

coub_group = coub.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

coub_below_med = coub_group[coub_group['consumption'] < coub_group['consumption'].median()]

print(coub_group['consumption'].mean())

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

with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    coub_below_med.to_excel(writer, sheet_name='City-Owned UnBilled')

plotly.offline.plot(fig, filename='Below Median COUB.html')





######################################################################################
## Plotting points on map to show where below avg/median consumption is (Commercial)
######################################################################################

com = pd.read_excel("Anomalous Consumption.xlsx", 'Commercial', usecols = "A, C, D, I, J")

com['Below Med'] = np.where(com['consumption'] < com['consumption'].median(), 1,0)

com_group = com.groupby(['meter_id', 'address', 'latitude', 'longitude'])[['Below Med', 'consumption']].sum().reset_index()

com_below_med = com_group[com_group['consumption'] < com_group['consumption'].median()]

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

with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    com_below_med.to_excel(writer, sheet_name='Commercial')

plotly.offline.plot(fig, filename='Below Median Commercial.html')





######################################################################################
## Plotting points on map to show where below avg/median consumption is (Commercial)
######################################################################################

ilam = pd.read_excel("Anomalous Consumption.xlsx", 'ILAM Water', usecols = "A, C, D, J, K")

ilam['Below Med'] = np.where(ilam['consumption'] < ilam['consumption'].median(), 1,0)

ilam['Below Med'].sum()

with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    ilam.to_excel(writer, sheet_name='ILAM')



######################################################################################
## Plotting points on map to show where zero consumption points are
######################################################################################

zero = pd.read_excel("Anomalous Consumption.xlsx", 'Zero Consumption', usecols = "A, B, D, E")

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

with pd.ExcelWriter('res.xlsx',
                    mode='a') as writer:  
    zero_group.to_excel(writer, sheet_name='Zero Consumption')

plotly.offline.plot(fig, filename='zero_consumption.html')
