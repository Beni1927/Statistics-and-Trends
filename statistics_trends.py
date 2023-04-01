# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:38:14 2023

@author: hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

d1 = "./D1.csv"
d2 = "./D2.csv"
d5 = "./D5.csv"
heatmap = "./heat_china"

def data(fn):
    d = pd.read_csv(fn)
    df = pd.DataFrame(d)
    dfn = df.dropna()
    dt = pd.DataFrame.transpose(dfn)
    return(dfn, dt)

df, dt = data(d5)
print(dt)

df.plot(x = "Country Name", y=["1990 [YR1990]", "2000 [YR2000]", "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]", "2015 [YR2015]"], kind= "bar", figsize = (9,8))

df1, dt1 = data(heatmap)
corr_mat = df1.corr()

            


