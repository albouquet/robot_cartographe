# Test du capteur vl53l0x
# Connecté en I2C sur la broche 3 (SDA 1),5 (SCL 1) du bus 1
# Son adresse est 29 (obtenue avec i2cdetect -y 1)
# Desactiver nftables
# Lancer pigpiod

# Necessité d'installer adafruit-circuitpython-vl53l0x via pip3
# et importer le module avec :  from adafruit_vl53l0x import VL53L0X

import pigpio
import board
import time
import socket
from adafruit_vl53l0x import VL53L0X

socket_envoi=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_envoi.connect(('192.168.1.18',9322))


pi1=pigpio.pi()
#dev1=pi1.i2c_open(1,0x29,0)


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



########## TEST distance

# Il y a 3 centimetres en trop dans chacunes des mesures, donc je les soustrais
dist_capt1=vlx_1.distance-1.5
dist_capt2=vlx_2.distance-1.5
print("Distance capteur 1 : {0}cm".format(dist_capt1))
print("Distance capteur 2 : {0}cm".format(dist_capt2))

socket_envoi.send((str(dist_capt1)+" "+str(dist_capt2)).encode("UTF-8"))

socket_envoi.close()
