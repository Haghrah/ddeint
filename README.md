ddeint
=======

Scipy-based delay differential equation (DDE) solver. See the docstrings and examples for more information. 

First of all, I would like to say "Thanks!" to @Zulko for developing the ddeint. I was using the ddeint for solving a system of delay differential equations with multiple time delays. Unfortunately, I was not able to simulate the system with the available features of the ddeint. So I made some changes to it. In this version, alongside with ddeVar, the ddeVars object is introduced for making the state variables with multiple delay values available. ddeVars acts like a list of ddeVar objects. Subsequently, the history of each state variable for time values smaller than zero is given by a list of functions, instead of a function with an array in its output.

An example
-----------
Let our system equation be as below:

<img src="/images/Ex1_Equation.png" width="256">

As it can be seen three history functions for each state variable is needed. Also, there is two delay values 1 and 0.2 in the equations. In order to write the model function we should write the code below:

```python
from ddeint import ddeint
from numpy import linspace, array

def model(Y, t):
    y2 = Y[1](t)
    y1d = Y[0](t-1)
    y2d = Y[1](t-0.2)
    return array([y1d, y1d+y2d, y2])
```

The history functions are defined as:

```python
g1 = lambda t : 1
g2 = lambda t : 1
g3 = lambda t : 1
```
Finally the system is solved as below:
```python
tt = linspace(0,5,5000)
yy = ddeint(model, [g1, g2, g3], tt)
```
The output of the example system is represented below:

<img src="/images/ddeint.png" width="256">

This example is also solved using the Matlab function, dde23. The matlab output is also available here which approves the same results:

<img src="/images/dde23.png" width="256">

Installation
--------------

ddeint can be installed by unzipping the source code in one directory and using this command: ::

    (sudo) python setup.py install
