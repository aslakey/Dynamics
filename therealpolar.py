import numpy as np
import matplotlib.pyplot as plt
import math
import random
tBegin=0 #begin time
tEnd= 2 #end time
dt=.001 #step

t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin time to end with a step size of dt
N = t.size #measuring length of array
v = np.zeros(N) #returns array of length N filled with zeros
r = np.zeros(N) #^^
w = np.zeros(N)
theta = np.zeros(N)

v[0] = 0 #set initial velocity value
r[0] = .5 #set initial radius
theta[0]=0 #set in theta value
w[0]=0

for i in xrange(1,N):
    v[i] = v[i-1] + (2*t[i]+r[i-1]*w[i-1]**2)*dt
    r[i] = r[i-1] + v[i-1]*dt
    w[i] = w[i-1] + (math.cos(math.pi*t[i])-2*v[i-1]*w[i-1])/r[i-1]*dt
    theta[i] = theta[i-1] + w[i-1]*dt

ax = plt.subplot(111, polar=True) #this just allows you to make a new plot, for example subplot(112) would be a 1x1 plot for subplot 2
ax.plot(theta,r, color='r') #ploting x=theta y=r
ax.grid(True)
plt.show() #show plot