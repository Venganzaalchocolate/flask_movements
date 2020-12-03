from movements import app
from flask import render_template

@app.route('/')

def lisaMovimientos():
    return render_template('movementsList.html', miTexto="YA veremos")