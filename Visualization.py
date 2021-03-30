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

from ipywidgets import interact
#import path

# %%
#Importe Data:
url = 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042633_archive.json'
path_target = "bike_traffic.json"
download(url, path_target, replace=False)


#%%
#Read .Json data as dataframe
bike_traffic_df = pd.read_json('bike_traffic.json', lines=True)
     

#%%
#Display of the first 5 lines 
bike_traffic_df.head(n=2)


# %%
#Display of the last 5 lines 
bike_traffic_df.tail(n=2)


# %%
#Checking data columns
bike_traffic_df.columns

df_titanic.describe()
df_titanic.info()


#%%
plt.figure(figsize=(5, 5))
plt.hist(bike_traffic_df['intensity'], density=False, bins=25)
plt.xlabel('Age')
plt.ylabel('Proportion')
plt.title("Passager age histogram")


#%%
from ipywidgets import interact
#%%
def kde_explore(bw=5):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    sns.kdeplot(bike_traffic_df['intensity'], bw=bw, shade=True, cut=0, ax=ax)
    plt.xlabel('Age (in year)')
    plt.ylabel('Density level')
    plt.title("Age of the passengers")
    plt.tight_layout()
    plt.show()
# %%
interact(kde_explore, bw=(0.001, 2, 0.01))

#%%
bike_traffic_df2=bike_traffic_df.copy()

#%%
bike_traffic_df2['laneId'] = bike_traffic_df2['laneId'].astype('str')



#%%
from pandas import Series


#%%
data_test=bike_traffic_df2.join(bike_traffic_df2['dateObserved'].apply(lambda x: Series(x.split('/'))))
data_test=data_test.rename(columns = {0: 'start_of_day', 1: 'end_of_day'}) 


#%%

time_improved = pd.to_datetime(data['start_of_day'] +
                               ' ' + data['Hour'] ,
                               format='%d/%m/%Y %H:%M:%S')
time_improved

# %%                              

data['DateTime'] = time_improved


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
