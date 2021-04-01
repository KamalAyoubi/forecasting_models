#%%
import pandas as pd
import matplotlib.pyplot as plt
from download import download


#%%
#------------------------------------------------------------------------------
#             Part1 : Preparing data
#------------------------------------------------------------------------------


# %%
#Database import 
url = " https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
path_target = "./data_prediction/La_myriade_de_Totems_de_Montpellier.csv"
download(url, path_target, replace=False)


# %%
# df: data frame
df_bike_data_raw = pd.read_csv('./data_prediction/La_myriade_de_Totems_de_Montpellier.csv', sep=',', parse_dates=True)


# %%
#Dropping useless columns ( with missing values).
to_drop = ['Remarque','Unnamed: 4','Vélos depuis le 1er janvier / Grand total']
df_bike1= df_bike_data_raw.drop(to_drop, inplace=False, axis=1)

#Dropping useless rows ( with missing values).
df_bike = df_bike1.dropna()


#%%
# create international timing format in the dataframe
standard_time  = pd.to_datetime(df_bike['Date'] +
                               ' ' + df_bike['HeureTime'],
                               format='%d/%m/%Y %H:%M:%S')

df_bike['DateTime'] = standard_time


#%%
# selecting night values
night_data = df_bike[(df_bike.HeureTime > '00:00') & (df_bike.HeureTime < '09:01')].tail(30)

# remove useles columns
del night_data['Date']
del night_data['HeureTime']

#Indexing by time serie
night_data = night_data.set_index(['DateTime'])

#day_bike = Vélos ce jour / Today's total
night_data.columns = ['day_bike']


#%%

fig, axes = plt.subplots(1, 1, figsize=(6, 4), sharex=True)

axes.plot(night_data['day_bike])
axes.set_title("Vélos par time day ")
axes.set_ylabel("Nombre des vélos")
plt.show()


#%%
#------------------------------------------------------------------------------
#             Part1 : Prediction with ARIMA
#------------------------------------------------------------------------------

# %%
X = night_data.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
print(train.shape,test.shape)

# %%
print(night_data.shape)
size = int(len(X) * 0.66)
train=night_data.iloc[:size]
test=night_data.iloc[size:]
print(train.shape,test.shape)

# %%
from statsmodels.tsa.arima_model import ARIMA
model=ARIMA(train,order=(0,1,2))
model=model.fit()
model.summary()

# %%
start = len(train)
end = len(train)+len(test)-1
pred = model.predict(start=start,end=end,typ='levels').rename('ARIMA Predictions')
print(pred)
# %%
pred.plot(legend='ARIMA Predictions')
test.plot(legend=True)

# %%
model2=ARIMA(night_data,order=(1,1,2))
model2=model2.fit()
night_data.tail()

# %%
index_future_dates= pd.date_range(start='2021-03-1', end='2021-04-04', freq = '1d')
#print(index_future_dates)
#%%
pred2=model2.predict(start=len(night_data),end=len(night_data)+ 34,typ='levels').rename('ARIMA Predictions')
#%%
P = pd.DataFrame(pred2)
P.index = index_future_dates
print(P)

# %%
fig = plt.figure(figsize = (20,8))
#P.plot(legend='ARIMA Predictions')
plt.plot(night_data, color='green')
plt.plot(P, color='red')

# %%