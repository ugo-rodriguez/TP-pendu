
#header 
#Faire un pendu
#27/11/2020
#Martin Rodriguez
#ToDo: afficher le score, voir si ca marcge avec des sauts de ligne dans el fichier

#bibliothèques

from fonctions import jeu 

#on crée la liste de mots
fichier=open("mots.txt",'r')

liste_mots=[]
for ligne in fichier:
    liste_mots.append(ligne)

fichier.close()

mots_pendu=liste_mots[0].split(" ")

#liste des mots proposés au joueur 



#on initialise le score max
score_max=0

#le jeu commence
jeu(mots_pendu,score_max)















    






    

            
            

            

            
    
    
    
    
    
    
    
    
    



