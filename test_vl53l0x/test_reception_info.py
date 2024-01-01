
import socket
import cv2 as cv
import numpy as np
import pickle as pk

socket_recoie=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_recoie.bind(('192.168.1.18',9322))
socket_recoie.listen(1)
conn_vid = socket_recoie.accept()[0]


chaine=""
while True:
		data = conn_vid.recv(1024)
		if not data:
			break
		chaine=chaine+data.decode("UTF-8")
		
print(chaine)
conn_vid.close()
