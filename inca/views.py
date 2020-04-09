from flask import Flask,render_template,request,url_for
import json
from cassandra.cluster import Cluster
from inca.forms import SelCatForm,SelScatForm
from config import Config
from wtforms import StringField,SelectField,SubmitField

app = Flask(__name__)
app.config.from_object(Config)
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

@app.route("/selection/cat/",methods=['get','post'])
def sel_cat():
    form = SelCatForm()

    cql = "SELECT scatname FROM scats_by_cat where catcode = 1" 
    cq = session.execute(cql)
    s1 = str(cq[0][0])
    s1 = str(cq[0][0])
    s1 = str(cq[0][0])
    form2 = SelScatForm()
    form2.scat = SelectField(u'subcategory',choices=[('sc1',1),('sc2',2),('sc3',3)],validators=[])
    return render_template('sel_cat.html',form=form,form2=form2)

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