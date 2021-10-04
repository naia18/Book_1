#!/usr/bin/env python
# coding: utf-8

# # Playing with interactive maps

# ## 1. Introduction

# In this Jupyter Book I use the pandas library to handle data and _geopandas_ which makes it easier to work with geospatial data in python. The aim is just to play a bit with different datasets in order to see the main differences amongst countries regarding several characteristics.
# 
# **Datasets**:
# 
# 1. The first dataset that I have used is the IPCC Socio-economic baseline Data from 1993. They provide per country data on:
#     - Population and Human development. 
#     - Economic conditions.
#     - Land cover/use.
#     - Water.
#     - Agriculture/Food.
#     - Energy.
#     - Biodiversity.

# ## 2. Code

# ### 2.1. Import libraries

# In[1]:


import pandas as pd
import geopandas
import folium


# ### 2.2. Read data from dataset

# In[2]:


# read_html returns a list of tables from the EXCEL file
df_sheet_all = pd.read_excel('Data/Data_GOOD.xls',sheet_name=None)
regions = ['Africa','Australasia', 'Europe', 'Latin America', 'Middle East and Arid Asia', 'North America', 'Small Island States', 'Temperate Asia', 'Tropical Asia']


# ### 2.3. Construct arrays

# I construct the arrays to merge all the results per country and use _geopandas_.

# In[3]:


Africa = df_sheet_all[regions[0]];
Africa = Africa[1:-1];
new_header = Africa.iloc[0] #grab the first row for the header
Africa = Africa[1:] #take the data less the header row
Africa.columns = new_header #set the header row as the df header

Australasia = df_sheet_all[regions[1]];
Australasia = Australasia[1:-1];
new_header = Australasia.iloc[0] #grab the first row for the header
Australasia = Australasia[1:] #take the data less the header row
Australasia.columns = new_header #set the header row as the df header

Europe = df_sheet_all[regions[2]];
Europe = Europe[1:-1];
new_header = Europe.iloc[0] #grab the first row for the header
Europe = Europe[1:] #take the data less the header row
Europe.columns = new_header #set the header row as the df header

Latinam = df_sheet_all[regions[3]];
Latinam = Latinam[1:-1];
new_header = Latinam.iloc[0] #grab the first row for the header
Latinam = Latinam[1:] #take the data less the header row
Latinam.columns = new_header #set the header row as the df header

Mideast = df_sheet_all[regions[4]];
Mideast = Mideast[1:-1];
new_header = Mideast.iloc[0] #grab the first row for the header
Mideast = Mideast[1:] #take the data less the header row
Mideast.columns = new_header #set the header row as the df header

Northam = df_sheet_all[regions[5]];
Northam = Northam[1:-1];
new_header = Northam.iloc[0] #grab the first row for the header
Northam = Northam[1:] #take the data less the header row
Northam.columns = new_header #set the header row as the df header

Islands = df_sheet_all[regions[6]];
Islands = Islands[1:-1];
new_header = Islands.iloc[0] #grab the first row for the header
Islands = Islands[1:] #take the data less the header row
Islands.columns = new_header #set the header row as the df header

Asia_tem = df_sheet_all[regions[7]];
Asia_tem = Asia_tem[1:-1];
new_header = Asia_tem.iloc[0] #grab the first row for the header
Asia_tem = Asia_tem[1:] #take the data less the header row
Asia_tem.columns = new_header #set the header row as the df header

Asia_trop = df_sheet_all[regions[8]];
Asia_trop = Asia_trop[1:-1];
new_header = Asia_trop.iloc[0] #grab the first row for the header
Asia_trop = Asia_trop[1:] #take the data less the header row
Asia_trop.columns = new_header #set the header row as the df header


# ### 2.4. Read Geopandas dataset and create map

# In[4]:


#frames = [Africa, Australasia, Europe, Latinam, Mideast, Northam, Islands, Asia_tem, Asia_trop]
frames = [Africa, Australasia, Europe, Latinam,Mideast,Northam,Islands,Asia_tem,Asia_trop]
result = pd.concat(frames)

# Read the geopandas dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

result = world.merge(result, how="left", left_on=['name'], right_on=['Country'])

# Drop NaN values in dataset
result = result.dropna(subset=['Forest and Woodland (1000 ha) 1993'])
#result.to_excel(r'results.xlsx')

# Create a map with Folium
my_map = folium.Map()


# In[5]:


# Add the data
folium.Choropleth(
    geo_data=result,
    name='choropleth',
    data=result,
    columns=['Country', 'Forest and Woodland (1000 ha) 1993'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Forest and Woodland (1000 ha) 1993'
).add_to(my_map)
my_map.save('forest.html')


# In[ ]:




