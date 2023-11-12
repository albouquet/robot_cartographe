import socket
import keyboard
import time

host = '192.168.1.18'
port = 9322

soc_cmd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc_cmd.bind((host,9322))
soc_cmd.listen(1)
conn_cmd = soc_cmd.accept()[0]

while True:

	event=keyboard.read_key()
	# conn_cmd.send(b(event))
	if (event=="z"):
		# Acceleration
		conn_cmd.send(b'z')
		print("c'est z \n")
	elif (event=="q"):
		# rotation gauche
		conn_cmd.send(b'q')
		print("c'est q \n")
	elif (event=="d"):
		# Rotation droite
		conn_cmd.send(b'd')
		print("c'est d \n")
	elif (event==" "):
		# Rotation droite
		conn_cmd.send(b' ')
		print("c'est espace \n")
	elif (event == "p"):
		conn_cmd.send(b'p')
		break;

	time.sleep(1)

conn_cmd.close()
