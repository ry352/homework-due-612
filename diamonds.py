# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:16:56 2019

@author: rryan
"""
#import libraries and rename columns
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv(r'C:\Users\rryan\Desktop\Personal\Python\diamonds.csv')
df.rename(columns={'x': 'length'}, inplace=True)
df.rename(columns={'y': 'width'}, inplace=True)
df.rename(columns={'z': 'deep'}, inplace=True)

#add column volume
df['volume']=df['length']*df['width']*df['deep']

#check data
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

#check stats
print(df.describe())

#in a new dataframe dfclean, remove price outliers
dfclean=df.copy()
meanprice=dfclean['price'].mean()
stdprice=dfclean['price'].std()
topprice=meanprice + stdprice*1.96
botprice=meanprice - stdprice*1.96

dfclean = dfclean.drop(dfclean[dfclean['price'] > topprice].index)
dfclean = dfclean.drop(dfclean[dfclean['price'] < botprice].index)

#in dfclean, remove rows where volume has a vlue of 0
dfclean.drop(dfclean.loc[dfclean['volume']==0].index, inplace=True)

#check stats again in dfclean

print(dfclean.describe())

#bin volume and carat
bins = [0,50,100,150,200,250,900]
names=['extra small','small','medium','medium large','large','extra large']
dfclean['Diamond Vol.']=pd.cut(dfclean['volume'],bins,labels=names)

bins1 = [0,1,1.5,2,2.5,3,3.5,4]
names1=['0-1c','1-1.5c','1.5-2c','2-2.5c','2.5-3c','3-3.5c','3.5-4c']
dfclean['Diamond Carat']=pd.cut(dfclean['carat'],bins1,labels=names1)

#groupby bin
print(dfclean.head)
print(dfclean.groupby(['Diamond Vol.'])['price'].mean())
print(dfclean.groupby(['Diamond Carat'])['price'].mean())
print(dfclean.groupby(['Diamond Vol.','color','cut'])['price'].mean())
print(dfclean.groupby(['Diamond Carat','Diamond Vol.'])['price'].mean())
print(dfclean.groupby(['cut'])['price'].mean())
print(dfclean.groupby(['color'])['price'].mean())

#graphs
print(sns.violinplot(x='Diamond Vol.',y='price',data=dfclean))
print(sns.violinplot(x='Diamond Carat',y='price',data=dfclean))
print(sns.violinplot(x='cut',y='price',data=dfclean))
print(sns.violinplot(x='color',y='price',data=dfclean))
print(sns.violinplot(x='clarity',y='price',data=dfclean))
print(dfclean.columns)
print(sns.lmplot(x='volume',y='price',data=dfclean))
print(sns.lmplot(x='carat',y='price',data=dfclean))
print(sns.lmplot(x='carat',y='volume',data=dfclean))
print(dfclean)'''