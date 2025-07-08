# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 13:06:08 2025

@author: akim
"""
import pandas as pd
import os

os.chdir("C:\\Users\\akim\\Downloads")

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
