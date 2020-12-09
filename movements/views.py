from movements import app
from flask import render_template, request
import csv

@app.route('/')

def listaIngresos():
    fingresos = open("movements/data/ingresos.csv", 'r')
    csvReader = csv.reader(fingresos, delimiter=',', quotechar='"')
    ingresos = list(csvReader)
    
    sumador=0
    for ingreso in ingresos:
        sumador+= float(ingreso[2])
    
    return render_template('movementsList.html', datos=ingresos, total=sumador)

@app.route('/creaAlta', methods=['GET', 'POST'])

def nuevoIngreso():
    if request.method == 'GET':
        print ('soy un get')
    else:
        print ('soy un post')
    return render_template("creaAlta.html")
