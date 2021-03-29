# %%
import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
from ipywidgets import interact 
from matplotlib import pyplot as plt
from download import download
from datetime import datetime
from scipy import stats as st
#import plotly.graph_objects as go
import calendar
import json
from pandas import json_normalize
#import path

# %%
url = 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042633_archive.json'
path_target = "bike_traffic.json"
download(url, path_target, replace=True)

#%%
data_raw = pd.read_json('bike_traffic.json', lines=True)
     
#%%
data_item = pd.read_json(open("bike_traffic.json", "r", encoding="utf8"),lines=True)
#%%


#%%
with open('bike_traffic.json', "r") as json_data:
    print(type(json_data))
    data_dict = json.load(json_data)
    print(data_dict)
#%%
data_raw = pd.read_json('./bike_traffic.json')
#data_raw.columns=['Date','Hour','Grand total',"Todaystotal", 'Unamed','Remark']
    
    
# %%
data = data_raw.copy()
data.drop(columns=['Unamed', 'Remark', 'Grand total'], inplace=True)
data.dropna(inplace = True)
data.info()

# %%
time_improved = pd.to_datetime(data['Date'] +
                               ' ' + data['Hour'] ,
                               format='%d/%m/%Y %H:%M:%S')
time_improved

# %%                              

data['DateTime'] = time_improved
# remove useles columns
del data['Date']
del data['Hour']


# %%
data

# %%
# visualize the data set now that the time is well formated:
df= data.set_index(['DateTime'])
df.idex = pd.to_datetime(df.index)
df.head(12)

# %%
df['weekday'] = df.index.weekday
df['Hour'] = df.index.time
df['Year'] = df.index.year
df['Date']=df.index.date
df['weekend'] = df['weekday'].isin([5, 6])

# %%
start = df.index[0]
end = df.index[-1]
# %%
week_df = df.loc[(df['weekend']  == False) ]
end_df = df.loc[(df['weekday'] == True )]

# %%
plt.figure(figsize=(20,4))
ax = plt.gca()
ax.set_xlim(start, end)
ax.set_ylim(0, 2500)
ax.set_ylabel('bike Count')
plt.scatter(week_df.index.date, week_df['Todaystotal'])  
plt.scatter(end_df.index.date, end_df['Todaystotal'], color='r')       
ax.legend(['weekday', 'weekend'])





# %%
