import pandas as pd
import numpy as np

df = pd.read_csv("sqllab_copy_of_untitled_query_1_20250630T155302.csv")
df2 = pd.read_excel('All meters .xlsx')

df2['check'] = np.where(df2['device_id'] == df2['device_id_'], 1,0)

df2['time'] = np.where(df2['end_read_time_local_'] <= "2025-06-25 00:00:00", 1,0)


    
    

c = pd.read_excel('All meters .xlsx', "6.30.2025 All Meters")
d = pd.read_csv('sqllab_avg_consumption_by_meter_20250702T145428.csv')


c['Device ID'] = c['Device ID'].astype(str).str.strip()
d['Device ID'] = d['Device ID'].astype(str).str.strip()



e = pd.merge(c,d, on = ['Device ID','Address'], how = 'outer')

b = pd.read_csv('sqllab_avg_consumption_by_meter_20250708T153428.csv')

b['Device ID'] = b['Device ID'].astype(str).str.strip()

f =pd.merge(b,c, on = ['Device ID', 'Address'], how = 'outer')

f['Average Consumption'] = f['Average Consumption']

f['Median Consumption'] = f['Median Consumption']

with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     f.to_excel(writer, sheet_name='Avg & Med2')
    

#Reading new data and merging to try and find a complete list of non-reads
#both from Xylem and Sensus.     
q = pd.read_excel('All meters .xlsx', "Xylem No Read")
p = pd.read_excel('no read.xlsx')

p['Device ID'] = p['Device ID'].astype(str).str.strip()
q['Device ID'] = q['Device ID'].astype(str).str.strip()

p['Address'] = p['Address'].str.replace('Des Plaines', '')

p['Address'] = p['Address'].astype(str).str.strip()
q['Address'] = q['Address'].astype(str).str.strip()


u = pd.merge(p,f, on = ['Device ID', 'Address'], how = 'left')

r = pd.merge(u, q, on = ['Device ID', 'Address'], how = 'outer')


t = pd.merge(f, r, on = ['Device ID', 'Address'], how = 'right')

with pd.ExcelWriter('All meters .xlsx',
                    mode='a') as writer:  
     t.to_excel(writer, sheet_name='Missing2')




s = pd.read_csv('Watermain Breaks.csv')

s['actualfinishdate'] = pd.to_datetime(s['actualfinishdate'])
s['year'] = s['actualfinishdate'].dt.year
s['month']=s['actualfinishdate'].dt.month

s['year'].value_counts()

with pd.ExcelWriter('Watermain Breaks.xlsx',
                    mode='a') as writer:  
     s.to_excel(writer, sheet_name='Breaks')