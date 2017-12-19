#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
 
import time
import atexit

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x6F)

myMotor = mh.getMotor(3)

print "Forward! "
myMotor.run(Adafruit_MotorHAT.FORWARD)
 
print "\tSpeed up..."
for i in range(255):
	myMotor.setSpeed(i)
	time.sleep(0.01)

mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)	

# while (True):
# 	print "Forward! "
# 	myMotor.run(Adafruit_MotorHAT.FORWARD)
 
# 	print "\tSpeed up..."
# 	for i in range(255):
# 		myMotor.setSpeed(i)
# 		time.sleep(0.01)
