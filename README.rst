ddeint
=======

Scipy-based delay differential equation (DDE) solver. See the docstrings and examples for more information. 

First of all, I would like to say "Thanks!" to @Zulko for developing the ddeint. I was using the ddeint for solving a system of delay differential equations with multiple time delays. Unfortunately, I was not able to simulate the system with the available features of the ddeint. So I made some changes to it. In this version, alongside with ddeVar, the ddeVars object is introduced for making the state variables with multiple delay values available. ddeVars acts like a list of ddeVar objects. Subsequently, the history of each state variable for time values smaller than zero is given by a list of functions, instead of a function with an array in its output.

How to use new version?
------------------------
Let our system equation be as below:

![Equation](https://github.com/Haghrah/ddeint/blob/master/images/Ex1_Equation.png)

Licence
--------

Public domain. Everyone is welcome to contribute!

Installation
--------------

ddeint can be installed by unzipping the source code in one directory and using this command: ::

    (sudo) python setup.py install
