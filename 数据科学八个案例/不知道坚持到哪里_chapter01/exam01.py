import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
trad_flow=pd.read_csv('RFM_TRAD_FLOW.csv',encoding='gbk')
print(trad_flow.columns)
print(trad_flow.iloc[:2])
f=trad_flow.groupby(['cumid','type'])[['transID']].count()
print(f.head())

F_trans=pd.pivot_table(f,index='cumid',columns='type',values='transID')
F_trans['Special_offer']=F_trans['Special_offer'].fillna(0)
print(F_trans.head())

F_trans['interest']=F_trans['Special_offer']/(F_trans['Special_offer']+F_trans['Normal'])
print(F_trans.head())

m=trad_flow.groupby(['cumid','type'])[['amount']].sum()
M_trans=pd.pivot_table(m,values='amount',index='cumid',columns='type')
M_trans['Special_offer']=M_trans['Special_offer'].fillna(0)
M_trans['returned_goods']=M_trans['returned_goods'].fillna(0)
M_trans['value']=M_trans['Special_offer']+M_trans['Normal']+M_trans['returned_goods']
print(M_trans .head())

def to_time(t):
    out_t=time.mktime(time.strptime(t,'%d%b%y:%H:%M:%S'))
    return out_t

trad_flow['time_new']=trad_flow.time.apply(to_time)
print(trad_flow.head())


r=trad_flow.groupby(['cumid'])[['time_new']].max()
print(r.head())







#print(f.columns)
#print(f.index)
#print(f[[True if item[0]==10001 else False for item in list(f.index)]])
#print(trad_flow[trad_flow['cumid']==10001])
