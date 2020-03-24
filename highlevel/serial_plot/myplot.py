#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()


