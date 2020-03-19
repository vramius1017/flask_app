# coding utf8
import uuid
from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy

#declaration du cluser Cassandra local URL et nom du keyspace inca_test
app = Flask(__name__)
app.config['CASSANDRA_HOSTS']=['127.0.0.1:9042']
app.config['CASSANDRA_KEYSPACE'] = "inca_test"
db = CQLAlchemy(app)


# famille de colonnes  INM 
class Scats_by_cat(db.Model):
    idc = db.columns.Integer()
    catcode = db.columns.Integer(primary_key=True)
    catname = db.columns.Integer(primary_key=True)
    scatcode = db.columns.Integer(primary_key=True)
    scatname = db.columns.Integer(primary_key=True)
    
class Inms_by_scat(db.Model):
    idi = db.columns.Integer()
    catcode = db.columns.Integer(primary_key=True)
    catname = db.columns.Integer(primary_key=True)
    scatcode = db.columns.Integer(primary_key=True)
    scatname = db.columns.Integer(primary_key=True)
    charac = db.columns.Text(default="none")
    
        
    

    
        

    
