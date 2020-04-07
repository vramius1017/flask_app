from flask import Flask,render_template,request,url_for
import json
from cassandra.cluster import Cluster

app = Flask(__name__)
app.config.from_object('config')
cluster = Cluster(['127.0.0.1','9042'])
session = cluster.connect()
session.set_keyspace("inca_test")

@app.route("/")
def index():
    cqlink = "SELECT name,url FROM links"
    liens = session.execute(cqlink)  
    return render_template('index.html',liens=liens)

@app.route("/selection/")
def selection():
    return render_template('search.html')

@app.route("/selection/scat")
def sel_scat():
    pass

@app.route("/selection/cat/")
def sel_cat():
    cqcat = "SELECT catname FROM cat"
    cats = session.execute(cqcat)
    resc = request.form
    qcat = resc['name']
    cqscat = "select * from scats_by_cat where catname = 'Psychological health intervention'" # +str(qcat)
    scats = session.execute(cqscat)
    return render_template('sel_cat.html',cats=cats,scats=scats)



@app.route("/selection/inm")
def sel_inm():
    pass

@app.route("/proposition/")
def proposition():
    return render_template('proposition.html')

@app.route("/validation/")
def validate():
    return render_template('validate.html')


@app.route("/divers/")
def   divers():
    return  render_template('divers.html')  


@app.route("/404/")
def PageError():
    error="Page 404"
    return render_template('404.html',error=error)


@app.route("/travaux/")
def PageTravaux():
    error = "Page en travaux"
    im = url_for('static',filename='img/tr.jpg')
    return render_template('travaux.html',error=error,im=im)