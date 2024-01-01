# Pour le PWM hardware : (pin, frequence, dutycycle)
#	frequence : 800hz est très bien pour un moteur
#	dutycycle : 300000 = 30%

# Le robot peut se stopper ou accelerer
# Pour effectuer une rotation, il se remet à l'arret, puis fait sa rotation
# Il n'est pas possible de décélerer


import pigpio
import time
import socket

# Partie CONNEXION SERVEUR
con_cmd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(con_cmd.connect(('192.168.1.18',9322)))

############################


# Partie TRAITEMENT COMMANDES
dc_moteur1=0
dc_moteur2=0

pi1=pigpio.pi()
pi1.set_mode(18,pigpio.OUTPUT)
pi1.set_mode(12,pigpio.OUTPUT)

# Au depart, les moteurs sont à l'arret
pi1.hardware_PWM(18,490,0)
pi1.hardware_PWM(12,490,0)

#	RECEPTION DE LA COMMANDE
while True:
	cmd=con_cmd.recv(1)
	print("La commande est ")
	print(cmd)
	if cmd==b' ':
		dc_moteur1=0
		dc_moteur2=0
	elif cmd==b'z':
		print("La commande z est recue")
		dc_moteur1+=50000
		dc_moteur2+=50000
	elif cmd==b'q':
		dc_moteur1=50000
		dc_moteur2=0
	elif cmd==b'd':
		dc_moteur1=0
		dc_moteur2=50000
	elif cmd==b'p':
		break

	pi1.hardware_PWM(18,490,dc_moteur1)
	pi1.hardware_PWM(12,490,dc_moteur2)

	time.sleep(1)

pi1.hardware_PWM(18,490,0)
pi1.hardware_PWM(12,490,0)


pi1.stop()
con_cmd.close()
