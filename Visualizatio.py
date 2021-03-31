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
#Read .Json data as dataframe#Display of the first 5 lines 
bike_traffic_df = pd.read_json('bike_traffic.json', lines=True)
     

#%%

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


# %%                              

data_test['start_day'] = time_improved


# %%
data_test = data_test.set_index(['start_day'])
# %%
# visualize the data set now that the time is well formated:
fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

#axes[0].plot(bike_ts['V1J']).resample('d').mean(), '-'
#axes[0].set_title("Vélos depuis le 1er janvier / Grand total")
#axes[0].set_ylabel("Nombre des vélos")

axes[1].plot(data_test['intensity'])
axes[1].set_title("Vélos ce jour / Today's total")
axes[1].set_ylabel("Nombre des vélos")

axes[0].plot(data_test['intensity'].resample('m').mean(), '-*')
axes[0].set_title("Vélos depuis le 1er janvier / Grand total")
axes[0].set_ylabel("Nombre des vélos")


plt.show()

#%%

def hist_explore( alpha = 'm', bw=1 ):


    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    ax.plot(data_test['intensity'].resample( alpha ).mean(), '-*')
    #ax.hist(df_titanic['Age'], density=density,
            #bins=n_bins, alpha=alpha)  # standardization
    plt.xlabel('Age')
    plt.ylabel('Density level')
    plt.title("Histogram for passengers age")
    plt.tight_layout()
    plt.show()


## todo CORRECT THE DENSITY OPTION.

# %%

interact(hist_explore,  alpha=['d','m'],bw=(1, 6, 1))


#%%
def hist_explore( bw=1 ):
    

    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    ax.plot(data_test['intensity'])
    #ax.hist(df_titanic['Age'], density=density,
            #bins=n_bins, alpha=alpha)  # standardization
    plt.xlabel('Age')
    plt.ylabel('Density level')
    plt.title("Histogram for passengers age")
    plt.tight_layout()
    plt.show()


## todo CORRECT THE DENSITY OPTION.

# %%

interact(hist_explore,  alpha=['d','m'],bw=(1, 6, 1))

# %%

def kde_explore(bw):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    sns.kdeplot(data_test['intensity'])
    plt.xlabel('Age (in year)')
    plt.ylabel('Density level')
    plt.title("Age of the passengers")
    plt.tight_layout()
    plt.show()


# %%

interact(kde_explore, bw=(1, 10, 2))

#%%
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
