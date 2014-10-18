'''
Script to run a terminal based alarm clock that 
pings, shows a dialog box and plays a song when the alarm ticks off.
'''

import time
from time import sleep
from pygame import mixer
import easygui

hours = float(input("Please enter the hours? 0 to 23 "))

if hours < 0 or hours > 23:
	print "Invalid value for hours, should be >= 0 or <=23"
	sys.exit(1)

minutes = float(input("Please enter the minutes?  "))

if minutes < 0 or minutes > 59:
	print "Invalid value for minutes, should be >= 0 or <=59"
	sys.exit(1)

if minutes == 1:
	unit_word = " minute"
else:
	unit_word = " minutes"

now_hour = time.strftime("%H")
now_min = time.strftime("%M")

if float(now_hour) != hours or float(now_min) != minutes:
	min_hours = (hours - float(now_hour)) * 60
	min_mins = minutes - float(now_min)
	total = min_hours + min_mins
	sec = total * 60
	if total > 0:
			print "Sleeping for " + str(total) + unit_word
			sleep(sec)
			print "WAAAKE UP!!!!"
			mixer.init()
			mixer.music.load('/home/divya/Music/pink')
			mixer.music.play()
			easygui.msgbox(msg="Time up!!!!", title= "J.A.R.V.I.S")
	for i in range(5):
		print "Alarm ringing!!", chr(7)
		sleep(1)