#!/usr/bin/env python
# coding: utf-8

# In[28]:


#!/usr/bin/env python
# coding: utf-8

from Bio import Entrez
from Bio import Medline

##########################
#      module clean      #
##########################

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

###########################
#    connexion à PubMed   #
###########################

def ConPub():
    Entrez.api_key = "41843b992ded592334c39fe437c425e40608"
    Entrez.email = "sacha.torres@univ_montp3.fr"
    Entrez.tool = "Inca"
    print("connexion active !!!  Captain Picard from Enterprise-F")
    
###########################
#   module query          #
###########################

def Query():
    p = input("query pubmed :")
    pq = p + " "+"and Cochrane Database Syst Rev"
    return pq

def CorQuPub(q):
    han = Entrez.espell(term=q)
    rea = Entrez.read(han)
    return rea["CorrectedQuery"]
    
###########################
#  module Meta Cochrane   #
###########################
    
def MetaList(q):
    hend = Entrez.esearch(db="pubmed",term=q)
    ret = Entrez.read(hend)
    return ret["IdList"]

def MetaCount(q):
    hand = Entrez.esearch(db="pubmed",term=q)
    rec = Entrez.read(hand)
    return rec["Count"]    
 
def FetchIdList(ids):
    handle = Entrez.efetch(db="pubmed",id=ids,rettype="medline",retmode="text")
    record = Medline.parse(handle)
    return record   

###################################
#  affichage trials list by meta  #
###################################

def FetchIdList(ids):
    handle = Entrez.efetch(db="pubmed",id=ids,rettype="medline",retmode="text")
    record = Medline.parse(handle)
    return record


###########################
#  affichage datas metas  #
########################### 

def DatasFromIds(idlist):
    for res in idlist:
        print("Title : ",res["TI"])
        print("PMID : ",res["PMID"]+", ",end="")
        print("NLM identifier : ",res["JID"]+", ",end="")
        # catch error if no OID exist
        try:
            print("other identifier : ",res["OID"],end="")
        except KeyError :
            print("Other identifier : none ")
        # return all authors    
        r = clean_data(res["FAU"])
        print("Authors : ",r)
        # return MesH terms list
        mh = clean_data(res["MH"])
        print("MesH terms:")
        print(mh)
        # catch error if no OT exist
        try :
            print("Key Words: ",res["OT"])
        except KeyError:
            print("Key Words: none ")    
        # catch error if no source exist
        try:
            print("Publication source :","  ",res["SO"]) 
        except KeyError:
            print("Publication source : none")
        # return create date from pubmed   
        dt = clean_data(res["CRDT"])    
        print("Create Date : ",dt)
        # return revision date from pubmed
        revdt = clean_date(res["LR"])
        print("Revision Date :",revdt)
        print(" ")
        
        
        
        
        
# main ------------------------------------
ConPub()
a = Query()
g = CorQuPub(a) 
print("modified MeSH Terms query : ",g)
print("")
b = MetaList(g)
c = MetaCount(g)
print(" nb metas : ",c)
print(" ")
y = FetchIdList(b)
DatasFromIds(y)


# In[ ]:




