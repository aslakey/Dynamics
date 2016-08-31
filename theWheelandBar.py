import numpy as np
import matplotlib.pyplot as plt
import math
import random
 
tBegin=0 #begin theta
tEnd=10  #end theta
dt=.1  #step
 
t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin theta to end with a step size of dt
N = t.size #measuring length of array
 
B = np.zeros(N) #returns array of length N filled with zeros
W = np.zeros(N) #^^^


for i in range(1,N):
    B[i] = math.asin((.5+.25*math.sin(t[i]))/2)    #angle beta=arcsin (opp/hyp)
    W[i] = (.1*math.cos(t[i]))/(2*math.cos(B[1])) #omega = Vay/(length*cosB)
 
ax = plt.subplot(111)    #this just allows you to make a new plot, for example subplot(112) would be a 1x1 plot for subplot 2
ax.plot(t,W)             #ploting t on horizontal, W on vertical
plt.show()      