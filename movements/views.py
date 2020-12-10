from movements import app
from flask import render_template, request, url_for, redirect
import csv
import sqlite3

@app.route('/')

def listaIngresos():
    conn = sqlite3.connect('movements/data/datos.db')
    c = conn.cursor()
    
    c.execute('SELECT fecha, concepto, cantidad FROM movimientos;')
    ingresos=c.fetchall()
    sumador=0
    for ingreso in ingresos:
        sumador+= float(ingreso[2])
    conn.close()
    
    return render_template('movementsList.html', datos=ingresos, total=sumador)

@app.route('/creaAlta', methods=['GET', 'POST'])

def nuevoIngreso():
    if request.method == 'POST':
        conn = sqlite3.connect('movements/data/datos.db')
        c = conn.cursor()
        
        c.execute('INSERT INTO movimientos (cantidad, concepto, fecha) VALUES (?,?,?);' ,
                  (float(request.form.get('cantidad')),
                  request.form.get('concepto'),
                  request.form.get('fecha'))
        )
        
        conn.commit()
        conn.close()
        return redirect(url_for('listaIngresos'))
    return render_template("creaAlta.html")
