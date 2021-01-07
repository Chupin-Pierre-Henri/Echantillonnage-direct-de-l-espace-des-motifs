import math
import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

# cela permet de charger le fichier
# On fait en sorte de modifier les données en les convertissant en int pour les utiliser plus facilement
def upload_file(nom_fichier):
    fichier = open(nom_fichier)
    data = []
    for ligne in fichier:
        #ici le split permet de s'éparer le string en list
        nouvelle_valeur = [int(x) for x in ligne.split()]
        data.append(nouvelle_valeur)
    return data

def motifs_doublon(motif_Unique, motifs):
    for i in motifs:
        if i not in motif_Unique:
            return False # il n'est pas en double
    return True # il est en double


def calcul_frequence_algo_frequence(dataset):
    for i in dataset:
        w_FBased.append(math.pow(2,abs(len(i))))
    for j, val in enumerate(w_FBased):
        f_FBased.append(val/sum(w_FBased))
    return f_FBased

def algorithme_frequence(dataset):
    double = True
    motifs = []
    motifs_Unique = []
    for i in dataset:
        for j in i:
            choix = random.randint(0, 1)
            if choix == 1:
                motifs.append(j)
        if not motifs_doublon(motifs_Unique,motifs):
            motifs_Unique.append(motifs)
        motifs = []
    #print("Motifs Retenu : ", motifs_Unique)
    return motifs_Unique

def calcul_frequence_algo_aire(dataset):
    for i in dataset:
        w_ABased.append(abs(len(i))* math.pow(2,(abs(len(i))-1)))
    for j, val in enumerate(w_ABased):
        f_ABased.append(val/sum(w_ABased))
    return f_ABased

def algorithme_aire(dataset):
    double = True
    iterateur = 0
    taille =[0 for t in dataset]
    # Motifs sans doublons
    motifs_Unique = []

    for i in dataset:
        compteur = 0
        choix = random.uniform(0, 1)
        for j in range(len(i)):
            compteur += j + 1
            if choix <= compteur/len(i)*2:
                taille[iterateur] = compteur
                break
        motifs = random.sample(i, taille[iterateur])
        if not motifs_doublon(motifs_Unique, motifs):
            motifs_Unique.append(motifs)
        iterateur += 1
    return motifs_Unique

def freq(motifs,motif_Unique):
    frequence= [0 for i in motif_Unique]
    cmpt = [0 for i in motif_Unique]
    for i in motifs:
        for j, val in enumerate(motif_Unique):
            if motifs_doublon(i,val):
                cmpt[j] += 1
    n = len(motifs)
    for i, value in enumerate(cmpt):
        frequence[i] = value/n
    return frequence

