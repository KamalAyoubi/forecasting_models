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
import calendar
import json
from pandas import json_normalize
from ipywidgets import interact
from pandas import Series
# %%
#                                             Importe Data 
#------------------------------------------------------------------------------------------------------------------------


#%%
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


#%%

# %%
#                                             Preparing Data 1
#------------------------------------------------------------------------------------------------------------------------


#%%
data_test=bike_traffic_df2.join(bike_traffic_df2['dateObserved'].apply(lambda x: Series(x.split('/'))))
data_test=data_test.rename(columns = {0: 'start_of_day', 1: 'end_of_day'}) 

data_test['start_of_day'] = data_test['start_of_day'].str.replace('T',' ')
#%%

time_improved = pd.to_datetime(data_test['start_of_day'] ,
                               format='%Y-%m-%d %H:%M:%S')
time_improved                       

data_test['start_day'] = time_improved

data_test = data_test.set_index(['start_day'])

# %%
#                                             Preparing Data 1
#------------------------------------------------------------------------------------------------------------------------

#%%
bike_traffic_df=bike_traffic_df.rename(columns = {'intensity': 'latte1'})

bike_traffic_df1=bike_traffic_df1.rename(columns = {'intensity': 'latte2'}) 


#%%
d = [bike_traffic_df['latte1'], bike_traffic_df1['latte2']]
#%%

data_test22 = pd.DataFrame([bike_traffic_df['latte1'], bike_traffic_df1['latte2']])
data_test22=data_test22.T


# %%
#                                             visualisation
#------------------------------------------------------------------------------------------------------------------------


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
