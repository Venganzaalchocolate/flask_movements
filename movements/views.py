from movements import app
from flask import render_template
import csv

@app.route('/')

def listaIngresos():
    fingresos = open("movements/data/ingresos.csv", 'r')
    csvReader = csv.reader(fingresos, delimiter=',', quotechar='"')
    ingresos = list(csvReader)
    
    print(ingresos)
    
    return render_template('movementsList.html', datos=ingresos)