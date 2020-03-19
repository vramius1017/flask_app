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
    idc = db.columns.Integer() # cluster Key
    catcode = db.columns.Integer(primary_key=True)
    catname = db.columns.Integer(primary_key=True)
    scatcode = db.columns.Integer(primary_key=True)
    scatname = db.columns.Integer(primary_key=True)
    
class Inms_by_scat(db.Model):
    idi = db.columns.Integer() # Cluster Key
    catcode = db.columns.Integer(primary_key=True)
    catname = db.columns.Integer(primary_key=True)
    scatcode = db.columns.Integer(primary_key=True)
    scatname = db.columns.Integer(primary_key=True)
    charac = db.columns.Text(primary_key=True,default="none")


# famille de colonnes Desease
class Desease(db.Model):
    pass

class Cancer(db.Model):
    pass

class Diabetes(db.Model):
    pass

class Synom(db.Model):
    pass

class Localisation(db.Model):
    pass

# famille de colonnes publication 

class Meta(db.Model):
    pass

class Sok(db.Model):
    pass

class Sko(db.Model):
    pass

class samb(db.Model):
    pass

class Pub(db.Model):
    pass

class Nopub(db.Model):
    pass

# famille de colonnes admin_app

    

    
        
    

    
        

    
