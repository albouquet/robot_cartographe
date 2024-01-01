"""
Ce programme permet le controle du robot :
	- reception des données des capteurs de distance
	- reception du flux video du robot
	- envoie de commande au robot

Trois sockets sont ouvertes pour recupérer et envoyer ces données.
"""
import socket
import cv2 as cv
import numpy as np
import pickle as pk
import subprocess
import keyboard
import threading
import time

#########	INITIALISATION socket capteur
socket_capt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_capt.bind(('192.168.1.18',9322))
socket_capt.listen(1)
conn_capt = socket_capt.accept()[0]
#########	FIN initialisation socket capteur


######### 	INITIALISATION socket video
socket_vid=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_vid.bind(('192.168.1.18',9323))
socket_vid.listen(1)
conn_vid = socket_vid.accept()[0].makefile('rb')
fichier_video=open("video.h264", "wb")
######### 	FIN initialisation socket video

######### 	INITIALISATION socket commande
socket_cmd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_cmd.bind(('192.168.1.18',9324))
socket_cmd.listen(1)
conn_cmd = socket_cmd.accept()[0]
######### 	FIN initialisation socket commande


def recup_capt():
	######### 	RECUPERATION des données des capteurs
	fichier_capt=open("data_capt.txt", "w")
	chaine=""
	while True:
			data = conn_capt.recv(256)
			if not data:
				break
			chaine=chaine+data.decode("UTF-8")
			fichier_capt.write(chaine+"\n")
			
	print(chaine)
	fichier_capt.close()
	conn_capt.close()
	######### 	FIN recuperation des données des capteurs


def recup_vid():
	#########	RECUPERATION du flux video
	try:
		#cmdline = ['mpv','--fps=30','--cache=yes','-']
		#player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
		while True:
			data = conn_vid.read(1024)
			if not data:
				break
			player.stdin.write(data)
			fichier_video.write(data)
	finally:
		fichier_video.close()
		conn_vid.close()
		socket_vid.close()
		player.terminate()
	#########	FIN recuperation du flux video


#########	LANCEMENT des threads (video + données capteurs)
thread_video=threading.Thread(target=recup_vid, args=())
thread_video.start()
thread_capt=threading.Thread(target=recup_capt, args=())
thread_capt.start()
#########	FIN lancement des threads (video + données capteurs)


cmdline = ['mpv','--fps=30','--cache=yes','-']
player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)


######### ENVOI des touches de control

while True:
	event='0'
	#récupération de la touche:
	event=keyboard.read_key()

	#traitement de la touche:
	if (event=="a"):
		conn_cmd.send(b'a')
		print("c'est a \n")
	elif (event=="z"):
		conn_cmd.send(b'z')
		print("c'est z \n")
	elif (event=="q"):
		conn_cmd.send(b'q')
		print("c'est q \n")
	elif (event=="e"):
		conn_cmd.send(b'e')
		print("c'est e \n")
	elif (event=="p"):
		conn_cmd.send(b'p')
		conn_cmd.close()
		conn_vid.close()
		conn_capt.close()
		#thread_capt.stop()
		#thread_video.stop()
		break
	time.sleep(1)

######### FIN envoi des touches de control
