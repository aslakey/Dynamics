import matplotlib.pyplot as plt
import math
import random
import numpy as np

tBegin=0 #begin theta
tEnd=6  #end theta
dt=.1  #step
 
t = np.arange(tBegin, tEnd, dt)
N = t.size
w = np.zeros(N)
#variables:
v=.2
l=2
r=.5

wd = np.array([0,0,-.4])  
b = np.array([0,1,0])  
print np.cross(wd,b)

