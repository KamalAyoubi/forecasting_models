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
#Importe Data:
url1 = 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042634_archive.json'
path_target = "bike_traffic1.json"
download(url1, path_target, replace=False)


#%%
#Read .Json data as dataframe#Display of the first 5 lines 
bike_traffic_df1 = pd.read_json('bike_traffic1.json', lines=True)
     



bike_traffic_df1.head(n=2)

#%%



from pandas import Series


#%%
data_test=bike_traffic_df2.join(bike_traffic_df2['dateObserved'].apply(lambda x: Series(x.split('/'))))
data_test=data_test.rename(columns = {0: 'start_of_day', 1: 'end_of_day'}) 

data_test['start_of_day'] = data_test['start_of_day'].str.replace('T',' ')
#%%

time_improved = pd.to_datetime(data_test['start_of_day'] ,
                               format='%Y-%m-%d %H:%M:%S')
time_improved

# %%                              

data_test['start_day'] = time_improved


# %%
data_test = data_test.set_index(['start_day'])

#%%
###################teste
bike_traffic_df=bike_traffic_df.rename(columns = {'intensity': 'latte1'})
#%%
bike_traffic_df1=bike_traffic_df1.rename(columns = {'intensity': 'latte2'}) 


#%%
d = [bike_traffic_df['latte1'], bike_traffic_df1['latte2']]
#%%

data_test22 = pd.DataFrame([bike_traffic_df['latte1'], bike_traffic_df1['latte2']])
data_test22=data_test22.T
#%%
data_test22['startday'] = time_improved
#%%
data_test22 = data_test22.set_index(['startday'])
# %%
#Display of the last 5 lines 
bike_traffic_df1.tail(n=2)


# %%
#Checking data columns
bike_traffic_df.columns

df_titanic.describe()
df_titanic.info()


#%%
from ipywidgets import interact


#%%
from pandas import Series


#%%
data_test=bike_traffic_df2.join(bike_traffic_df2['dateObserved'].apply(lambda x: Series(x.split('/'))))
data_test=data_test.rename(columns = {0: 'start_of_day', 1: 'end_of_day'}) 

data_test['start_of_day'] = data_test['start_of_day'].str.replace('T',' ')
#%%

time_improved = pd.to_datetime(data_test['start_of_day'] ,
                               format='%Y-%m-%d %H:%M:%S')
time_improved

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

def hist_explore( pos ='latte1', alpha = 'd', bw=1 ):

  
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    ax.plot(data_test22[pos].resample( alpha ).mean(), '-*')
    #ax.hist(df_titanic['Age'], density=density,
            #bins=n_bins, alpha=alpha)  # standardization
    plt.xlabel('Age')
    plt.ylabel('Density level')
    plt.title("Histogram for passengers age")
    plt.tight_layout()
    plt.show()


## todo CORRECT THE DENSITY OPTION.

# %%

interact(hist_explore ,pos=['latte1','latte2'] ,alpha=['d','m'],bw=(1, 6, 1))
#%%
import ipywidgets as widgets

#%%
def hist_explore( bw=1 ):
    

    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    ax.hist(bike_traffic_df['intensity'])
    
    plt.xlabel('Age')
    plt.ylabel('Density level')
    plt.title("Histogram for passengers age")
    plt.tight_layout()
    plt.show()


## todo CORRECT THE DENSITY OPTION.

# %%

interact(hist_explore,  alpha=['d','m'],bw=(1, 6, 1))

# %%
