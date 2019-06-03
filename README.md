# 본인의 과제명 작성

학과 | 학번 | 성명
---- | ---- | ---- 
통계학과 |201411503 | 김명준


## 프로젝트 개요
본인의 프로젝트 개요에 대하여 작성합니다.

## 사용한 공공데이터 
[데이터보기](https://github.com/cybermin/python2019/blob/master/%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%EC%97%AD%EC%82%AC%EC%A0%95%EB%B3%B4_20190520.csv)
http://beta.fnguide.com/SNI/SNI_FactorModelDetail.asp?u_cd=3FM.5B5.X

## 소스
* [링크로 소스 내용 보기](https://github.com/cybermin/python2019/blob/master/tes.py)

* 코드 삽입
~~~python
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
print(data.head())
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
print(cov)
# Moving Average(1year)
.
c
hml_MovingAverage=hml.rolling(window=52).mean()
smb_MovingAverage=smb.rolling(window=52).mean()
hml_MovingAverage=pd.concat([date,hml_MovingAverage],axis=1)
smb_MovingAverage=pd.concat([date,smb_MovingAverage],axis=1)
hml_MovingAverage=hml_MovingAverage.dropna(axis=0)
smb_MovingAverage=smb_MovingAverage.dropna(axis=0)
hmld=df(hml_MovingAverage)
smbd=df(smb_MovingAverage)

#.Portfolio Variance
.
w=np.matrix([0.7,0.3])
portfolio_variance=(w*cov*w.T)[0,0]
weighted_deviation=np.sqrt(portfolio_variance)
mu=np.matrix(np.mean(data[['hml','smb']]))
weighted_average=(w*mu.T)[0,0]
print(portfolio_variance)
print(weighted_deviation)
print(weighted_average)

#시각화
plt.plot(data['date'],data['hml'])
plt.plot(data['date'],data['smb'])
plt.show()

plt.plot(data['date'],data['hml'])
plt.plot(hmld['date'],hmld['hml'])
plt.show()

plt.plot(data['date'],data['smb'])
plt.plot(smbd['date'],smbd['smb'])
plt.show()

plt.plot(hmld['date'],hmld['hml'])
plt.plot(smbd['date'],smbd['smb'])
plt.show()
~~~
