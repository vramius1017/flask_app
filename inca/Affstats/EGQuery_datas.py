#!/usr/bin/env python
# coding: utf-8

# In[1]:


##########################################
# module affstats                        #
# nb de publications par bases de Medline#
##########################################
from Bio import Entrez
from Bio import Medline

def ConPub():
    Entrez.api_key = "41843b992ded592334c39fe437c425e40608"
    Entrez.email = "sacha.torres@univ_montp3.fr"
    Entrez.tool = "Inca"
    print("connexion active !!!")
    
def EGQuery(t):
    handle = Entrez.egquery(term=t)
    record = Entrez.read(handle)
    return record
    
ConPub()  
te = input("entrer un terme: ")
print("")
for row in EGQuery(te)["eGQueryResult"]:
    print(row["DbName"],row["Count"])


# In[ ]:




