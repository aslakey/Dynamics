#Problem 2: What is the velocity if a golfer can hit a 300 yard drive at 9 degrees

import numpy as np
import matplotlib.pyplot as plt
import math
import random

tBegin=0 #begin time
tEnd= 3 #end time
dt=.001 #step
t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin time to end with a step size of dt
N = t.size #measuring length of array

theta= 9 #launch angle in degrees
theta = theta * math.pi/180. # convert launch angle to radians

#Find the first velocity at which y does not go negative
answer=0
for v_init in range(50,1000):
    x = np.zeros(N) #returns array of length N filled with zeros
    y = np.zeros(N) #^^
    
    x[0] = -900 #set initial x-position value
    y[0] = 0 #set initial y-pos value
    end=0
    for i in range(1,N):
        y[i] = y[0]+v_init*(math.sin(theta))*t[i] + (-16.1*t[i]**2)   #y position
        x[i] = x[0]+v_init*math.cos(theta)*t[i] 			       #x position
        if x[i]>=0:
            end = i
            break
    if y[end] > 0: #the gold ball made it
        answer = v_init
        break
    
print(answer)    #307 m/s         
