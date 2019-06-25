#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:14:00 2019

@author: arslan
"""

from ddeint import ddeint
from numpy import linspace, array
from matplotlib.pyplot import figure, plot, legend, grid, show

def model(X, t):
    x2 = X[1](t)
    x1d = X[0](t-1)
    x2d = X[1](t-0.2)
    return array([x1d, x1d+x2d, x2])

g1 = lambda t : 1
g2 = lambda t : 1
g3 = lambda t : 1
tt = linspace(0,5,5000)
yy = ddeint(model, [g1, g2, g3], tt)


figure()

plot(tt, yy[:,0])
plot(tt, yy[:,1])
plot(tt, yy[:,2])

legend(["x1", "x2", "x3"])
grid(True)

show()
