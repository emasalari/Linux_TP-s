#!/usr/bin/env python3
# -*- coding: utf8 -*-


# import sys,os,re
# import numpy as np
# import pandas as pd
# import scipy as sp
# pd.core.common.is_list_like = pd.api.types.is_list_like
import matplotlib.pyplot as plt
# import pandas_datareader as pdr

import yfinance as yf
from pandas_datareader import data, wb
from pandas_datareader import data as pdr
#print (pdr.get_data_fred('GS10'))



#% matplotlib inline
# using yahoo finance downloader
#goog = yf.download('GOOG',start='2010-01-01')
#print (goog.head())
#--------------------------------------------------------------------------------------
# using a list of stocks shares
stocks = ['FB','AMZN','GOOGL','AAPL']
data = yf.download(stocks,start='2018-01-01')
print(data.tail())
data.to_csv('2018-01-01.csv')
data['High']['AAPL'].plot()
plt.show()
#print (data['Close'].head())
#print (data['Close']['FB'])

#--------------------------------------------------------------------------------------
# using pandas datareader
#goog = pdr.get_data_yahoo('GOOG')
#goog.head()

#--------------------------------------------------------------------------------------

# import cv2
#   
# print("OpenCV version:")
# print(cv2.__version__)
# 
# img = cv2.imread("clouds.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 
# cv2.imshow("Over the Clouds", img)
# cv2.imshow("Over the Clouds - gray", gray)
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------

# import scipy as sp
# import matplotlib.pylab as plt
# 
# t = sp.arange(0, 10, 1/100)
# plt.plot(t, sp.sin(1.7 * 2 * sp.pi * t) + sp.sin(1.9 * 2 * sp.pi * t))
# plt.show()
