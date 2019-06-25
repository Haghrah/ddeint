#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:13:13 2019

@author: arslan
"""

from ddeint import ddeint
from numpy import linspace, array, cos
from matplotlib.pyplot import figure, plot, grid, show


def model(X, t):
    return array([-X[0](t - 3 * cos(X[0](t)) ** 2)])

g1 = lambda t: 1
tt = linspace(0, 30, 2000)
yy = ddeint(model, [g1], tt)

figure()
plot(tt, yy[:,0])
grid(True)
show()
