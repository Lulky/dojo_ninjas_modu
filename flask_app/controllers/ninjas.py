from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models import dojo, ninja 

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos=dojo.Dojo.muestra_dojos())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.guardar_ninja(request.form)
    return redirect('/')