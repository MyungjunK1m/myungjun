# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:36:57 2018

@author: lg3
"""

import numpy as np
import pandas as pd
from pandas import DataFrame as df
from pandas import Series
import matplotlib.pyplot as plt

# Data handling
.

data=pd.read_excel('C:/python/xlsx/3fac.xlsx')
data.head()
data=np.matrix(data)
data=df(data,columns=['date','hml','smb'])
data.head()
length1=len(data)
data=data[2:length1]
length1=len(data)
data2=data[['hml','smb']]
data2=np.matrix(data2).T
data2=data2.astype(np.double)
hml=data['hml']
smb=data['smb']
date=data['date']
# Covariance Matrix(Cov1,2)
.
cov=np.cov(data2)
# Moving Average(1year)
.
c
hml_MovingAverage=pd.concat([date,hml_MovingAverage],axis=1)
smb_MovingAverage=smb.rolling(window=52).mean()
smb_MovingAverage=pd.concat([date,smb_MovingAverage],axis=1)
hml_MovingAverage=hml_MovingAverage.dropna(axis=0)
smb_MovingAverage=smb_MovingAverage.dropna(axis=0)



#.Portfolio Variance
.
w=np.matrix([0.7,0.3])
portfolio_variance=(w*cov*w.T)[0,0]
weighted_deviation=np.sqrt(portfolio_variance)
mu=np.matrix(np.mean(data[['hml','smb']]))
weighted_average=(w*mu.T)[0,0]
portfolio_variance
weighted_deviation
weighted_average
