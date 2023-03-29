# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:38:14 2023

@author: hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d1 = "./D1.csv"
d2 = "./D2.csv"

def data(fn):
    d = pd.read_csv(fn)
    df = pd.DataFrame(d)
    dfn = df.dropna()
    dt = pd.DataFrame.transpose(dfn)
    return(dfn, dt)

df, dt = data(d1)
print(dt)