if __name__ == "__main__":
    w_FBased = []
    f_FBased = []
    w_ABased = []
    f_ABased = []
    filename='connect.dat'
    data = upload_file(filename)
    k = 1
    print("algorithme de fréquence")
    print("")
    f_FBased = calcul_frequence_algo_frequence(data)
    d_freq = random.choices(data,f_FBased, k=k)
    print(d_freq)
    print("")
    motifs = algorithme_frequence(d_freq)
    frequence_motif = freq(data, motifs_freq)
    print("fréquence des motifs choisis : ")
    print(frequence_motif)
    print("Motifs choisi : ")
    print(motifs)

    print("")
    print("algorithme d'aire'")
    print("")
    f_ABased = calcul_frequence_algo_aire(data)
    d_air = random.choices(data,f_ABased, k=k)
    print(d_air)
    print("")
    motifs = algorithme_aire(d_air)
    frequence_motif = freq(data, motifs_freq)
    print("fréquence des motifs choisis : ")
    print(frequence_motif)
    print("Motifs choisi : ")
    print(motifs)

    filename='connect.dat'
    data = upload_file(filename)
    w_FBased = []
    f_FBased = []
    w_ABased = []
    f_ABased = []
    k = 1000

    #frequence
    f_FBased = calcul_frequence_algo_frequence(data)
    d_freq = random.choices(data,f_FBased, k=k)
    motifs_freq = algorithme_frequence(d_freq)
    print("Génération du graphe fréquence")
    x = [len(n) for n in motifs_freq]
    y = freq(data, motifs_freq)
    s = 10
    plt.scatter(x, y, s)
    plt.xlabel("taille des motifs")
    plt.ylabel("fréquences des motifs")
    plt.title('Distribution de {0} réalisations avec {1}'.format(k,filename))
    plt.show()
    
    
    # aire
    f_ABased = calcul_frequence_algo_aire(data)
    d_air = random.choices(data,f_ABased, k=k)
    motifs_air = algorithme_aire(d_air)
    print("Génération du graphe aire")
    x = [len(n) for n in motifs_air]
    y = freq(data, motifs_air)
    s = 10
    plt.scatter(x, y, s)
    plt.xlabel("taille des motifs")
    plt.ylabel("fréquences des motifs")
    plt.title('Distribution de {0} réalisations avec {1}'.format(k,filename))
    plt.show()

    #ici on regarde si les motif tiré sont bien proportionelle à leur mesure
    k=1000
    f1='connect.dat'
    f2='chess.dat'
    f3='mushroom.dat'
    f4='pumsb.dat'
    f5='pumsb_star.dat'
    tab_f=[f1,f2,f3,f4,f5]
    for f in tab_f:
        print("pour le fichier ", f)
        print("")
        data = upload_file(f)
        w_FBased = []
        f_FBased = []
        w_ABased = []
        f_ABased = []
        # frequence
        f_FBased = calcul_frequence_algo_frequence(data)
        d_freq = random.choices(data,f_FBased, k=k)
        motifs_freq = algorithme_frequence(d_freq)
        x = freq(d_freq, motifs_freq)
        y = freq(data, motifs_freq)
        s = 10
        plt.scatter(x, y, s, c="g")
        plt.xlabel("Fréquences motifs choisis")
        plt.ylabel("Fréquences dans les fichiers de donné ")
        plt.title('Data = {0}, algo fréquence'.format(filename))
        plt.plot([1,0],[1,0])
        plt.show()
        
        # aire
        f_ABased = calcul_frequence_algo_aire(data)
        d_air = random.choices(data,f_ABased, k=k)
        motifs_air = algorithme_aire(d_air) 
        x = freq(d_air, motifs_air)
        y = freq(data, motifs_air)
        s= 10
        plt.scatter(x, y, s, c="g")
        plt.xlabel("Fréquences motifs choisis")
        plt.ylabel("Fréquences dans les fichiers de donné ")
        plt.title('Data = {0}, algo aire'.format(filename))
        plt.plot([1,0],[1,0])
        plt.show()

        #ici on regarde si il y a une bonne diversité tirés
        #calcul_frequence_algo_frequence(data)
        d_freq = random.choices(data,f_FBased, k=k)
        motifs_freq = algorithme_frequence(d_freq)
        print("Diversité avec l'algorithme de fréquence:")
        f_freq = freq(motifs_freq, motifs_freq)   
        diversite = sum(f_freq)/len(f_freq)
        print(diversite)
        print("")

        #calcul_frequence_algo_aire(data)
        d_air = random.choices(data,f_ABased, k=k)
        motifs_air = algorithme_aire(d_air)
        print("Diversité avec l'algorithme d'aire:")
        f_air = freq(motifs_air, motifs_air)   
        diversite = sum(f_air)/len(f_air)
        print(diversite)
        print("")

def kosara_resolution(filename):
    sample=upload_file(filename)
    w_FBased=[]
    w_ABased=[]
    taille=[]
    tab=[]
    
    for i,v in enumerate(sample):
        taille.append(len(v))
    moyenne = np.average(taille)
    print("moyenne:",moyenne)

    for i,v in enumerate(sample):
        if(len(v) <= moyenne):
            tab.append(v)
            w_FBased.append(math.pow(2,abs(len(v)))) #le calcul poid Fréquence
            w_ABased.append(abs(len(v))* math.pow(2,(abs(len(v))-1))) #le calcul poid Aire 
    #ici on le fait just pour k = 1 car c'est surtout pour tester si il réussi à passer le problème d'avant dans le calcul du poids
    k = 1
    
    print("fréquence")
    d_freq = random.choices(tab,w_FBased, k=k)
    print("motif")
    motifs = algorithme_frequence(d_freq)
    print(motifs)
    
    print("Aire")
    d_air = random.choices(tab,w_ABased, k=k)
    print("motif")
    motifs = algorithme_aire(d_air)
    print(motifs)
    
kosara_resolution("kosarake.txt")