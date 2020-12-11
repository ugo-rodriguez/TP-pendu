

#header 
#Faire un pendu ( partie fonction )
#27/11/2020
#Martin Rodriguez
#ToDo: 
    
    
import random as rd


#commencer a faire interagir l'utilisateur
def progression_mot_deviner(liste_lettre_restante,mot_deviner,chance,lettre_essaye):
    
    #annonce des chances restantes
    print("il vous reste "+str(chance)+" "+"chances")
    
    #annonce des lettres deja utilisées
    lettre_utilise=""
    for i in lettre_essaye:
       lettre_utilise+=i+", "
    print("vous avez déjà utilisé les lettres : "+lettre_utilise)
    
    #choix de la letter par l'utilisateur
    choix_lettre=input("rentrez une lettre  : ")
    lettre_essaye.append(choix_lettre)
    
    
    #mise a jour de la liste des lettres restantes et du mot a deviner
    indice_lettre_a_enlever=[]
    for k in range(len(liste_lettre_restante)):
        if liste_lettre_restante[k][0]==choix_lettre:
            indice_lettre_a_enlever=[k]+indice_lettre_a_enlever
            
    if indice_lettre_a_enlever==[]:
        print("Fichtre, c'est raté")
        chance-=1
            
    for i in indice_lettre_a_enlever:
        mot_deviner[liste_lettre_restante[i][1]]=liste_lettre_restante[i][0]
        liste_lettre_restante.pop(i)
    return liste_lettre_restante,mot_deviner,chance,lettre_essaye  







#transformation mot deviner en chaine de caractères

def affichage_mot(mot_deviner):
    res=""
    for i in mot_deviner:
        res+=i+" "
    return res
    


#la fontion du jeu
def jeu(mots_pendu,score_max):
    
    #on choisi un mot parmi la liste
    mot_choisi=mots_pendu[rd.randint(0, len(mots_pendu)-1)]
    
    
    
    #separation du mot en toute ses lettres
    liste_lettre=[]
    for lettre in mot_choisi:
        liste_lettre.append(lettre)
    
    
    #création mot secret
    
    mot_deviner=[liste_lettre[0]]
    for i in range (1,len(liste_lettre)):
        mot_deviner.append("_")
        #on affiche dès le début au joueurs les tirets et les letter identiques a la première
        if liste_lettre[i]==liste_lettre[0]:
            mot_deviner[i]=mot_deviner[0]
        if liste_lettre[i]=="-":
            mot_deviner[i]="-"
    
    
    
    #création de la liste des lettre restantes du mot
    liste_lettre_restante=[]
    for k in range(1,len(liste_lettre)):
        
        
        if ((liste_lettre[k] != "-") and (liste_lettre[k] != liste_lettre[0])):
            liste_lettre_restante.append([liste_lettre[k],k])
            #liste de liste avec pour chaque sous liste le premier élement
            #qui correspond a la lettre restante et le deuxième sa position dans le mot
            
    
    
    

    chance=8
    lettre_essaye=[]
    mot_deviner_afficher=affichage_mot(mot_deviner)
    print(mot_deviner_afficher+"\n")
    
    
    while chance>0 and liste_lettre_restante!=[]:
    #le jeu s'arrete si il n'a plus de chance 
    #ou si la liste des lettres restantes est vide c'est a dire
    #que l'utilisateur a trouvé le mot en entier
        
        #on appelle la fonction progression mot deviner qui fait avancer le jeu étape par étape
        liste_lettre_restante,mot_deviner,chance,lettre_essaye=progression_mot_deviner(liste_lettre_restante, mot_deviner,chance,lettre_essaye)
       
    
        #on appelle la fonction affichage mot pour afficher a l'utilisateur l'avancement du mot
        mot_deviner_afficher=affichage_mot(mot_deviner)
        print(mot_deviner_afficher+"\n")
        
    
    score_max=max(score_max,chance)#mise a jour du score max
    print("Votre score max est : "+str(score_max))
    
    #on propsoe a l'utilisateur de rejouer
    rejouez=input("Voulez vous rejouez? (oui ou non) : ")
    if (rejouez=="oui"):
        jeu(mots_pendu,score_max)
    
    
    