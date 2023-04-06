# -*- coding: utf-8 -*-
"""

@author: Beni Vimal
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d3 = "./d3.csv"
d1 = "./d111.csv"
china = "./heat_china.csv"
us = "./heat_us.csv"
d2 = "./D7.csv"
ln_plot = "./ln_plot.csv"
linedata = "./linedata.csv"
se_plot = "./se_plot.csv"
hist1 = "./hist1.csv"

def data(fn):
    d = pd.read_csv(fn)
    df = pd.DataFrame(d)
    dfn = df.dropna()
    dt = pd.DataFrame.transpose(dfn)
    return(dfn, dt)

heatdf, heatdt = data(china)
heat_corr = heatdf.corr()
fig, ax = plt.subplots(figsize = (10, 10))
im = ax.imshow(heat_corr, cmap = "YlGn")
cbar = ax.figure.colorbar(im, 
                          ax = ax,
                          shrink = 0.5 )
ax.set_xticks(np.arange(len(heat_corr)), 
               heat_corr.index, 
              size = 12)
ax.set_yticks(np.arange(len(heat_corr)),
               heat_corr.columns,size = 12)
plt.setp(ax.get_xticklabels(),
         rotation = 45,
         ha = "right",
         rotation_mode = "anchor")
ax.set_title("Gaseous Emissions - China", size = 20)
for i in range(len(heat_corr.columns)):
    for j in range(len(heat_corr.columns)):
        text = ax.text(j, i, round(heat_corr.to_numpy()[i, j], 2),
                       ha = "center", va = "center", color = "orange")
fig.tight_layout()
print(heat_corr)

heatdf1, heatdt1 = data(us)
heat_corr1 = heatdf1.corr()
fig1, ax1 = plt.subplots(figsize = (10,10))
im = ax1.imshow(heat_corr, cmap = "YlGn")
cbar = ax1.figure.colorbar(im, 
                          ax = ax1,
                          shrink = 0.5 )
ax1.set_xticks(np.arange(len(heat_corr1)), 
               heat_corr1.index, 
              size = 12)
ax1.set_yticks(np.arange(len(heat_corr1)),
               heat_corr1.columns,size = 12)
plt.setp(ax1.get_xticklabels(),
         rotation = 45,
         ha = "right",
         rotation_mode = "anchor")
ax1.set_title("Gaseous Emissions - US", size = 20)
for i in range(len(heat_corr1.columns)):
    for j in range(len(heat_corr1.columns)):
        text = ax1.text(j, i, round(heat_corr1.to_numpy()[i, j], 2),
                       ha = "center", va = "center", color = "orange")
fig1.tight_layout()
print(heat_corr1)

dfn, dt = data(d3)
print(dt.describe())
grp = dfn.groupby(['Country Name'])[["1990 [YR1990]", "2000 [YR2000]", "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]", "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2018 [YR2018]", "2019 [YR2019]"]].sum()
grp.plot(kind = 'bar', title = 'Total Points by Team', ylabel = 'Emission Rate', xlabel = 'Country Name', figsize = (10, 6))
plt.title("Nitrous oxide emission- thousand metric tons")

dfn1,dt1 = data(d1)
print(dfn1)
grp = dfn1.groupby(['Country Name'])[["1990 [YR1990]", "2000 [YR2000]", "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]", "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2018 [YR2018]"]].sum()
grp.plot(kind = 'bar', title = 'Total Points by Team', ylabel = 'Emission Rate', xlabel = 'Country Name', figsize = (10, 6))
plt.title("CO2 emissions")

line_df, line_dt = data(ln_plot)
print(line_df.dtypes)
line_df.drop(["France"], axis = 1, inplace = True)
line_df.plot(x = "Year", y = ["Australia", "Belgium", "Chile", "Canada"], figsize = (15, 5), style = ['+-', 'o-', '.--', 's:'])
plt.title("Methane emissions - thousand metric tons")

line_df1, line_dt1 = data(linedata)
print(line_df1.dtypes)
line_df1.drop(["France"], axis = 1, inplace = True)
line_df1.plot(x = "Year", y = ["Australia", "Belgium", "Chile", "Canada"], figsize = (15, 5), style = ['+-', 'o-', '.--', 's:'])
plt.title("COE emissions")


a = pd.DataFrame(data = [line_df.mean()], index = line_df.Year)
dt = a.T
data = dt.drop(labels=["2006y", "2007y", "2008y", "2009y", "2010y", "2011y", "2011y", "2012y", "2013y", "2014y", "2015y", "2016y", "2017y", "2018y"], axis = 1)
#data.to_csv('hist.csv')
d = pd.read_csv(se_plot)
a = d.sort_values('2005y').head()
mean_data = a.rename(columns = {'2005y':'Mean'})
print(mean_data)
mean_data.plot.scatter(x = 'Country Name', y = 'Mean', s = 100, c = "orange");
plt.title("Average emission of methane (over 13 years)")

b = pd.DataFrame(data = [line_df1.mean()], index = line_df1.Year)
dt1 = b.T
data = dt1.drop(labels=["2006y", "2007y", "2008y", "2009y", "2010y", "2011y", "2011y", "2012y", "2013y", "2014y", "2015y", "2016y", "2017y", "2018y"], axis = 1)
#data.to_csv('hist1.csv')
data1 = pd.read_csv(hist1)
b = data1.sort_values('2005y').head()
mean_data1 = b.rename(columns = {'2005y':'Mean'})
print(mean_data1)
mean_data1.plot.scatter(x = 'Country Name', y = 'Mean', s = 100, c = "orange");
plt.title("Average emission of CO2 (over 13 years)")