import time
from functools import wraps

n = 1
suma = 0
brojac = 0
flask_poruka1 = ''
flask_poruka2 = ''
flask_poruka3 = ''
flask_poruka4 = ''


def dekor(func):
    @wraps(func) #ocuvanje metapodataka funkcije
    def wrapper(*args, **kwargs):
        vremeUlaska = 0
        global brojac
        global flask_poruka1
        global flask_poruka3
        global flask_poruka4
        if (brojac == 0):
            vremeUlaska = time.time()
            vremeUlaskaFormatirano = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(vremeUlaska))
            flask_poruka1 = str("Ime funkcije: %s, vreme ulaska u funkciju: %s" % (func.__name__, vremeUlaskaFormatirano))
            #print("Ime funkcije: %s, vreme ulaska u funkciju: %s" %(func.__name__, vremeUlaskaFormatirano))  # ispisuje naziv funkcije i vreme ulaska
        result = func(*args, **kwargs) #svi argumenti
        if (brojac == 6):
            brojac += 1
            vremeIzlaska = time.time()
            vremeIzlaskaFormatirano = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(vremeIzlaska))
            flask_poruka3 = str("Ime funkcije: %s, vreme izlaska iz funkcije: %s" % (func.__name__, vremeIzlaskaFormatirano))
            flask_poruka4 = str("Vreme provedeno u funkciji: %s" % ((vremeIzlaska - vremeUlaska) / 100000000 / 60))

            #print("Ime funkcije: %s, vreme izlaska iz funkcije: %s" %(func.__name__, vremeIzlaskaFormatirano))  # ispisuje vreme izlaska
            #print("Vreme provedeno u funkciji: %s" %((vremeIzlaska-vremeUlaska)/100000000/60))  # ispisuje vreme provedeno u funkciji
        return result
    return wrapper

@dekor
def izracunajSumu(n, sign):
    global brojac
    brojac +=1
    if(brojac<6):
        global suma
        suma += (n**2)*sign
        poruka = "*** n = " + str(n) + " Suma: " + str(suma)
        global flask_poruka2
        flask_poruka2 += poruka + ' '
        n += 1
        if(sign == -1):
            sign = 1
        else:
            sign = -1
        izracunajSumu(n, sign)


def mainEntry():
    izracunajSumu(1, 1)
    return (flask_poruka1, flask_poruka2, flask_poruka3, flask_poruka4)


