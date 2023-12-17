#import pigpio
import time
import socket
import numpy as np
import picamera
import pickle as pk

taille_frame=320*240*3
frame1=np.empty((240,320,3), dtype=np.uint8)
cam=picamera.PiCamera()
cam.resolution = (320,240)
cam.framerate=30


# Partie CONNEXION SERVEUR
socket_envoie=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(socket_envoie.connect(('192.168.1.18',9322)))
connection=socket_envoie.makefile('wb')
##########################

"""
i=0

while i < 10 :
	cam.capture(frame1,'rgb')
	socket_envoie.send(taille_frame.to_bytes(4,'little',signed=False))
	socket_envoie.sendall(pk.dumps(frame1))
	i+=1
	time.sleep(1)
"""


try:
	cam.start_recording(connection,format='h264')
	cam.wait_recording(20)
	# AU lieu du cam.wait faire une boucle de ce qui enverra les données des capteurs et recuperera les commandes
finally:
	print("fin")
	cam.stop_recording()
	connection.close()
	socket_envoie.close()
