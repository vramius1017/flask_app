# coding utf8
import uuid
from flask import Flask
from flask_cassandra import CassandraCluster
from cassandra.cqlengine.columns import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
#declaration du cluser Cassandra local URL et nom du keyspace inca_test
app = Flask(__name__)
cassandra = CassandraCluster()

app.config['CASSANDRA_HOSTS']=['127.0.0.1:9042']
app.config['CASSANDRA_KEYSPACE'] = "inca_test"

# selection des apps 
class links(Models):
    __table_name__ = 'links'
    idap = columns.Integer(primary_key=True)
    name = columns.Text()
    url = columns.Text()
    
# famille de colonnes  INM 

class Scats_by_cat(Model):
    __table_name__ = 'scats_by_cat'
    
    
class Inms_by_scat(Model):
    id_inm = columns.Integer(primary_key=True,clustering_order="ASC") # Cluster Key
    catcode = columns.Integer(primary_key=True)
    catname = columns.Integer(primary_key=True)
    scatcode = columns.Integer(primary_key=True)
    scatname = columns.Integer(primary_key=True)
    charac = columns.Text(primary_key=True,default="none")


# famille de colonnes Desease
class Desease(Model):
    pass

class Cancer(desease):
    pass

class Diabetes(desease):
    pass

class Synom(Model):
    pass

class Localisation(Model):
    pass

# famille de colonnes publication 

class Meta(Model):
    pass

class Sok(Model):
    pass

class Sko(Model):
    pass

class samb(Model):
    pass

class Pub(Model):
    pass

class Nopub(Model):
    pass

# famille de colonnes admin_app

    
class User(Model):
    pass

class colab(Model):
    id_cob = columns.integer(primary_key=True)
    name_cob = columns.Text(required=True)
    pre_cob = columns.Text(required=True)
    mail_cob = columns.text(primary_key=True,clustering_order="ASC") 
    keycol = columns.Text(required=True)
    
        
def ConectCass():
     session = cassandra.connect()
     session.set_keyspace("inca_test") 


def SyncDb(cf):
     return sync_table(cf)      

if __name__ == '__main__':
    app.run()  
        

    
