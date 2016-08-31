import numpy as np
import matplotlib.pyplot as plt
import math

'''
Problem 1: Basketball
A Basketball player shoots from 20 feet away.
He releases the ball at 7 feet, and 
shoots with an initial velocity of 30m/s
What angle should he shoot to make the basket?
'''
#Set up array of time for derivatives
tBegin=0 #begin time
tEnd= 2 #end time
dt=.001 #step

t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin time to end with a step size of dt
N = t.size #measuring length of array


#initial amgles and answers
angle = 0
make_angles=[]

while angle < 90:
    
    theta = angle * math.pi/180. # convert launch angle to radians

    #initialize shot arrays
    x = np.zeros(N) #returns array of length N filled with zeros
    v = np.zeros(N) #^^^
    y = np.zeros(N) #^^
    
    v[0]=30 #set initial velocity value
    x[0] = -20 #set initial x-position value
    y[0] = 7 #set initial y-pos value
    
    end=0
    for i in range(1,N):
        y[i] = y[0]+v[0]*(math.sin(theta))*t[i] + (-16.1*t[i]**2) #y position
        x[i] = x[0]+v[0]*math.cos(theta)*t[i] #x position
        #break when x reaches the goal
        if x[i] >= 0:
            end=i
            break
    if np.abs(y[end] - 10)<=.05: #Its a make (with some room for error)!
        make_angles.append(angle)
        '''
        If you want to plot the shot:
        ax = plt.subplot(111) #this just allows you to make a new plot, for example subplot(112) would be a 1x1 plot for subplot 2
        ax.plot(x,y) #ploting x on horizontal v y on vertical
        plt.show() #show plot'''
        
    angle+=.1
    
print(make_angles) #ANSWER = 33.9 and 64.8 degrees


