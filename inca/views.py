from flask import Flask,render_template,request,url_for
import json

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/selection/")
def selection():
    return render_template('search.html')

@app.route("/proposition/")
def proposition():
    return render_template('proposition.html')

@app.route("/validation/")
def valdate():
    return render_template('validate.html')