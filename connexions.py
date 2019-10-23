#!/usr/bin/env python3
# -*- coding: utf8 -*-


import sys,os,re


os.system("clear")
os.system("last -w > last.txt")


with open("last.txt", "r") as f:
    lines = f.readlines()

# régulière qui extrait : le login
def login():
    with open("connexions_login.txt", "w") as f:
        i = 1
        for line in lines:
            # Find the lines that have at least one "@" in it.
            if re.search(r'.@', line):
                j = str(i)
                # take the part before "@" as a username
                login = re.split("@",line)
                f.write(j+". "+login[0]+"\n")
                print(line, " is recorded.")
                i +=1
            else:
                print(line," I didn't find anything on this line")
        
# régulière qui extrait : le nom du mois et le numéro du jour dans le mois (la date)

def dayAndMonth():
    with open("connexions_dayAndMonth.txt", "w") as f:
        i = 1
        for line in lines:
            # Find the lines that have at least one "@" in it.
            if re.search(r'.@', line):
                j = str(i)
                # take the part before "@" as a username
#                date = re.split(" ",line)
#                ourDate = date[:6]
                myRE = line.strip(':')
                print(j+". "+line[:-1],"\t stripped =====> ",myRE)
                
                
#                f.write(j+". "+ourDate+"\n")
#                print(line, " is recorded.")
                i +=1
#            else:
#                print(line," I didn't find the date on this line")
   












# régulière qui extrait : le nombre d’heures
# régulière qui extrait : le nombre de minutes et affichez ces informations
# régulière qui Affichez: le nombre de connexions par login (via un dictionnaire)
# régulière qui Affichez: le nombre de connexions et le temps de connexions (en minutes) par login (via un dictionnaire de listes)
# régulière qui Affichez: puis par login et par date (via un dictionnaires de dictionnaires de listes)
# Suivant des paramètres indiquant un nombre maximal de connexions et/ou un temps de connexion cumulé maximal, affichez des alertes !


# un script python qui liste les jours de connexion des utilisateurs qui ont fréquenté cette machine
# (en sachant que vous désirez surveiller les (mauvaises) fréquentations de celle-ci).
# pompidor s’est connecté les : 25 septembre (1 fois), 24 septembre (1 fois), 23 septembre (4 fois)
# meynard s’est connecté les : 24 septembre (1 fois), 23 septembre (1 fois)


#login()
dayAndMonth()








