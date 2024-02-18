# Pour le PWM hardware : (pin, frequence, dutycycle)
#	frequence : 800hz est très bien pour un moteur
#	dutycycle : 300000 = 30%



import pigpio
import time


def avancer():
	global pi1
	# Partie TRAITEMENT COMMANDES
	dc_moteur1=0
	dc_moteur2=0

	pi1.hardware_PWM(18,490,0)
	pi1.hardware_PWM(13,490,0)
	pi1.write(25,1)
	pi1.write(8,0)
	pi1.write(9,1)
	pi1.write(11,0)

	dc_moteur1=400000
	dc_moteur2=400000

	pi1.hardware_PWM(18,490,dc_moteur1)
	pi1.hardware_PWM(13,490,dc_moteur2)

	time.sleep(1)

	pi1.hardware_PWM(18,490,0)
	pi1.hardware_PWM(13,490,0)
	pi1.write(25,0)
	pi1.write(8,0)
	pi1.write(9,0)
	pi1.write(11,0)


def tourner_gauche():
	global pi1
	# Partie TRAITEMENT COMMANDES
	dc_moteur1=0
	dc_moteur2=0

	pi1.hardware_PWM(18,490,0)
	pi1.hardware_PWM(13,490,0)
	pi1.write(25,0)
	pi1.write(8,1)
	pi1.write(9,1)
	pi1.write(11,0)

	dc_moteur1=400000
	dc_moteur2=400000

	pi1.hardware_PWM(18,490,dc_moteur1)
	pi1.hardware_PWM(13,490,dc_moteur2)

	time.sleep(0.30)

	pi1.hardware_PWM(18,490,0)
	pi1.hardware_PWM(13,490,0)
	pi1.write(25,0)
	pi1.write(8,0)
	pi1.write(9,0)
	pi1.write(11,0)



pi1=pigpio.pi()
pi1.set_mode(18,pigpio.OUTPUT)
pi1.set_mode(13,pigpio.OUTPUT)
# Broches IN1 et IN2 pour le sens de rotation M1
pi1.set_mode(25,pigpio.OUTPUT)
pi1.set_mode(8,pigpio.OUTPUT)
# Broches IN3 et IN4 pour le sens de rotation M2
pi1.set_mode(9,pigpio.OUTPUT)
pi1.set_mode(11,pigpio.OUTPUT)

avancer()
tourner_gauche()

pi1.stop()
