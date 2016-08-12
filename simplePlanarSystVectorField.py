from numpy import *
import pylab as p

def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return array([ (0.4-0.1*X[1])*X[0] ,  
                  (0.005*(X[0])-0.3)*X[1] ])
                  
ymax = 15                       # get axis limits
xmax = 10 
nb_points   = 20                      

x = linspace(0, xmax, nb_points)
y = linspace(0, ymax, nb_points)

X1 , Y1  = meshgrid(x, y)                       # create a grid
DX1, DY1 = dX_dt([X1, Y1])                      # compute growth rate on the gridt

M = (hypot(DX1, DY1))                           # Norm of the growth rate 
M[ M == 0] = 1.                                 # Avoid zero division errors 
DX1 /= M                                        # Normalize each arrows
DY1 /= M 

# plot trajectories where X_f1 is a known fixed point
#for v, col in zip(values, vcolors): 
#    X0 = v * X_f1                               # starting point
#    X = integrate.odeint( dX_dt, X0, t)         # we don't need infodict here
#    p.plot( X[:,0], X[:,1], lw=3.5*v, color=col, label='X0=(%.f, %.f)' % ( X0[0], X0[1]) )
    

p.title('Trajectories and direction fields')
Q = p.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=p.cm.jet)
p.xlabel('X')
p.ylabel('Y')
p.legend()
p.grid()
p.xlim(0, xmax)
p.ylim(0, ymax)
p.show()