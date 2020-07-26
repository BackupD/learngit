#!/usr/bin/python
# -*- coding=utf-8 -*-



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-100,100,100)
#e^(x)的原函数
f1 = np.exp(x)

#泰勒级数
f2 , f3 , f4 = 0 , 0 , 0
jiechen = 1

for i in range(1,15):
    jiechen *= i
    if i<=5:
        f2 += x**i/jiechen
    if i<=10:
        f3 += x**i/jiechen
    f4 += x**i/jiechen

plt.plot(x,f1,'k','-')
plt.plot(x,f2,'r','--')
plt.plot(x,f3,'g','-.')
plt.plot(x,f4,'c',':')