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
path_target = "./data/La_myriade_de_Totems_de_Montpellier.csv"
download(url, path_target, replace=False)


# %%
# df: data frame
df_bike_data_raw = pd.read_csv('./data/La_myriade_de_Totems_de_Montpellier.csv', sep=',', parse_dates=True)


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


#%%









# %%

from statsmodels.tsa.arima_model import ARIMA
#%%
fig = plt.figure(figsize=(10,8))
model = ARIMA(bike1['VCJ'], order=(2,1,2)) 
ax = plt.gca()
results = model.fit()
plt.plot(bike1['VCJ'], color='green')
plt.plot(results.fittedvalues, color='red')
ax.legend([' bike count', 'prediction'])

#%%
print(results)
# %%
fig = plt.figure(figsize=(20,8))
num_points = len(bike1['VCJ'])
x = results.predict(start=(20), end=(29), dynamic=False)

plt.plot(bike1['VCJ'][:30])
plt.plot(x, color='r')
#%%

















#%%



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
model=ARIMA(train,order=(1,1,2))
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
#%%
P['2021-04-01']
# %%

















# %%
X = bike_ts.values
size = int(len(X) * 0.50)
train, test = X[0:size], X[size:len(X)]
print(train.shape,test.shape)

# %%
print(bike_ts.shape)
size = int(len(X) * 0.66)
train=bike_ts.iloc[:size]
test=bike_ts.iloc[size:]
print(train.shape,test.shape)

# %%
from statsmodels.tsa.arima_model import ARIMA
model=ARIMA(train,order=(1,1,2))
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
model2=ARIMA(bike_ts,order=(1,1,2))
model2=model2.fit()
bike_ts.tail()

# %%
index_future_dates= pd.date_range(start='2021-03-1', end='2021-04-04', freq = '1d')
#print(index_future_dates)
#%%
pred2=model2.predict(start=len(bike_ts),end=len(bike_ts)+ 34,typ='levels').rename('ARIMA Predictions')
#%%
P = pd.DataFrame(pred2)
P.index = index_future_dates
print(P)

# %%
fig = plt.figure(figsize = (20,8))
#P.plot(legend='ARIMA Predictions')
plt.plot(bike_ts, color='green')
plt.plot(P, color='red')
#%%
P['2021-04-01']
# %%






