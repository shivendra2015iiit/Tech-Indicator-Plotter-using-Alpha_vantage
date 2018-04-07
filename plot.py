import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import animation
from matplotlib import style
import sys

style.use('ggplot')
#This file will plot the csv file given as argument and refresh it with interval of 100 sec.

fig = plt.figure(sys.argv[1])          #we have to change it according to the ticker's whose sma we need.
ax1 = fig.add_subplot(1,1,1)

def stockchart(i):
    data=pd.read_csv(sys.argv[1]+".csv")
    ax1.clear()
    try:
        data['SMA'].plot()
    except:
        data['EMA'].plot()


anim = animation.FuncAnimation(fig, stockchart, interval=100)
plt.show()