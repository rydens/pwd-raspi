#!/usr/bin/env python3
# The main file for the onboard Pi, needs to run on boot as a dtach
import RPi.GPIO as GPIO
import os
import skilstak.colors as c
from getch import getch

pins = [4,17,22,23,5,13,12,16]	# The GPIO pin numbers to set up


# Set up the LED pins for output
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins,0)

r1 = 0
r2 = 0
y1 = 0
y2 = 0
g1 = 0
g2 = 0
b1 = 0
b2 = 0

# Main thing
while True:
	key = getch()
	if key == "2":
		if r1 == 0:
			GPIO.output(pins[0],1)
			r1 = 1
		elif r1 == 1:
			GPIO.output(pins[0],0)
			r1 = 0
	elif key == "3":
		if r2 == 0:
			GPIO.output(pins[1],1)
			r2 = 1
		elif r2 == 1:
			GPIO.output(pins[1],0)
			r2 = 0
	elif key == "5":
		if y1 == 0:
			GPIO.output(pins[2],1)
			y1 = 1
		elif y1 == 1:
			GPIO.output(pins[2],0)
			y1 = 0
	elif key == "6":
		if y2 == 0:
			GPIO.output(pins[3],1)
			y2 = 1
		elif y2 == 1:
			GPIO.output(pins[3],0)
			y2 = 0
	elif key == "8":
		if g1 == 0:
			GPIO.output(pins[4],1)
			g1 = 1
		elif g1 == 1:
			GPIO.output(pins[4],0)
			g1 = 0
	elif key == "9":
		if g2 == 0:
			GPIO.output(pins[5],1)
			g2 = 1
		elif g2 == 1:
			GPIO.output(pins[5],0)
			g2 = 0
	elif key == "/":
		if b1 == 0:
			GPIO.output(pins[6],1)
			b1 = 1
		elif b1 == 1:
			GPIO.output(pins[6],0)
			b1 = 0
	elif key == "*":
		if b2 == 0:
			GPIO.output(pins[7],1)
			b2 = 1
		elif b2 == 1:
			GPIO.output(pins[7],0)
			b2 = 0
	elif key == "0":
		if r1 == 1 or r2 == 1 or y1 == 1 or y2 == 1 or g1 == 1 or g2 == 1 or b1 == 1 or b2 == 1:
			GPIO.output(pins,0)
			r1 = 0
			r2 = 0
			y1 = 0
			y2 = 0
			g1 = 0
			g2 = 0
			b1 = 0
			b2 = 0
		elif r1 == 0 and r2 == 0 and y1 == 0 and y2 == 0 and g1 == 0 and g2 == 0 and b1 == 0 and b2 == 0:
			GPIO.output(pins,1)
			r1 = 1
			r2 = 1
			y1 = 1
			y2 = 1
			g1 = 1
			g2 = 1
			b1 = 1
			b2 = 1
	elif key == "1":
		if r1 == 1 or r2 == 1:
			GPIO.output(pins[0],0)
			r1 = 0
			GPIO.output(pins[1],0)
			r2 = 0
		elif r1 == 0 and r2 == 0:
			GPIO.output(pins[0],1)
			r1 = 1
			GPIO.output(pins[1],1)
			r2 = 1
	elif key == "4":
		if y1 == 1 or y2 == 1:
			GPIO.output(pins[2],0)
			y1 = 0
			GPIO.output(pins[3],0)
			y2 = 0
		elif y1 == 0 and y2 == 0:
			GPIO.output(pins[2],1)
			y1 = 1
			GPIO.output(pins[3],1)
			y2 = 1
	elif key == "7":
		if g1 == 1 or g2 == 1:
			GPIO.output(pins[4],0)
			g1 = 0
			GPIO.output(pins[5],0)
			g2 = 0
		elif g1 == 0 and g2 == 0:
			GPIO.output(pins[4],1)
			g1 = 1
			GPIO.output(pins[5],1)
			g2 = 1
	elif key == "-":
		if b1 == 1 or b2 == 1:
			GPIO.output(pins[6],0)
			b1 = 0
			GPIO.output(pins[7],0)
			b2 = 0
		elif b1 == 0 and b2 == 0:
			GPIO.output(pins[6],1)
			b1 = 1
			GPIO.output(pins[7],1)
			b2 = 1
	elif key == '\x03':
		GPIO.cleanup()
		raise KeyboardInterrupt()

	
	
	
	
	
	


	
