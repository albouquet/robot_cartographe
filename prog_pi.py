import pigpio
import board
import time
import socket
import picamera
import pickle as pk
import numpy as np
import threading
from adafruit_vl53l0x import VL53L0X

def changement_angle(sens):
	global vecteur
	global direction_x
	global direction_y

	if direction_x == True :
		if vecteur == 1 and sens=='d':
			vecteur = -1
		elif vecteur == -1 and sens=='d':
			vecteur = 1
	elif direction_y == True :
		if vecteur == 1 and sens=='g':
			vecteur = -1
		elif vecteur == -1 and sens=='g':
			vecteur = 1

	direction_x=not(direction_x)
	direction_y=not(direction_y)


########	Fonction de repérage 2D
def reperage_2D():
	global x
	global y

	while True :
		if etat=="a":
			x=x+(direction_x * vecteur)
			y=y+(direction_y * vecteur)

		time.sleep(0.2)

########	FIN fonction de repérage 2D

########	CREATION de la fonction de controle des moteurs
def controle_moteurs():

	global etat
	#global pi1
	# Au depart, les moteurs sont à l'arret
	pi1.hardware_PWM(18,400,0)
	pi1.hardware_PWM(13,400,0)
	pi1.write(25,0)
	pi1.write(8,0)
	pi1.write(9,0)
	pi1.write(11,0)

	#	Reception des commandes
	while True:
		cmd=socket_cmd.recv(1)

		if cmd == b'a':
			dc_moteur1=0
			dc_moteur2=0
			pi1.write(25,0)
			pi1.write(8,0)
			pi1.write(9,0)
			pi1.write(11,0)
			etat='s'
		elif cmd == b'z':
			dc_moteur1=400000
			dc_moteur2=410000
			pi1.write(25,1)
			pi1.write(8,0)
			pi1.write(9,1)
			pi1.write(11,0)
			etat='a'
		elif cmd == b'q':
			# Rotation gauche (90°)
			dc_moteur1=400000
			dc_moteur2=400000
			pi1.write(25,0)
			pi1.write(8,1)
			pi1.write(9,1)
			pi1.write(11,0)
			pi1.hardware_PWM(18,400,dc_moteur1)
			pi1.hardware_PWM(13,400,dc_moteur2)
			time.sleep(0.3)
			dc_moteur1=0
			dc_moteur2=0
			pi1.write(25,0)
			pi1.write(8,0)
			pi1.write(9,0)
			pi1.write(11,0)
			etat='s'
			changement_angle('g')

		elif cmd == b'd':
			# Rotation droite (90°)
			dc_moteur1=400000
			dc_moteur2=400000
			pi1.write(25,1)
			pi1.write(8,0)
			pi1.write(9,0)
			pi1.write(11,1)
			pi1.hardware_PWM(18,400,dc_moteur1)
			pi1.hardware_PWM(13,400,dc_moteur2)
			time.sleep(0.3)
			dc_moteur1=0
			dc_moteur2=0
			pi1.write(25,0)
			pi1.write(8,0)
			pi1.write(9,0)
			pi1.write(11,0)
			etat='s'
			changement_angle('d')
		elif cmd == b'p':
			etat='p'
			break

		pi1.hardware_PWM(18,400,dc_moteur1)
		pi1.hardware_PWM(13,400,dc_moteur2)

		time.sleep(1)

	pi1.hardware_PWM(18,100,0)
	pi1.hardware_PWM(13,100,0)

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
# Broches PWM pour les deux moteurs
pi1.set_mode(18,pigpio.OUTPUT)
pi1.set_mode(13,pigpio.OUTPUT)
# Broches IN1 et IN2 pour le sens de rotation M1
pi1.set_mode(25,pigpio.OUTPUT)
pi1.set_mode(8,pigpio.OUTPUT)
# Broches IN3 et IN4 pour le sens de rotation M2
pi1.set_mode(9,pigpio.OUTPUT)
pi1.set_mode(11,pigpio.OUTPUT)

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


#########	INITIALISATION variables de plan 2D

x=0
y=0
# direction prend True ou False
direction_x=False
direction_y=True
#vecteur prend 1 ou -1
vecteur=1

#########	FIN initialisation variables de plan 2D


#########	ENVOIE Video + donnees
try:
	#########	INITIALISATION du thread de reception des commandes
	t_control=threading.Thread(target=controle_moteurs, args=())
	t_control.start()
	#########	FIN initialisation du thread de reception des commandes


	t_reperage=threading.Thread(target=reperage_2D, args=())
	t_reperage.start()

	cam.start_recording(con_vid,format='h264')

	while True:

		if etat == 'a':

			#########	Envoi distance et COO

			dist_capt1=vlx_1.distance-1.5
			dist_capt2=vlx_2.distance-1.3
			print("Distance capteur 1 : {0}cm".format(dist_capt1))
			print("Distance capteur 2 : {0}cm".format(dist_capt2))

			# envoi des données (coordonnées du robot, distance capteur gauche, distance capteur droit)
			socket_capteurs.send((str(int(dist_capt1))+" "+str(int(dist_capt2))+" "+str(int(x))+" "+str(int(y))).encode("UTF-8"))

			#########	FIN Envoi distance et COO

		elif etat == 'p':
			break

		# Envoie des infomations de télémetrie toute les secondes
		time.sleep(0.5)

finally:
	print("fin")
	socket_video.close()
	cam.stop_recording()
	con_vid.close()
	socket_capteurs.close()
	socket_cmd.close()

###########	FIN envoie video + donnees
