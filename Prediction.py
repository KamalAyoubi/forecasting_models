#%%

#import os
#import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
#Database import 
df_bike_data_raw = pd.read_csv('./data/La_myriade_de_Totems_de_Montpellier.csv', sep=',', parse_dates=True)
data = df_bike_data_raw.values


#%%
#Display of the first 5 lines 
df_bike_data_raw.head(n=5)

# %%
#Display of the last 5 lines 
df_bike_data_raw.tail(n=5)

# %%
#Checking data columnss
df_bike_data_raw.columns


# %%
#Dropping useless columns ( with missing values).
to_drop = ['Remarque','Unnamed: 4']
df_bike1= df_bike_data_raw.drop(to_drop, inplace=False, axis=1)


# %%
#Dropping useless rows ( with missing values).
df_bike = df_bike1.dropna()


# %%
#Checking data, after cleaning :
df_bike.head(n=5)
df_bike.tail(n=5)
df_bike.columns


#%%

standard_time  = pd.to_datetime(df_bike['Date'] +
                               ' ' + df_bike['Heure / Time'],
                               format='%d/%m/%Y %H:%M:%S')

# Where d = day, m=month, Y=year, H=hour, M=minutes
standard_time 


#%%

# create correct timing format in the dataframe
df_bike['DateTime'] = standard_time 
#%%
# remove useles columns
del df_bike['Date']
del df_bike['Heure / Time']


# %%



# %%

#df_bike.columns = ['',' ','']
