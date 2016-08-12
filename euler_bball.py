import numpy as np
import matplotlib.pyplot as plt
import math
import random
tBegin=0 #begin time
tEnd= 2 #end time
dt=.001 #step
theta= 34 #launch angle in degrees
theta = theta * math.pi/180. # convert launch angle to radians
t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin time to end with a step size of dt
N = t.size #measuring length of array
x = np.zeros(N) #returns array of length N filled with zeros
v = np.zeros(N) #^^^
y = np.zeros(N) #^^

v[0]=30 #set initial velocity value
x[0] = -20 #set initial x-position value
y[0] = 7 #set initial y-pos value

for i in xrange(1,N):
    y[i] = y[0]+v[0]*(math.sin(theta))*t[i] + (-16.1*t[i]**2) #y position
    x[i] = x[0]+v[0]*math.cos(theta)*t[i] #x position
    if x[i] > 0:
        break
ax = plt.subplot(111) #this just allows you to make a new plot, for example subplot(112) would be a 1x1 plot for subplot 2
ax.plot(x,y) #ploting x on horizontal v y on vertical
plt.show() #show plot
