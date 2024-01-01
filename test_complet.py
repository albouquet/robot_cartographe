# Test de l'envoie de la video et des données
# ainsi que de la reception des commandes

import pigpio
import board
import time
import socket
import picamera
import pickle as pk
import numpy as np
import threading
from adafruit_vl53l0x import VL53L0X

###########	INITIALISATION du thread de reception des commandes
t_control=threading.Thread(target=controle_moteurs, args=())
###########	FIN initialisation du thread de reception des commandes

########### 	INITIALISATION Camera
taille_frame=320*240*3
cam=picamera.PiCamera()
cam.resolution = (320,240)
cam.framerate=30
########### 	FIN initialisation camera


########### 	CONNEXION Socket video
socket_video=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_video.connect(('192.168.1.18',9322))
con_vid=socket_video.makefile('wb')
########### 	FIN connexion socket video


###########	CONNEXION Socket capteurs
socket_capteurs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_capteurs.connect(('192.168.1.18',9322))
###########	FIN connexion socket capteurs


###########	INSTANCIATION de l'objet GPIO
pi1=pigpio.pi()
###########	FIN instanciation de l'objet gpio


#########	Initialisation des capteurs VL53l0X

# Les pins SHDN des 2 capteurs
pi1.set_mode(4,pigpio.OUTPUT)
pi1.set_mode(14,pigpio.OUTPUT)
pi1.write(4,0)
pi1.write(14,0)

bus_i2c=board.I2C()

# Changement d'adresse des capteurs (car par defaut, tous les deux sont à 0x29)
pi1.write(4,1)
vlx_1=VL53L0X(bus_i2c)
vlx_1.set_address(0x30)
pi1.write(14,1)
vlx_2=VL53L0X(bus_i2c)
vlx_2.set_address(0x31)


#########	FIN Initialisation des capteurs VL53l0X





###########	ENVOIE Video
try:
	cam.start_recording(con_vid,format='h264')
	#cam.wait_recording(20)

	##########	TEST distance

	dist_capt1=vlx_1.distance-1.5
	dist_capt2=vlx_2.distance-1.5
	print("Distance capteur 1 : {0}cm".format(dist_capt1))
	print("Distance capteur 2 : {0}cm".format(dist_capt2))

	socket_capteurs.send((str(dist_capt1)+" "+str(dist_capt2)).encode("UTF-8"))


	##########	FIN test distance

finally:
	print("fin")
	cam.stop_recording()
	con_vid.close()
	socket_video.close()
	socket_capteurs.close()

###########	FIN envoie video
