import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

ax = plt.axes([0.1, 0.15, 0.8, 0.8])
maligne, = ax.plot([0, 0.8], [0, 0.8], linewidth=1, color='black')

ax_curseur = plt.axes([0.25, 0.05, 0.6, 0.03])
moncurseur = Slider(ax_curseur, "lingueur", 0, 1, valinit=0.8)

def update(event) :
    longueur = moncurseur.val
    maligne.set_data([0, longueur], [0, longueur])
    plt.draw()
moncurseur.on_changed(update)
plt.show()
