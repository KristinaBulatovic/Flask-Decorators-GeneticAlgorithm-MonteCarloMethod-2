import tkinter
import pylab as plt
import numpy as np
import random

root=tkinter.Tk()

flask_poruka = ""

def f(n):
    pog = 0;
    for i in range(n):
        xrand = 2 + random.random()*4
        yrand = random.random()*5
        if ((((-(xrand**2)/2)+(5*xrand)-8)>(yrand)) and ((1/4*((xrand-4)**3)+2)<yrand)):
            pog+=1
    return(pog/n)

flask_poruka += "Broj gadjanja Površina" + "\n"
flask_poruka += '{:>10d} {:<5.4}'.format(1000000, f(1000000)*20)

print("Broj gadjanja Površina")
print('{:>10d} {:<5.4}'.format(1000000,f(1000000)*20))

def funkcija1(x):
    return (1/4*((x-4)**3)+2)

def funkcija2(x):
    return ((-(x**2)/2)+(5*x)-8)

def nacrtaj():
    xmin = 0
    xmax = 7
    step = 0.01
    x = np.arange(xmin, xmax, step)
    plt.plot(x, funkcija1(x), x, funkcija2(x))
    plt.grid(True)
    plt.axis([0,7,0,7])
    plt.show()

def mainEntry():
    return flask_poruka