import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os
from stack2dim import *

plt.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False

snd=pd.read_csv(r'data/sndHsPr.csv')
snd['all_pr2']=snd[['price','AREA']].apply(lambda x:x[0]*x[1],axis=1)

district = {'fengtai':'丰台区','haidian':'海淀区','chaoyang':'朝阳区','dongcheng':'东城区','xicheng':'西城区','shijingshan':'石景山区'}
snd['district']=snd['dist'].map(district)


def diag_value_counts():
    figure=plt.figure(figsize=(10,10))
    f1=plt.subplot()
    f1.bar(snd.dist.value_counts().index,snd.dist.value_counts().values)
    plt.show()
    print(type(snd.dist.value_counts()))

def data_describe():
    print(snd.price.mean())
    print(snd.price.median())
    print(snd.price.std())
    print(snd.price.skew())  #偏离值
    snd.price.hist(bins=40)
    plt.show()
#print(snd.dist.value_counts())
#print(snd.groupby(['dist'])['dist'].count())
print(snd.price.agg(['mean','median','sum','std','skew']))  #也可以通过agg集合各种统计操作
print(snd.price.quantile([0.01,0.5,0.99])) #取分位点函数

#以下是两个变量之间的关系

def cross_table():
    sub_sch=pd.crosstab(snd.district,snd.school)
    sub_subway=pd.crosstab(snd.district,snd.subway)
    sub_sch.plot(kind='bar',stacked=True)
    plt.show()
    pass

#标准化的堆叠柱形图
def standard_cross_tab():
    sub_school=pd.crosstab(snd.district,snd.school)
    #sub_school['sum']=sub_school.apply(lambda x:x[0]+x[1],axis=1)
    #也可以按以下汇总
    sub_school['sum'] =sub_school.sum(1)
    sub_school=sub_school.div(sub_school['sum'],axis=0)
    sub_school[[0,1]].plot(kind='bar',stacked=True)
    plt.show()

#自定义，柱状图堆叠显示，粗细反映数据量
#stack2dim(snd,i='district',j='school')

#通过地图来展示效果
def by_map():
    #from pyecharts import Map
    attr=list(snd.groupby(['district'])['price'].mean().index)
    value=list(snd.groupby(['district'])['price'].mean().values)
    min_ = snd.price.groupby(snd.dist).mean().min()
    max_ = snd.price.groupby(snd.dist).mean().max()
   # map = Map('北京各区房价', width = 1200, height = 600)
    #map.add('', attr, value, maptype = '北京', is_visualmap = True, visual_range=[min_, max_],visual_text_color = '#000', is_label_show =True)
    #map.render()
    print(min_)

def barh():
    #连续变量和分类变量，一起作图
    snd.price.groupby(snd.district).mean().sort_values(ascending=False).plot(kind='barh')
    plt.show()
    pass

def boxplot():
    #利用seaborn画箱线图，在pycharm中，要用plt.show()显示
    sns.boxplot('district','price',data=snd)
    plt.show()
    pass

boxplot()
