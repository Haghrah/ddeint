#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:20:06 2019

@author: arslan
"""

from ddeint import ddeint
from numpy import linspace, array, pi, sin
from matplotlib.pyplot import figure, plot, grid, show

def model(X, t):
    return array([X[0](t - 3. * pi / 2.)])

tt = linspace(0,50,10000)
g1 = sin
yy = ddeint(model, [g1], tt)

figure()
plot(tt, yy[:,0])
grid(True)
show()
