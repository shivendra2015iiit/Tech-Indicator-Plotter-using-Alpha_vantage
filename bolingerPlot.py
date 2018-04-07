import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import animation
from matplotlib import style
from alpha_vantage.techindicators import TechIndicators
import sys
import time



style.use('ggplot')

symbol = sys.argv[1]
ts = TechIndicators(key='X7GN8OP6JOXQGTOH', output_format='pandas')
print("downloading data...")
data, meta_data = ts.get_bbands(symbol=symbol, interval='1min', time_period=10, series_type='close')
print("Saving...")
data.to_csv('BBANDS_' + symbol + '.csv')
print("Ploting...")
data=pd.read_csv('BBANDS_' + symbol + '.csv')

data.plot(y=['Real Upper Band','Real Middle Band','Real Lower Band'],title='Bollinger Bands')

#anim = animation.FuncAnimation(fig, stockchart, interval=100)
plt.show()