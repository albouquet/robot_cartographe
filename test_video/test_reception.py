# Dans ce programme : 
#	- Ouverture d'une socket pour recevoir le flux video de la Pi
#	- Reception de ce flux dans un file-like
#	- Affichage du flux video via MPV
#	- Enregistrement du flux video dans le fichier video.h264


import socket
import cv2 as cv
import numpy as np
import pickle as pk
import subprocess

socket_recoie=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_recoie.bind(('192.168.1.18',9322))
socket_recoie.listen(1)
conn_vid = socket_recoie.accept()[0].makefile('rb')
fichier_video=open("video.h264", "wb")




try:
	cmdline = ['mpv','--fps=30','--cache=yes','-']
	player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
	while True:
		data = conn_vid.read(1024)
		if not data:
			break
		player.stdin.write(data)
		fichier_video.write(data)
finally:
	fichier_video.close()
	conn_vid.close()
	socket_recoie.close()
	player.terminate()
