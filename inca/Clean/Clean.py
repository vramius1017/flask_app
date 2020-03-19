#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clean_data(x):
    chaine = str(x)
    chaine = chaine.replace("['"," ")
    chaine = chaine.replace("']"," ")
    chaine = chaine.replace("'"," ")
    return chaine


def clean_a(x):
    chaine = str(x)
    chaine = chaine.replace("/","")
    chaine = chaine.replace("*"," ")
    return chaine

def clean_date(x):
    import datetime
    md = datetime.datetime.strptime(x,"%Y%m%d").date()
    return md

