# -*- coding: utf-8 -*-
from scipy.integrate import odeint
from pylab import *
# for plotting commands
def deriv(y,t):
    # return derivatives of the array y
    a =-90
    b =-100
    return array([ y[0],a*y[1]+b*y[0]**3])
    
time = linspace(0.0,10.0,1000)
yinit = array([10,0]) # initial values
y = odeint(deriv,yinit,time)
print y