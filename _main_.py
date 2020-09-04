#!/usr/bin/python3
# -*- coding: utf-8 -*-

import speech_recognition as sr

from queries import *

from subprocess import call

import pyttsx3

import time 



engine = pyttsx3.init()
r = sr.Recognizer()
engine.say("Hello boss, Welcome to my project")
engine.runAndWait()
time.sleep(1)
engine.say("Tell me what I have to do boss")
engine.runAndWait()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Say Lock/Unlock the door\n")
		audio=r.listen(source)
		print("Recorded\n")
	try:
		userdata=r.recognize_google(audio).lower()
		print("You said:- " + r.recognize_google(audio))
		if(userdata in unlock):
			call(["touch", "success"])
			call(["scp","success","pi@192.168.4.1:/home/pi/Desktop/project/output"])
			call(["rm", "success"])
			engine.say('Door Unlocked')
			engine.runAndWait()
		elif(userdata in lock):
			call(["touch", "fail"])
			call(["scp","fail","pi@192.168.4.1:/home/pi/Desktop/project/output"])
			call(["rm", "fail"])
			engine.say('Door locked')
			engine.runAndWait()
		else:
			engine.say('I am not human to understand whatever you say')
			engine.runAndWait()
	except sr.UnknownValueError:
         	 print("Could not understand audio")
	




