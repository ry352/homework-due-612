# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:48:14 2019

@author: rryan
"""

import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import cashflows as cf
import statsmodels.formula.api as smf

df = pd.read_csv(r'C:\Users\rryan\Desktop\Personal\Python\DC_Properties.csv')
#copy into clean version
'''dfclean=dfclean.copy()

#remove outliers for price
meanprice = dfclean['PRICE'].mean()
stdprice = dfclean['PRICE'].std()
toprange = meanprice + stdprice * 1.96
botrange = meanprice - stdprice * 1.96

dfclean = dfclean.drop(dfclean[dfclean['PRICE'] > toprange].index)
dfclean = dfclean.drop(dfclean[dfclean['PRICE'] < botrange].index)

#remove null for price
dfclean['PRICE'].fillna(df['PRICE'].mean(),inplace=True)



# see numbers better
pd.options.display.float_format='{0:,.2f}'.format


#Replace WARD values
dfclean['WARD']=dfclean['WARD'].replace('Ward 8','8')
#Replace WARD null
dfclean = dfclean.dropna(axis=0, subset=['WARD'])

# Set WARD as integer
dfclean['WARD']=dfclean['WARD'].astype(int)'''


print(dfclean[['PRICE','SALE_NUM','BATHRM','HF_BATHRM','ROOMS','BEDRM','HEAT','AC','STORIES','ZIPCODE','CITY','LANDAREA','WARD']].corr())

result = smf.ols('PRICE ~ BATHRM + HF_BATHRM + BEDRM + ROOMS + WARD', data=dfclean).fit()

print(result.summary())


