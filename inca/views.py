from flask import Flask,render_template,request,url_for
import json

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def index():
    links=["www.inmcancer.fr","www.niri.fr","www.nishare.fr"]    
    return render_template('index.html', links=links)

@app.route("/selection/")
def selection():
    return render_template('search.html')

@app.route("/proposition/")
def proposition():
    return render_template('proposition.html')

@app.route("/validation/")
def validate():
    return render_template('validate.html')


@app.route("/divers/")
def   divers():
    return  render_template('divers.html')  