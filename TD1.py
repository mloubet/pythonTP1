# -*- coding:utf-8 -*- #
# Auteur 	: Matteo Loubet
# Titre 	: AlgoEtProg_TD1.py
# Role 		: Somme de frcations
# Date		: 2/11/16
# Version	: 1.0
# Apports	: #
print"\n\n\n" #Mise en page propre en console avec retours à  la ligne

import random

"""
######

Ce fichier comporte plusieurs fonctions du TD1 (question 1 à 11, question 12 dans un autre fichier), 
et d'autres fonctions, soit qui servent à répondre à ces question
soit qui ont d'abord été faite pour comprendre et ensuite faire les questions.

Chaque question est numérotée en commentaire de la fonction concernée.

Bien évidement, toute ces fonctions ont été réalisées seuls, en utilisant uniquement le PDF du cours.

#####
"""


def saisie(): # Fonction qui permet de saisir les éléments d'une liste
	x = 1
	list1 = []
	while x!=0:
		x = input('Entez les valeurs de la liste (0 pour terminer) : ')
		if x!=0: list1.append(x)
	return list1		

def randlist(): # Pour les test : fonction qui génère une liste aléatoirement
	x = 0
	list1 = []
	for i in xrange(20):
		x = random.randint(0, 20)
		list1.append(x)
	return list1

def saisieCheck(): # Fonction qui permet de saisir les éléments d'une liste sans qu'ils ne se répètent
	x = 1
	list1 = []
	while x!=0:
		x = input('Entez les valeurs de la liste (0 pour terminer) : ')
		if x!=0 and check(list1, x): list1.append(x)
	return list1

def maxi(l): #Fonction qui renvoit la valeur maximum d'une liste
 	maxi = l[0]
 	for i in l:
 		if i > maxi:
 			maxi = i
 	return maxi

def indiceMaxi(l): #4 Renvoit l'indice de la valeur maximum d'une liste 'l' (renvoit l'indice du premier si le maximum est présent plusieur fois)
	u = 0
	for i in l:
		if i != maxi(l):
			u += 1
		else:
			break
	return u


def present(l, n): #1 : Fonction qui cherche un élément 'n' dans la liste 'l'
	for i in l:
		if n==i:
			return 1
	return 0

def occurence(l, n): #2 : Renvoit le nombre d'élément 'n' dans la liste 'l'
	occurence = 0
	for i in l:
		if i == n:
			occurence += 1
	return occurence

def antiDoublons(l): #3 Fonction qui supprime les doublons dans une liste 'l'
	l1 = []
	for u, i in enumerate(l):
		for x, y in enumerate(l):
			if i==y and x!=u:
				del l[x]
	return l

def moyenneVariance(l): #5-6 Renvoit la moyenne et la variance de la liste 'l'
	somme = 0
	for i in l:
		somme += i
	m = (somme + 0.0) / len(l)
	somme = 0
	for i in l:
		somme += (i - m)**2
	v = (somme + 0.0) / len(l)
	return m,v

def indiceMaxiNPremiers(l, n): #7 a - Fonction qui renvoit l'indice du plus haut terme de la liste 'l' parmis le 'n' premiers termes
	if n>len(l):
		n = len(l)
	list2 = list()
	for i in xrange(0, n):
		list2.append(l[i])
	return indiceMaxi(list2)


def triDecroissant(l): #Fonction de tri 1
	l2 = []
	while l!=[]:	
		m = maxi(l)
		l2.append(m)
		l.remove(m)
	return l2

def swap(l, a, b): #Fonction qui interverti les termes d'indice 'a' et 'b' de la liste 'l'
	c = l[a]
	l[a] = l[b]
	l[b] = c


def triCroissant(l): #7b Fonction qui tri une liste à l'aide de la fonction 7a
	for i in xrange(len(l)):
		if indiceMaxiNPremiers(l, len(l)-i) < (len(l)-i-1):
			swap(l, len(l)-i-1, indiceMaxiNPremiers(l, len(l)-i))


def mediane(l): #8 Fonction qui renvoit la médiane d'une liste
	med = 0
	lenl = len(l)
	if lenl % 2 == 0:
		med = (l[(lenl/2)-1] + l[(lenl/2)] + 0.0)/2
	else :
		med = l[lenl/2]
	return med

def listIndice(l, n): #9 Fonction qui renvoit la liste des indice d'un élément 'n' donné dans 'l'
	indice = list()
	for u, i in enumerate(l):
		if i == n :
			indice.append(u)
	return indice

def insereElement(l, n): #1ère tentative #10 version 1 : insère un élément dans une liste triée
	l2 = list()
	done = 0
	for i in l :
		if (n > i) or (done == 1):
			l2.append(i)
		else :
			l2.append(n)
			done = 1
			l2.append(i)
	return l2

def insereElement2(l, n): #2ème tentative #10 version 2 : insère un élément dans une liste triée.
	done = 0
	if n > maxi(l): 
		l.append(n)
		return l
	else:
		for i in xrange(len(l)) :
			if (n > l[i]) or (done == 1):
				pass
			else :
				l.insert(i, n)
				return l

def insereElementDichotomie(l, n): #10 par Dichotomie (Enfin !)
	if n > l[len(l)-1]:
		l.append(n)
		return l

	d = 0
	f = len(l) - 1
	while (f - d) > 1:
		m = (f + d) / 2
		if n < l[m] :
			f = m
		else : 
			d = m

	if n == l[d] :
		l.insert(d, n)
	elif n > l[d] :
		l.insert(f, n)
	return l

def fusion(l1, l2): #11 Fusion de deux listes triées.
	i, j = 0, 0
	l = list()
	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j] :
			l.append(l1[i])
			i += 1
		else :
			l.append(l2[j])
			j += 1
	if i == len(l1):
		for u in xrange(j, len(l2)):
			l.append(l2[u])

	else :
		for u in xrange(i, len(l1)) :
			l.append(l1[u])


	return l


#### MAIN ####


list1 = saisie()
#list1 = randlist() #Pour les test ;)
list2 = randlist()
print list1, list2

print "\n\n\n"

for u, i in enumerate(list1):
	print list1[u], " est présent\t  ", occurence(list1, i), " fois dans la liste"

n = input("Entrez un élément dont vous voulez connaitre les indices : ")
print listIndice(list1, n)

list1 = antiDoublons(list1)

moyenne, variance = moyenneVariance(list1)
print "\n\nmoyenne : {}\t variance : {}".format(moyenne, variance)

print "\n\nListe apres suppression des doublons : ", list1

print "\n\nValeur max : ", maxi(list1)

print "\nIndice de la valeur max : ", indiceMaxi(list1), " (La première valeur a l'indice 0 !)"

print "\nIndice du terme maximum parmis les n premiers termes : (entrez 'n')", indiceMaxiNPremiers(list1, input())

list1 = triDecroissant(list1)

print "\nListe triée décroissante : ", list1

triCroissant(list1)

print "\nListe triée croissante : ", list1

print 'Médiane de la liste : ', mediane(list1)

n = input('Entrez une valeur à insérer dans la liste : ')
print insereElement2(list1, n)
print insereElementDichotomie(list1, n)


print 'liste 1 : ', list1
triCroissant(antiDoublons(list2))
print 'Liste 2 (aléatoire) : ', list2
print len(list1), len(list2), fusion(list1, list2)







print"\n\n\n" #Mise en page propre en console avec retours à  la ligne







