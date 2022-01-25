
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from numpy import (pi, tan, cos, sin, arctan, arccos, arcsin)

n = 1.5 # indice de réfraction
A = 3*pi/4   # angle d'ouverture du prisme
alpha1 = pi/16 # pente du rayon incident
p = tan(A/2) #on aura besoin de cette grandeur plusieurs fois

theta1 = alpha1 + A/2               #angle d'incidence sur face 1
theta1prime = arcsin(sin(theta1)/n) #angle de réfraction
alpha2 = theta1prime -A/2       #pente du rayon intérieur
theta2prime = alpha2 - A/2

y1 = -0.5                               #point P2
x1 = y1*p                               #point P2
x0, y0 = x1-cos(alpha1), y1-sin(alpha1) #point P1
x = [x0,x1]                             #rayon P1P2
y = [y0,y1]                             #rayon P1P2
t2 = tan(alpha2)                        #raccourci

if abs(n*sin(theta2prime)) < 1:
    theta2 = arcsin(n*sin(theta2prime))     #angle de réfraction
    alpha3 = theta2 + A/2
    x += [x[2] + cos(alpha3)]               #point P4
    y += [y[2]+sin(alpha3)]                 #point P4

fig, ax = plt.subplots()
plt.plot(x,y)
ax.add_patch(Polygon(([0,0],[-1*p,-1],[1*p,-1]), closed=True, fill=True, color='lightgrey'))

plt.axis('equal')
plt.show()