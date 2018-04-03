from flask import Flask, render_template, redirect, url_for, request
import dekorator
import povrsinaIGrafik
import genetskiAlgoritam

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("ispitni_zadaci.html")


@app.route('/z1')
def z1():
    poruke = dekorator.mainEntry()
    return render_template("z1.html", txt=poruke)


@app.route('/z2')
def z2():
    poruka = povrsinaIGrafik.mainEntry()
    return render_template("z2.html", txt=poruka)

@app.route('/nacrtaj')
def nacrtaj():
    povrsinaIGrafik.nacrtaj()
    poruka = povrsinaIGrafik.mainEntry()
    return render_template("z2.html", txt=poruka)


@app.route('/z3')
def z3():
    poruka = genetskiAlgoritam.glavnaPetlja()
    return render_template("z3.html", txt=poruka)

@app.route('/prikaziTackasto')
def prikaziTackasto():
    genetskiAlgoritam.prikazi()
    poruka = genetskiAlgoritam.glavnaPetlja()
    return render_template("z3.html", txt=poruka)

if __name__ == '__main__':
    app.run()