
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.widgets import Slider
from numpy import (pi, tan, cos, sin, arctan, arccos, arcsin)

def prisme(n=1.5, A=pi/2, alpha1=pi/16):
    """
    Prend en Arguments:
        n : Indice du prisme (n=1.5 par défaut) : float
        A : Angle sommet du prisme (A=pi/2 par défaut) : float
        alpha1 : Angle d'incidence du rayon (alpha1=pi/16 par défaut) : float
    """
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
    
    prism.plot(x,y) #préciser sur quel axe tracer le prisme
    prism.add_patch(Polygon(([0,0],[-1*p,-1],[1*p,-1]), closed=True, fill=True, color='lightgrey'))


fig, axs = plt.subplots(3)

prism = axs[0]


# Curseurs
curseur_angleA = Slider(ax=axs[1], label='Angle A', valmin=pi/4, valmax=pi/2, valinit=pi/2)
curseur_alpha1 = Slider(ax=axs[2], label="Angle d'incidence", valmin=pi/4 , valmax= pi/3, valinit=pi/16)

prisme(A=pi/3, alpha1= pi/16)

def update(val):
    prisme(A=curseur_angleA.val, alpha1=curseur_alpha1.val)

curseur_angleA.on_changed(update)
curseur_alpha1.on_changed(update)


plt.show()
