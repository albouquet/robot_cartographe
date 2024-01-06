"""
	Test de l'envoie des données (video, capteurs, coordonnées)
	ainsi que de la reception des commandes.
	
"""


import pigpio
import board
import time
import socket
import picamera
import pickle as pk
import numpy as np
import threading
from adafruit_vl53l0x import VL53L0X


########	CREATION de la fonction de controle des moteurs
def controle_moteurs():
	
	global etat
	# Au depart, les moteurs sont à l'arret
	pi1.hardware_PWM(18,490,0)
	pi1.hardware_PWM(12,490,0)
	pi1.write(20,0)
	pi1.write(21,0)
	pi1.write(19,0)
	pi1.write(26,0)

	#	Reception des commandes
	while True:
		cmd=socket_cmd.recv(1)
		
		match cmd:
			case b' ':
				dc_moteur1=0
				dc_moteur2=0
				pi1.write(20,0)
				pi1.write(21,0)
				pi1.write(19,0)
				pi1.write(26,0)
				etat='s'
			case b'z':
				dc_moteur1=250000
				dc_moteur2=250000
				pi1.write(20,1)
				pi1.write(21,1)
				pi1.write(19,1)
				pi1.write(26,1)
				etat='a'
			case b'q':
				# Rotation gauche (90°)
				dc_moteur1=100000
				dc_moteur2=100000
				pi1.write(20,1)
				pi1.write(21,0)
				pi1.write(19,1)
				pi1.write(26,0)
				pi1.hardware_PWM(18,490,dc_moteur1)
				pi1.hardware_PWM(12,490,dc_moteur2)
				time.sleep(1)
				dc_moteur1=0
				dc_moteur2=0
				pi1.write(20,0)
				pi1.write(21,0)
				pi1.write(19,0)
				pi1.write(26,0)
				etat='s'
			case b'd':
				# Rotation droite (90°)
				dc_moteur1=100000
				dc_moteur2=100000
				pi1.write(20,0)
				pi1.write(21,1)
				pi1.write(19,0)
				pi1.write(26,1)
				pi1.hardware_PWM(18,490,dc_moteur1)
				pi1.hardware_PWM(12,490,dc_moteur2)
				time.sleep(1)
				dc_moteur1=0
				dc_moteur2=0
				pi1.write(20,0)
				pi1.write(21,0)
				pi1.write(19,0)
				pi1.write(26,0)
				etat='s'
			case b'p':
				etat='p'
				break

		pi1.hardware_PWM(18,490,dc_moteur1)
		pi1.hardware_PWM(12,490,dc_moteur2)

		time.sleep(1)

	pi1.hardware_PWM(18,490,0)
	pi1.hardware_PWM(12,490,0)

########	FIN creation de la fonction de controle des moteurs







######### 	INITIALISATION Camera
taille_frame=320*240*3
cam=picamera.PiCamera()
cam.resolution = (320,240)
cam.framerate=30
######### 	FIN initialisation camera



#########	CONNEXION Socket capteurs
socket_capteurs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_capteurs.connect(('192.168.1.18',9322))
#########	FIN connexion socket capteurs


######### 	CONNEXION Socket video
socket_video=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_video.connect(('192.168.1.18',9323))
con_vid=socket_video.makefile('wb')
######### 	FIN connexion socket video


#########	CONNEXION Socket commandes
socket_cmd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_cmd.connect(('192.168.1.18',9324))
#########	FIN connexion socket commandes


#########	INSTANCIATION de l'objet GPIO
pi1=pigpio.pi()
#########	FIN instanciation de l'objet gpio


#########	INITIALISATION des gpio des moteurs
	# La variable globale "etat" prend la valeur 'a' (le robot avance) ou 's' (il fait autre chose qu'avancer) ou 'p' (arret complet du robot)
	etat='s'
	pi1.set_mode(18,pigpio.OUTPUT)
	pi1.set_mode(12,pigpio.OUTPUT)
	pi1.set_mode(20,pigpio.OUTPUT)
	pi1.set_mode(21,pigpio.OUTPUT)
	pi1.set_mode(19,pigpio.OUTPUT)
	pi1.set_mode(26,pigpio.OUTPUT)
#########	FIN initialisation des gpio des moteurs



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





#########	ENVOIE Video + donnees
try:
	#########	INITIALISATION du thread de reception des commandes
	t_control=threading.Thread(target=controle_moteurs, args=())
	t_control.start()
	#########	FIN initialisation du thread de reception des commandes
	
	cam.start_recording(con_vid,format='h264')
	#cam.wait_recording(20)

	while True:
		
		if etat == 'a':
			
			#########	Envoi distance

			dist_capt1=vlx_1.distance-1.5
			dist_capt2=vlx_2.distance-1.3
			print("Distance capteur 1 : {0}cm".format(dist_capt1))
			print("Distance capteur 2 : {0}cm".format(dist_capt2))

			# envoi des données (coordonnées du robot, distance capteur gauche, distance capteur droit)
			socket_capteurs.send((str(int(dist_capt1))+" "+str(int(dist_capt2))).encode("UTF-8"))

			#########	FIN Envoi distance
		
		elif etat == 'p':
			break
		
		time.sleep(1)

finally:
	print("fin")
	cam.stop_recording()
	con_vid.close()
	socket_video.close()
	socket_capteurs.close()
	socket_cmd.close()

###########	FIN envoie video + donnees
