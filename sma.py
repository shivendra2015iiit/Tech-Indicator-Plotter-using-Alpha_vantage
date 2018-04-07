from alpha_vantage.techindicators import TechIndicators
import sys
import time


#This file will fetch and save the tech indicator given as argument to sma_<Ticker_name>.csv
# as it is downloading minute data we can sleep loop for 30 40 seconds.
while(True) :
    try:
        symbol = sys.argv[1]
        ts = TechIndicators(key='X7GN8OP6JOXQGTOH', output_format='pandas')
        data, meta_data = ts.get_sma(symbol=symbol, interval='1min')
        data.to_csv('SMA_'+symbol+'.csv')
        print("saved and going to sleep")
        time.sleep(40)
        print("woke up, downloading again...")

    except:
        print ("Unexpected error:", sys.exc_info()[0])
        raise