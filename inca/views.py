from flask import Flask,render_template,request,url_for,redirect
import json
from cassandra.cluster import Cluster
from inca.forms import SelCatForm,SelScatForm,SelInmForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

cluster = Cluster(['127.0.0.1','9042'])
session = cluster.connect()
session.set_keyspace("inca_test")

inm = ""
cancer = ""



@app.route("/")
def index():
    
    cqlink = "SELECT name,url FROM links"
    liens = session.execute(cqlink)  
    return render_template('index.html',liens=liens)

@app.route("/selection/") 
def selection():
    return render_template('search.html')




@app.route("/selection/cat/", methods=['post','get'])
def sel_cat():
    form1 = SelCatForm()
    return render_template('sel_cat.html',form1=form1)#,x=x)#,r=r,cp=cp,t=t)

@app.route("/selection/cat/scat/", methods=['get','post'])
def sel_scat():
    form1 = SelCatForm()
    form2 = SelScatForm()
    x = request.form['cat']
    r = session.execute("SELECT scatname from scats_by_cat where catname= "+"'"+str(x)+"'")
    cp = session.execute("SELECT count(scatname) from scats_by_cat where catname= "+"'"+str(x)+"'")
    t = cp[0][0]

    form2.scat.choices = [((r[0][0],r[0][0]))]
    for i in range(1,t):
       form2.scat.choices.append((r[i][0],r[i][0]))
    #form2.scat = SelectField(u'sous-categorie',choices=form2.scat.choices,validators=[])

    return render_template('sel_scat.html',form1=form1,form2=form2,x=x,r=r,cp=cp,t=t)

@app.route("/selection/inm" , methods=['get','post'])
def sel_inm():
    form2 = SelScatForm()
    form3 = SelInmForm()
    y = request.form['scat']
    # requete selection des inm   !!! aux nombres
    # requetes alphabetiques

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