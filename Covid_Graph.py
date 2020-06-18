import requests
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "af8414c813mshfa68b005eced6a6p1d6a6fjsn16bfa57b4c34"
    }

response = requests.request("GET", url, headers=headers)
data=response.json()
df = DataFrame(data)

figure = plt.figure(figsize=(12,7))
subplot = figure.add_subplot(211)
plt.title('INDIA COVID-19 STATISTICS')
subplot.plot(df['date'], df['dailyconfirmed'], label='Daily_confirmed', color='blue')
subplot.plot(df['date'], df['dailydeceased'], label='Daily_deceased', color='red')
subplot.plot(df['date'], df['dailyrecovered'], label='Daily_recovered', color='green')
subplot.legend(loc='upper left')

start, end = subplot.get_xlim()
subplot.xaxis.set_ticks(np.arange(start, end, 15))
start, end = subplot.get_ylim()
subplot.yaxis.set_ticks(np.arange(start, end, 20))

subplot = figure.add_subplot(212)
subplot.plot(df['date'], df['totalconfirmed'], label='Total_confirmed', color='blue')
subplot.plot(df['date'], df['totaldeceased'], label='Total_deceased', color='red')
subplot.plot(df['date'], df['totalrecovered'], label='Total_recovered', color='green')
subplot.legend(loc='upper left')

start, end = subplot.get_xlim()
subplot.xaxis.set_ticks(np.arange(start, end, 15))
start, end = subplot.get_ylim()
subplot.yaxis.set_ticks(np.arange(start, end, 20))

plt.show()
#print(df)

