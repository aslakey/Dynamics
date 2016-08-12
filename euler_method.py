import numpy as np
import matplotlib.pyplot as plt
import math
import random
 
tBegin=0 #begin time
tEnd=.3  #end time
dt=.001  #step
 
t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin time to end with a step size of dt
N = t.size #measuring length of array
 
x = np.zeros(N) #returns array of length N filled with zeros
v = np.zeros(N) #^^^

v[0]=0 #set initial velocity value
x[0] = 0 #set initial position value

for i in xrange(1,N):
    v[i] = v[i-1] - dt*(90*v[i-1]+100*(x[i-1]**3))    #new velocity = old v + dt * acc
    x[i] = x[i-1] + dt*v[i-1]                         #new pos = old pos + dt* old v
 
ax = plt.subplot(111)    #this just allows you to make a new plot, for example subplot(112) would be a 1x1 plot for subplot 2
ax.plot(t,x)             #ploting t on horizontal v x on vertical
plt.show()               #show plot