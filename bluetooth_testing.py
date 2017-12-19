import picamera
import bluetooth
import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI
import datetime
import time
import threading
import BMP280 as BMP280
import logging

logging.basicConfig(level=logging.DEBUG)

sensor = BMP280.BMP280()

LED=21

GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
GPIO.output(LED,0)

camera = picamera.PiCamera()
camera.resolution = (1280, 720)

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

bd_addr = "B4:F1:DA:2A:84:86"

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
threads = []

def altworker():
	"""thread worker function"""
	client_socket.send("Running Function 1\n")
	return 

def vidworker():
	"""thread worker function"""
	client_socket.send("Running Function 2\n")
	return

print "Accepted connection from ",address
while 1:
	data = client_socket.recv(1024)
	print "Received: %s" % data
	if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
		client_socket.send("1 Received\n")
		t = threading.Thread(target=vidworker)
		threads.append(t)
		t.start()
	if (data == "2"):
		client_socket.send("2 Received\n")
		t2 = threading.Thread(target=altworker)
		threads.append(t2)
		t2.start()		
	if (data == "q"):
		print ("Quit")
		client_socket.send("Quit command accepted: Shutting Down All Recording!")
		break

client_socket.close()
server_socket.close()

