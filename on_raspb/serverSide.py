import RPi.GPIO as GPIO
import time
from subprocess import call,check_output
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)

while(True):
	mad = check_output(["ls","test"])
	string = mad.decode("utf-8")
	string  = string[:-1]
	if(string=="success"):
        	GPIO.output(12,GPIO.LOW)
		print("SuccessFully Unlocked")
		call(["rm","test/success"])
	if(string=="fail"):
        	GPIO.output(12,GPIO.HIGH)
		print("LOCKED")
		call(["rm","test/fail"])

