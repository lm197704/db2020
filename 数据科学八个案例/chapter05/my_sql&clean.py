# -*- coding：UTF-8 -*-

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


sale=pd.read_csv('data/sale.csv',encoding='gbk')
con=sqlite3.connect(':memory:')
sale.to_sql('sale',con)

sqlresult=pd.read_sql_query('select * from sale',con)

camp=pd.read_csv('data/teleco_camp_orig.csv')

#用缺失值替代0
camp.AvgIncome=camp.AvgIncome.replace({0:np.NAN})
camp['AvgHomeValue']=camp['AvgHomeValue'].replace({0: np.NaN})
#plt.hist(camp.AvgIncome,bins=20,range=(camp.AvgIncome.min(),camp.AvgIncome.max()))
#plt.show()

#print(camp[['Age','AvgHomeValue','AvgIncome']].describe())

def dup_flag():
    camp['dup']=camp.duplicated()
    camp['dup1']=camp.ID.duplicated()
    print(camp.head())
#
def deal_age():
    vmean=camp.Age.mean(axis=0,skipna=True)
    camp['Age_emflag']=camp.Age.isnull()
    camp.Age=camp.Age.fillna(vmean)
    print(camp[:5])
    print(camp.Age.describe())
    pass

def blk(floor,root):
    def f(x):
        if x<floor:
            x=floor
        elif x>root:
            x=root
        return x
    return f

def deal_age_noise():
    print(camp.Age.quantile([0.01,0.5,0.99]))
    q01=camp.Age.quantile(0.01)
    q99=camp.Age.quantile(0.99)
    blk_tot=blk(q01,q99)
    camp.Age=camp.Age.map(blk_tot)
    print(camp.Age.describe())
    print(camp.head())

    pass
deal_age()
deal_age_noise()


