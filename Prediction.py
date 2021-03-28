#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from download import download

# %%
#Database import 
#df_bike_data_raw = pd.read_csv('./data/La_myriade_de_Totems_de_Montpellier.csv', sep=',', parse_dates=True)
#data = df_bike_data_raw.values

#%%
url = " https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
path_target = "./data/La_myriade_de_Totems_de_Montpellier.csv"
download(url, path_target, replace=False)  # if needed `pip install download`

# %%
# df: data frame
df_bike_data_raw = pd.read_csv('./data/La_myriade_de_Totems_de_Montpellier.csv', sep=',', parse_dates=True)


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
#%%
del df_bike['Heure / Time']


# %%

bike_ts = df_bike.set_index(['DateTime'])
#bike_ts = polution_ts.sort_index(ascending=True)
#bike_ts.head(12)


# %%

#V1J = Vélos depuis le 1er janvier / Grand total
#VCJ = Vélos ce jour / Today's total
bike_ts.columns = ['V1J','VCJ']
#%%
del bike_ts['V1J']

#%%

fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

#axes[0].plot(bike_ts['V1J']).resample('d').mean(), '-'
#axes[0].set_title("Vélos depuis le 1er janvier / Grand total")
#axes[0].set_ylabel("Nombre des vélos")

axes[1].plot(bike_ts['VCJ'])
axes[1].set_title("Vélos ce jour / Today's total")
axes[1].set_ylabel("Nombre des vélos")

axes[0].plot(bike_ts['VCJ'].resample('d').mean(), '-')
axes[0].set_title("Vélos depuis le 1er janvier / Grand total")
axes[0].set_ylabel("Nombre des vélos")


plt.show()


# %%

bike_day_mean=bike_ts['VCJ'].resample('d').mean()

bike_ts = pd.DataFrame(bike_day_mean)
#%%































from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    #rolmean = pd.rolling_mean(timeseries, window=12)
    rolmean = pd.Series(timeseries).rolling(window=12).mean()

    #rolstd = pd.rolling_std(timeseries, window=12)#Plot rolling statistics:
    rolstd = pd.Series(timeseries).rolling(window=12).std()

    plt.plot(timeseries, color='blue',label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

# %%

bike_ts






#%%
test_stationarity(bike_ts['VCJ'])
# %%

from statsmodels.tsa.arima_model import ARIMA
#%%
fig = plt.figure(figsize=(20,8))
model = ARIMA(bike_ts['VCJ'], order=(1,0,2)) 
ax = plt.gca()
results = model.fit()
plt.plot(bike_ts['VCJ'], color='green')
plt.plot(results.fittedvalues, color='red')
ax.legend(['Car Count', 'Forecast'])
#%%
model.fit?
#%%
print(results)
# %%
fig = plt.figure(figsize=(20,8))
num_points = len(bike_ts['VCJ'])
x = results.predict(start=(1350), end=(1376), dynamic=False)

plt.plot(bike_ts['VCJ'][:1377])
plt.plot(x, color='r')
#%%


















#%%



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



























