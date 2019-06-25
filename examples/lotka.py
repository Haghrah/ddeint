#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:07:52 2019

@author: arslan
"""

from ddeint import ddeint
from numpy import linspace, array
from matplotlib.pyplot import subplots, show


def model(X, t, d):
    x = X[0](t)
    xd = X[0](t - d)
    y = X[1](t)
    yd = X[1](t - d)
    return array([0.5 * x * (1 - yd), -0.5 * y * (1 - xd)])

g1 = lambda t: 1
g2 = lambda t: 2
tt = linspace(2, 30, 20000)

fig, ax = subplots(1,figsize=(4,4))

for d in [0, 0.2]:
    print("Computing for d=%.02f"%d)
    yy = ddeint(model, [g1, g2], tt, fargs=(d,))
    ax.plot(yy[:,0], yy[:,1], lw=2, label='delay = %.01f'%d)
    ax.legend()

show()

