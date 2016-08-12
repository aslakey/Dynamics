import numpy as np
import matplotlib.pyplot as plt
import math
import random
tBegin=0 #begin time
tEnd= 2 #end time
dt=.001 #step
#theta= 34 #launch angle in degrees
#theta = theta * math.pi/180. # convert launch angle to radians
t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin time to end with a step size of dt
N = t.size #measuring length of array
x = np.zeros(N) #returns array of length N filled with zeros
y = np.zeros(N) #^^

x[0] = 2*math.cos(math.sin(math.pi*0)) #set initial x-position value
y[0] = 2*math.sin(math.sin(math.pi*0)) #set initial y-pos value

for i in xrange(1,N):
    y[i] = 2*math.sin(math.sin(math.pi*t[i]))#y pos
    x[i] = 2*math.cos(math.sin(math.pi*t[i])) #x position

ax = plt.subplot(111) #this just allows you to make a new plot, for example subplot(112) would be a 1x1 plot for subplot 2
ax.plot(x,y) #ploting t on horizontal v x on vertical
plt.show() #show plot