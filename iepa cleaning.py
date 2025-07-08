import pandas as pd
import os

#File Path
os.getcwd()
os.chdir("C:\\Users\\akim\\Downloads")

iepa = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Just Lines')


app_a = iepa.loc[(iepa['PWS-Owned Service Line Material'] == 'U') |
                 (iepa['Customer Side Service Line Material'] == 'U')]

 
def write(file, new, name):
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        new.to_excel(writer, sheet_name=name, index=False)

a=(iepa['Service Address'].astype(str).str.split(', ', expand = True)
    )


write('Master IEPA 2025 Service Line Inventory.xlsx', a, 'Appendix__A')

attach_b = iepa.loc[(iepa['Customer Side Service Line Material'] == 'L')]

write('Master IEPA 2025 Service Line Inventory.xlsx', attach_b, 'Attachment B4')

attach_b2 = iepa.loc[(iepa['Customer Side Service Line Material'] == 'G')]

write('Master IEPA 2025 Service Line Inventory.xlsx', attach_b2, 'Attachment B Galv2')

e = pd.read_excel('Master IEPA 2024 Final Material Inventory Template.xlsx', 'asdf')
e2 = e.loc[e['Is this a high-risk Facility or Area?'] == 'Y']

e2 = (e2['Service Address'].astype(str).str.split(', ', expand = True)
    )
write('Master IEPA 2024 Final Material Inventory Template.xlsx', e2, 'Attachment E2')

match = iepa.loc[iepa['PWS-Owned Service Line Material'] == iepa['Customer Side Service Line Material']]

match.reset_index()
   

filtered = match[match['PWS-Owned Service Line Material'].isin(['U','G','L'])]

filtered = filtered.reset_index(drop = True)

write('Master IEPA 2025 Service Line Inventory.xlsx',filtered,'filtered')

service = iepa[iepa['Classification for Entire Serivice Line'].isin(['U', 'L','GRR'])]

service = service[['Service Address', 'PWS-Owned Service Line Material',
                   'Customer Side Service Line Material']]

write('Master IEPA 2025 Service Line Inventory.xlsx',service,'Repair Inventory')



actual_copper = pd.read_excel('Master IEPA 2025 Service Line Inventory.xlsx', 'Full Table')


    