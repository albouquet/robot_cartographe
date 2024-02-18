# Ce programme permet de réaliser un plan 2D grace au données d'un fichier en entré.
# Ce fichier contient 4 données par lignes, séparées par des espaces :
#	 distance_gauche distance_droite x y

import matplotlib.pyplot as plt
import numpy as np
import time


# Fonction de création du plan 2D
def map_2D(lines):
	global ax
	
	line1= [0,0,0,0]
	
	# Point à gauche du robot
	p1_temp_prec=[0,0]
	# Point à droite du robot
	p2_temp_prec=[0,0]
	
	for line2 in lines:
	
		if line2[2] != line1[2]:
			# x a changé
			if line2[2] < line1[2]:
				p1_temp=[ line2[2] , line2[3]-line2[0] ]
				p2_temp=[ line2[2] , line2[3]+line2[1] ]
			else :
				p1_temp=[ line2[2] , line2[3]+line2[0] ]
				p2_temp=[ line2[2] , line2[3]-line2[1] ]
		else :
			# y a changé
			if line2[3] < line1[3] :
				p1_temp=[ line2[2]+line2[0] , line2[3] ]
				p2_temp=[ line2[2]-line2[1] , line2[3] ]
			else :
				p1_temp=[ line2[2]-line2[0] , line2[3] ]
				p2_temp=[ line2[2]+line2[1] , line2[3] ]

		# Gestion des distances à 817 (distance inconnue car trop grande donc ne pas faire de lien entre les points)
		#if (abs(p1_temp_prec[0]) < 200 and abs(p1_temp[0]) < 200) :
		#	if (abs(p1_temp_prec[1]) < 200 and abs(p1_temp[1]) < 200) :
		ax.plot([p1_temp_prec[0],p1_temp[0]], [p1_temp_prec[1],p1_temp[1]])
		#if (abs(p2_temp_prec[0]) < 200 and abs(p2_temp[0]) < 200) :
		#	if (abs(p1_temp_prec[1]) < 200 and abs(p1_temp[1]) < 200) :
		ax.plot([p2_temp_prec[0],p2_temp[0]], [p2_temp_prec[1],p2_temp[1]])
		
		line1=line2
		p1_temp_prec=p1_temp
		p2_temp_prec=p2_temp

		plt.pause(0.4)





# Création du corps du plan
fig = plt.figure()
ax = plt.axes()

# Lecture et modification du fichier de données
with open("data_capt_111_125.txt") as temp_f:
	datafile = temp_f.readlines()
	
	for i in range(0,len(datafile)):
		# Symbole de fin de ligne supprimé
		datafile[i] = datafile[i].replace("\n", "")
		# Chaque nombre est séparé par un espace (symbole de séparation des nombres)
		datafile[i]=datafile[i].split(" ")
		# Les nombres sont en "string" donc je les retype intier
		datafile[i][:] = list(map(int, datafile[i]))
	
	map_2D(datafile)


# Affichage plan 2D
plt.show()
