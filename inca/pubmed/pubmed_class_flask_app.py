#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# alignement requete + lists id + list meta + trials from meta par id


from Bio import Entrez
from Bio import Medline


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

def ConPub():
    Entrez.api_key = "41843b992ded592334c39fe437c425e40608"
    Entrez.email = "sacha.torres@univ_montp3.fr"
    Entrez.tool = "Inca"
    print("connexion active !!!")

def Query():
    p = input("query pubmed :")
    pq = p + " "+"and Cochrane Database Syst Rev"
    return pq

def CorQuPub(q):
    han = Entrez.espell(term=q)
    rea = Entrez.read(han)
    return rea["CorrectedQuery"]

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
    #code jinja pour la liste des données dans le dictionnaire
    #for re in record:
    #    titre : re["TI"]
    #   r = clean_data(re["FAU"])
    #    auteurs : r
        
def TrFromMeta(mid):
    handlle = Entrez.elink(db="pubmed",id=mid,cmd="prlinks")
    result = Entrez.read(handlle)
    print(result[0]["LinkSetDb"])
    return result
    
def DataDbs():
    pass
    
ConPub()
a = Query()
CorQuPub(a)
b = MetaList(a)
c = MetaCount(a)

print(" nb metas : ",c)
print(" ")
for res in FetchIdList(b):
    print("Title : ",res["TI"])
    print("PMID : ",res["PMID"]+", ",end="")
    print("NLM identifier : ",res["JID"]+", ",end="")
    try:
        print("other identifier : ",res["OID"],end="")
    except KeyError :
        print("Other identifier : none ")
    r = clean_data(res["FAU"])
    print("Authors : ",r)
    mh = clean_data(res["MH"])
    print("MesH terms:")
    print(mh)
    try :
        print("Key Words: ",res["OT"])
    except KeyError:
        print("Key Words: none ")
    try:
        print("Publication source :","  ",res["SO"]) 
    except KeyError:
        print("Publication source : none")
    dt = clean_data(res["CRDT"])    
    print("Create Date : ",dt)
    revdt = clean_date(res["LR"])
    print("Revision Date :",revdt)
    print(" ")
for res in  FetchIdList(b):
    print("Trials list linked with pmid ",res["PMID"]+":  ",TrFromMeta(res["PMID"]))
    print("#######################################################################################################################################################################")    
#id=31264709
#print(TrFromMeta(id))
#print("")


# In[ ]:


pmid = 29360138
TrFromMeta(pmid)


# In[ ]:


# données sur les citations de la meta analyse ou de l'article 


from Bio import Entrez ,Medline
def ConPub():
    Entrez.api_key = "41843b992ded592334c39fe437c425e40608"
    Entrez.email = "sacha.torres@univ_montp3.fr"
    Entrez.tool = "Inca"
    print("connexion engaged Captain Picard !!!")
    print("")
    
def clean_data(x):
    chaine = str(x)
    chaine = chaine.replace("['"," ")
    chaine = chaine.replace("']"," ")
    chaine = chaine.replace("'"," ")
    return chaine    

def PubStats():
    pmid = input("entrer un pmid : ")# faire un test sur est un entier ou est un potentiel pmid 
    handle = Entrez.elink(db="pubmed",id=pmid)
    record = Entrez.read(handle)
    return record
def PubLink():
    pass


ConPub()
record = PubStats()

# print("DB origine : ",record[0]["DbFrom"])
# print(" pmid de la publication : ",record[0]["IdList"])

links = record[0]["LinkSetDb"]
for link in links:
    print(link["DbTo"],link["LinkName"]," ",len(link["Link"]))
print("")    
############################################ 

# pubmed pubmed_pubmed   
# pubmed pubmed_pubmed_alsoviewed   
# pubmed pubmed_pubmed_citedin  
# pubmed pubmed_pubmed_combined   
# pubmed pubmed_pubmed_five   6 
# pubmed pubmed_pubmed_refs   61 
# pubmed pubmed_pubmed_reviews   169 
# pubmed pubmed_pubmed_reviews_five  

# il manque pubmed_assembly , pubmed_bioproject , pubmed_biosystems , pubmed_biosample , pubmed_cancerchromosomes
############################################
#for i in links:
#   print("pubmed_pubmed :  ",end="")
#    print(record[0]["LinkSetDb"][0]["Link"])
#    print("-------------------------------------")
#    print("pubmed_pubmed_alsoviewed :  ",end="")
#    print(record[0]["LinkSetDb"][1]["Link"])# on accede au type de lien par le deuxieme indice
#print("")

# pour afficher les pmid selon le type de lien 
#ids = record[0]["LinkSetDb"][4]["Link"]
#for link in ids:
#    print(link["Id"]," ",end="")
    


# In[52]:


import datetime
madate = "20201005"
md = datetime.datetime.strptime(madate,"%Y%m%d").date()
print(md)


# In[ ]:




