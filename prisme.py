
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.widgets import Slider
from numpy import (pi, tan, cos, sin, arctan, arccos, arcsin)

def prisme(n=1.5, A=pi/4):
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

    if alpha2 < A/2 - pi/2:                 #si le rayon ne ressort pas
        x += [x1[1] + cos(alpha2)]
        y += [y1[1] + sin(alpha2)]
    else:                                   #si le rayon ressort
        t2 = tan(alpha2)
        x += [(x[1] * t2 - y[1])/(1/p+t2)]
        y += [y[1] + (x[2] - x[1]) * t2]

        if abs(n*sin(theta2prime)) < 1: # si pas de deformation totale
            theta2 = arcsin(n*sin(theta2prime))     #angle de réfraction
            alpha3 = theta2 + A/2
            x += [x[2] + cos(alpha3)]               #point P4
            y += [y[2] +sin(alpha3)]                 #point P4

    plt.plot(x,y)
    ax.add_patch(Polygon(([0,0],[-1*p,-1],[1*p,-1]), closed=True, fill=True, color='lightgrey'))

# Curseurs

fig, ax = plt.subplots()
ax_curseur = plt.axes([0.1, 0.1, 0.8, 0.03])
curseur_angle = Slider(ax=ax_curseur, label='Angle A', valmin=pi/4, valmax=pi/2, valinit=pi/2)

prisme(A=curseur_angle.val)

def update(val):
    n = 1.5
    prisme(n, curseur_angle.val)

curseur_angle.on_changed(update)


plt.axis('equal')
plt.show()