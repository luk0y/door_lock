#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from subprocess import call,check_output



GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(12,GPIO.OUT)

while(True):
	bool_test = check_output(["ls","test"])
	string = bool_test.decode("utf-8")
	string  = string[:-1]
	if(string=="success"):
        	GPIO.output(12,GPIO.LOW)
		print("SuccessFully Unlocked")
		call(["rm","test/success"])
	if(string=="fail"):
        	GPIO.output(12,GPIO.HIGH)
		print("LOCKED")
		call(["rm","test/fail"])

