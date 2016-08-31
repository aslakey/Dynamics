#Design Spring System with lowest spring constant s.t. it damps out in two cycles
import numpy as np
import math
import matplotlib.pyplot as plt

#Mass = 5 kg
tBegin=0 #begin time
tEnd=10 #end time
dt=.001 #step

#Given:
mass = 5
uk= 0.2 #coeff kin friction
l = .2 #unstretched length
w = 9.81*mass*math.cos(math.pi/6) #weight
Normal = 9.81*mass*math.sin(math.pi/6)

t = np.arange(tBegin, tEnd, dt) #numpy makes an array from begin time to end with a step size of dt
N = t.size #measuring length of array

init_constant = 1 #spring constant
max_constant = 11
answer = 0
plot_index = N

for k in range(init_constant,max_constant):
    #initialize arrays
    x = np.zeros(N) #returns array of length N filled with zeros
    v = np.zeros(N) #^^^
    v[0] = 0 #set initial velocity value
    x[0] = 0 #set initial position value
    cycle = 0
    
    for i in range(1,N):
        sinTheta = x[i-1]/math.sqrt(l**2+x[i-1]**2)
        fk = 0 #friction set as 0 incase v was 0
        if v[i-1] != 0: #change friction accordingly
            fk = (-v[i-1])/(math.sqrt(v[i-1]**2))*uk*Normal 
        v[i] = v[i-1] + (w+fk-k/mass*(math.sqrt(l**2+x[i-1]**2)-l)*sinTheta)*dt 
        x[i] = x[i-1] + dt*v[i-1]
        
        if cycle==0 and x[i]<x[i-1]:
            cycle = 1
            print('cycle = ',cycle)
        if cycle == 1 and x[i]>x[i-1]:
            cycle = 1.5
            print('cycle = ',cycle)
        if cycle==1.5 and x[i]<x[i-1]:
            cycle = 2
            print('cycle = ',cycle)
        if cycle == 2 and np.abs(x[i]-x[i-1])<.00000001: #can stop here
            print('found answer:',k)
            answer = k
            plot_index = i
            break
        
    if answer!=0:
        ax = plt.subplot(111)
        ax.plot(t[:plot_index],x[:plot_index]) #ploting t on horizontal v x on vertical
        plt.show() #show plot
        break
    elif answer==0 and k==max_constant-1:
        print("Still bouncing, up the maximum spring constant")

