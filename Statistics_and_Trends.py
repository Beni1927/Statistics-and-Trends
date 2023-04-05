# -*- coding: utf-8 -*-
"""

@author: Beni Vimal
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d1 = "./d1.csv"
d3 = "./d3.csv"
china = "./heat_china.csv"
d2 = "./D7.csv"
ln_plot = "./ln_plot.csv"
se_plot = "./se_plot.csv"

def data(fn):
    d = pd.read_csv(fn)
    df = pd.DataFrame(d)
    dfn = df.dropna()
    dt = pd.DataFrame.transpose(dfn)
    return(dfn, dt)


heatdf, heatdt = data(china)
heat_corr = heatdf.corr()
heatdf.dtypes
fig, ax = plt.subplots( figsize = (10,10))
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
ax.set_title("Gaseous Emissions", size = 20)
for i in range(len(heat_corr.columns)):
    for j in range(len(heat_corr.columns)):
        text = ax.text(j, i, round(heat_corr.to_numpy()[i, j], 2),
                       ha="center", va = "center", color = "orange")
fig.tight_layout()
print(heat_corr)


dfn, dt = data(d3)
print(dt.describe())
grp = dfn.groupby(['Country Name'])[["1990 [YR1990]", '2000 [YR2000]', "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]", "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2018 [YR2018]", "2019 [YR2019]"]].sum()
grp.plot(kind = 'bar', title = 'Total Points by Team', ylabel = 'Emission Rate', xlabel = 'Country Name', figsize = (10, 6))
plt.title("Nitrous oxide emission- thousand metric tons")

line_df, line_dt = data(ln_plot)
print(line_df.dtypes)
line_df.drop(["France"], axis = 1, inplace = True)
line_df.plot(x = "Year", y = ["Australia", "Belgium", "Chile", "Canada"], figsize = (15, 5), style = ['+-','o-','.--','s:'])
plt.title("Methane emissions - thousand metric tons")


a = pd.DataFrame(data = [line_df.mean()], index = line_df.Year)
dt = a.T
data = dt.drop(labels = ["2006y", "2007y", "2008y", "2009y", "2010y", "2011y", "2011y", "2012y", "2013y", "2014y", "2015y", "2016y", "2017y", "2018y"], axis = 1)
#data.to_csv('hist.csv')
d = pd.read_csv(se_plot)
a = d.sort_values('2005y').head()
mean_data = a.rename(columns = {'2005y':'Mean'})
print(mean_data)
mean_data.plot.scatter(x = 'Country Name', y = 'Mean', s = 100, c = "green");
plt.title("Average emission of methane (over 13 years)")

