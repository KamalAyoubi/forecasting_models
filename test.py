#%%
#import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
from ipywidgets import interact 

from datetime import datetime

import json
from pandas import json_normalize

from ipywidgets import interact
from download import download


#%%

#Database import 
url = [
#Celleneuve
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042633_archive.json',
#Lattes 2
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042634_archive.json',
#Berracasa
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json',
#Lavérune
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042632_archive.json',
#Lattes 1
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042635_archive.json',
#Vieille poste
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063161_archive.json',
#Gerhardt
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063162_archive.json',
#Tanneurs
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_XTH19101158_archive.json',
#Delmas 1
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063163_archive.json',
#Delmas 2
    'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063164_archive.json',
]

download(url[0], "./data_visulization/Celleneuve.json", replace=False)
download(url[1], "./data_visulization/Lattes2.json", replace=False)
download(url[2], "./data_visulization/Berracasa.json", replace=False)
download(url[3], "./data_visulization/Lavérune.json", replace=False)
download(url[4], "./data_visulization/Lattes1.json", replace=False)
download(url[5], "./data_visulization/Vieille_poste.json", replace=False)
download(url[6], "./data_visulization/Gerhardt.json", replace=False)
download(url[7], "./data_visulization/Tanneurs.json", replace=False)
download(url[8], "./data_visulization/Delmas1.json", replace=False)
download(url[9], "./data_visulization/Delmas2.json", replace=False)

#%%
bike_traffic_df1 = pd.read_json('./data_visulization/Celleneuve.json', lines=True)
bike_traffic_df2 = pd.read_json('./data_visulization/lattes2.json', lines=True)
bike_traffic_df3 = pd.read_json('./data_visulization/Berracasa.json', lines=True)
bike_traffic_df4 = pd.read_json('./data_visulization/Lavérune.json', lines=True)
bike_traffic_df5 = pd.read_json('./data_visulization/Lattes1.json', lines=True)
bike_traffic_df6 = pd.read_json('./data_visulization/Vieille_poste.json', lines=True)
bike_traffic_df7 = pd.read_json('./data_visulization/Gerhardt.json', lines=True)
bike_traffic_df8 = pd.read_json('./data_visulization/Tanneurs.json', lines=True)
bike_traffic_df9 = pd.read_json('./data_visulization/Delmas1.json', lines=True)
bike_traffic_df10 = pd.read_json('./data_visulization/Delmas2.json', lines=True)

#Display of the first lines
#bike_traffic_df1.head(n=3)
#bike_traffic_df2.head(n=2)

#%%
from pandas import Series


#Split 'dateObserved' column into two columns 
data_test=bike_traffic_df1.join(bike_traffic_df1['dateObserved'].apply(lambda x: Series(x.split('/'))))
data_test=data_test.rename(columns = {0: 'start_of_day', 1: 'end_of_day'}) 

#replace the 'T' between date and time with a space 
data_test['end_of_day'] = data_test['end_of_day'].str.replace('T',' ')

#Convert to time series 
time_improved = pd.to_datetime(data_test['end_of_day'] , format='%Y-%m-%d %H:%M:%S')               

#Indexing data by 'end_of-day' (time series)
data_test['end_of_day'] = time_improved
data_test = data_test.set_index(['end_of_day'])


#%%
# Rename intensity column by position name
bike_traffic_df1=bike_traffic_df1.rename(columns = {'intensity': 'Celleneuve'})
bike_traffic_df2=bike_traffic_df2.rename(columns = {'intensity': 'Lattes2'}) 
bike_traffic_df3=bike_traffic_df3.rename(columns = {'intensity': 'Berracasa'}) 
bike_traffic_df4=bike_traffic_df4.rename(columns = {'intensity': 'Lavérune'}) 
bike_traffic_df5=bike_traffic_df5.rename(columns = {'intensity': 'Lattes1'}) 
bike_traffic_df6=bike_traffic_df6.rename(columns = {'intensity': 'Vieille_poste'}) 
bike_traffic_df7=bike_traffic_df7.rename(columns = {'intensity': 'Gerhardt'}) 
bike_traffic_df8=bike_traffic_df8.rename(columns = {'intensity': 'Tanneurs'}) 
bike_traffic_df9=bike_traffic_df9.rename(columns = {'intensity': 'Delmas1'}) 
bike_traffic_df10=bike_traffic_df10.rename(columns = {'intensity': 'Delmas2'}) 

#Extract the renamed columns, and combine them into a new dataframe 
data_test22 = pd.DataFrame((bike_traffic_df1['Celleneuve'], bike_traffic_df2['Lattes2'],bike_traffic_df3['Berracasa'],bike_traffic_df4['Lavérune'],bike_traffic_df5['Lattes1'],bike_traffic_df6['Vieille_poste']))
data_test22=data_test22.T

#Indexing neww data by 'end_of-day' (time series)
data_test22['startday'] = time_improved
data_test22 = data_test22.set_index(['startday'])
print(data_test22)

#%%
color_picker = widgets.ColorPicker(
    concise=True
    description='curv color:',
    value='#efefef',
)
color_picker
#%%
def Intenity_visualisation( count_point ='latte1', day_month='d', efefef='red', start_date='2020-12-15', end_date='2021-04-01'):
    
  
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    data_intensity=[]
    ax.plot(data_intensity[count_point].resample( day_month ).mean(), '-*',color= efefef )
    
    plt.xlabel('Time serie')
    plt.ylabel('Intensity')
    plt.title("intensity of bikes")
    plt.tight_layout()
    plt.show()


interact(Intenity_visualisation ,
                                count_point=['Celleneuve', 'Lattes2', 'Berracasa', 'Lavérune','Lattes1',                                                            'Vieille_poste', 'Gerhardt', 'Tanneurs','Delmas1', 'Delmas2'] , 
                                day_month=['d','m'],
                                efefef=color_picker,
                                start_date=widgets.DatePicker(value=pd.to_datetime('2020-12-15')),
                                 end_date=widgets.DatePicker(value=pd.to_datetime('2021-04-01'))
                                
        )
#%%
