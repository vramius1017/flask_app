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
   

###################################
#  affichage trials stats by DBs  #
###################################


# input : pmid list from MetaList()    output : dictionnaire stats 
def TrLs(pid):
    hind = Entrez.elink(db="pubmed",id=pid,cmd="neighbor_score")
    rec = Entrez.read(hind)
    return rec
# input  : result from TrLs(pid) a integer from Metacount()  output : print stats links by db  , link by pmid

def PubStatsLinks(result,a):
    ide = clean_data(result[a]["IdList"])
    print("pmid de la publication Cochrane: ",ide)
    cpl = 0
    for link in result[a]["LinkSetDb"]:
        cpl = cpl + 1
        print("nom du lien de cette publication dans pubmed ",link["LinkName"]," numéro du lien :",cpl)
        print("nombre de publications lié à cette publication Cochrane ",ide," dans ",link["LinkName"],": ",len(link["Link"]))

        
        print("-------------------------------------------------------------------------------")
    print(" nombre de liens concernés par cette publication :",cpl)    

# input:  pimd   output : datas
def DatasFromTid(pid):
    ha = Entrez.efetch(db="pubmed",id=pid,rettype="medline",retmode="text")
    resas = Medline.parse(ha)
    for res in resas:
        try:
            print("Title : ",res["TI"])
        except KeyError:
            print("pas de titre")
        try:
            print("PMID : ",res["PMID"]+", ",end="")
        except KeyError:
            print(" pas de pmid")
        try :     
            print("NLM identifier : ",res["JID"]+", ",end="")
        except:
            print(" pas NLM identifier")
        # catch error if no OID exist
        try:
            print("other identifier : ",res["OID"],end="")
        except KeyError :
            print("Other identifier : none ")
        # return all authors 
        try:
            r = clean_data(res["FAU"])
            print("Authors : ",r)
        except KeyError:
            au = clean_data(res["AU"])
            print("Authors :",au)
        # return MesH terms list
        try:
            mh = clean_data(res["MH"])
            print("MesH terms:")
            print(mh)
        except KeyError:
            print("MesH terms: none")
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
print("liste des publications Cochrane correspondant à la requête : \n",b)
c = MetaCount(g)
print(" nombre de publications Cochrane correspondant à la requête : ",c)
print(" ")
y = TrLs(b)
print(" ")
for jd in b:
    print("liste des essais cités dans la publication Cochrane ",jd)
    print("")
    for i in range (0,50):
        tid = y[1]["LinkSetDb"][0]["Link"][i]["Id"]
        DatasFromTid(tid)
        tsc = y[1]["LinkSetDb"][0]["Link"][i]["Score"]
        print("pmid :",tid,"  score :",tsc)
        print("")
    print("----------------------------------------------------------")     







