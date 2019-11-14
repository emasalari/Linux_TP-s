#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, json, re
from flask import Flask
app = Flask(__name__)

# 
# @app.route("/recherche/<critere>")
# def recherche_critere(critere):
#     print("/recherche/"+critere)
#     lignes = []
#     liste = os.listdir("PAGES") 
#     for fichier in liste :
#         fd = open("PAGES/"+fichier)
#         print(fichier)
#         contenu = fd.read()  # lecture du fichier comme une seule ligne
#         contenu = contenu.replace('\n', '')
#         entreprises = re.findall("(\|\d+\..+?\|-)", contenu)
#         for entr in entreprises :
#             print(entr)
#             print("------------------------------------------------")
#         #print(contenu)
#            
#     return json.dumps(lignes)

@app.route("/recherche/<critere>")
def recherche_critere(critere):
    print("/recherche/"+critere)
    lignes = []
    liste = os.listdir("PAGES") 
    for fichier in liste :
        fd = open("PAGES/"+fichier)
        print(fichier)
        contenu = fd.readlines()  
        start = re.search("{| class=\"wikitable sortable\"" , ligne)
        end = re.search("</tbody></table>" ,ligne)
        for ligne in contenu:
            if (start):
                with open (critere,"w") as ff:
                    while (ligne != end)
                        ff.write(ligne)

app.run()
