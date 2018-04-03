import tkinter
import pylab as plt
import numpy as np
import math
import random

#radom.random mora da se generise tako da ide samo od-do gde je povrsina
#yrand je metak
#f(1000000) se mnozi sa brojem kockica koje su u okviru povrsine

root=tkinter.Tk()

def funkcija1(x):
    return 3*np.sin(x/4)*np.cos(x)

def nacrtaj():
    xmin = -15
    xmax = 15
    step = 0.01
    x = np.arange(xmin, xmax, step)
    plt.plot(x, funkcija1(x))
    plt.grid(True)
    plt.show()

nacrtaj()
root.mainloop()