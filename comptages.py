#!/usr/bin/env python3
# -*- coding: utf8 -*-


import sys,os


os.system("clear")

if len(sys.argv)>1:
    repertoire = sys.argv[1]
else:
    repertoire = "."

print("repertoire = ",repertoire)
extensions = {}
files = {}
nbTotal = 0


def parcours (repertoire, depth) :
    global nbTotal
    print("   "*depth, repertoire)
    liste = os.listdir(repertoire)
    for fichier in liste :
        if os.path.isdir(repertoire+"/"+fichier) :
            parcours(repertoire+"/"+fichier, depth+1)
        
        else :
            chaines = fichier.split(".")
            lastExt = chaines[-1]
            if len(chaines) > 1 :
                if lastExt not in extensions:
                    extensions[lastExt] = 1
                    files[lastExt] = [fichier]
                else:
                    extensions[lastExt] += 1
                    files[lastExt].append(fichier)
                nbTotal += 1


parcours (repertoire, 0) # Appel initial de la fonction récursive

for (k,v) in extensions.items():
    print(k+": "+str(v)+" times \t", end="") 

print("Total files: ",nbTotal)
for ext in extensions:
    print(ext)
    for f in files[ext]:
        print("  ",f)
    #print("Extension:",k+" = ",files.values()) 



