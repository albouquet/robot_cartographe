# Test du capteur vl53l0x
# Connecté en I2C sur la broche 3 (SDA 1),5 (SCL 1) du bus 1
# Son adresse est 29 (obtenue avec i2cdetect -y 1)
# Desactiver nftables

# Necessité d'installer adafruit-circuitpython-vl53l0x via pip3
# et importer le module avec :  from adafruit_vl53l0x import VL53L0X

import pigpio
import board
import time
from adafruit_vl53l0x import VL53L0X

pi1=pigpio.pi()
#dev represente les 4 objets vl53lx
dev=[]

#dev1=pi1.i2c_open(1,0x29,0)



#########	Initialisation des capteurs VL53l0X

# Les pins SHDN des 4 capteurs
pi1.write(4,0)
pi1.write(5,0)
pi1.write(6,0)
pi1.write(7,0)

bus_i2c=board.I2C()


for i in [4]:
	pi1.write(4,1)
	dev.insert(i-4,VL53L0X(bus_i2c))
	# Changement de ladresse de chacun des capteurs
	dev[i-4].set_address(i+0x30)


#########	FIN Initialisation des capteurs VL53l0X



#########	Initialisation des moteurs (signaux PWM)

# Initialisation des GPIO PWM
pi1.set_mode(18,pigpio.OUTPUT)
pi1.set_mode(12,pigpio.OUTPUT)

# PWM hardware à 800Hz sur pin 18 et 12
pi1.hardware_PWM(18,800,0)
pi1.hardware_PWM(12,800,0)



#print("Range : {0}cm".format(vl53.distance))
