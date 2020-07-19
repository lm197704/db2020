import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os

auto=pd.read_csv("data/auto_ins.csv",encoding='gbk')
auto['lost_flag']=auto.Loss.map(lambda x:1 if x>0 else 0)

print(auto.head())
print(auto.lost_flag.describe())
print(auto.lost_flag.value_counts()/auto.lost_flag.count())

auto_age=auto.groupby(['Age','lost_flag'])[['Loss']].count()
print(auto_age.head())
t_auto_age=pd.pivot_table(auto_age,index='Age',columns='lost_flag',values='Loss')
#t_auto_age.plot(kind='bar')


fig=plt.figure(figsize=(10,10*2))
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)

sns.boxplot(x='lost_flag',y='Age',data=auto,ax=ax1)
sns.boxplot(x='lost_flag',y='vAge',data=auto,ax=ax2)
plt.show()