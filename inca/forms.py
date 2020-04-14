from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
from flask import Flask,request

cluster = Cluster(['127.0.0.1','9042'])
session = cluster.connect()
session.set_keyspace("inca_test")

class SelCatForm(FlaskForm):
    
    cql = "SELECT catname FROM cat"
    r = session.execute(cql)
    a = (str(r[0][0]))
    b = (str(r[1][0]))
    c = (str(r[2][0]))
    d = (str(r[3][0]))
    e = (str(r[4][0]))
    cat = SelectField(u'categorie',choices = [(a,a),(b,b),(c,c),(d,d),(e,e)],validators=[])
    submit = SubmitField('Validation  cat')


class SelScatForm(FlaskForm):
    
    scat = SelectField(u'sous-categorie',choices=[],validators=[])
    submit2 = SubmitField('Validation scat')


class SelInmForm(FlaskForm):

    inm = StringField(u'intervention',validators=[])
    submit3 = SubmitField('Validation inm')
