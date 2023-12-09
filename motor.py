# (C) Andrei Dumitras, July 2022
#
#  > Faculty of Automation and Computer Science | Automation and Applied Informatics
#  > Bachelor's Thesis: AUTONOMPUS TELESCOPE
#
#  > Motor module

import RPi.GPIO as GPIO
from time import sleep

class Motor:
	MAX_SPEED = 100000
	
	'''
	__init__(pin_puls, pin_dir)
	Initialize a new Motor object with the specified pins, inside the Raspberry Pi
	'''
	def __init__(self, pin_puls, pin_dir):
		# initialize the Raspberry Pi environment
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		# fill the atributes:
		self.pin_puls = pin_puls
		self.pin_dir = pin_dir
		# initialize the Raspberry Pi pins with the ones montioned
		GPIO.setup(self.pin_puls, GPIO.OUT)
		GPIO.setup(self.pin_dir, GPIO.OUT)
	'''
	step(direction)
	go one step to the given direction
	'''
	def step(self, direction):
		# set up pin_dir to be an output pin for direction:
		GPIO.output(self.pin_dir, direction)
		# let current pass
		GPIO.output(self.pin_puls, GPIO.HIGH)
		# maintain it for 0.001 sec
		time.sleep(0.001)
		# stop current pass
		GPIO.output(self.pin_puls, GPIO.LOW)

	'''
	step_deg(deg, direction, speed)
	steps until deg - the amount specified in degrees - is reached, with a certain direction and a certain speed.
	'''
	def spin_deg(self, deg, direction, speed):
		# set the resolution from the switches register
		resolution = 800
		# compute the amount of degrees in one pulse
		pulse = 360 / resolution
		# compute the number of steps to be taken
		steps = round(deg / pulse)
		# set up pin_dir to be an output pin for the specified direction:
		GPIO.output(self.pin_dir, direction)
		# bound the speed if is to high
		if speed > MAX_SPEED:
			speed = MAX_SPEED

		# for each step to be taken
		for i in range(1, steps):
			# let the current pass
			GPIO.output(self.pin_puls, GPIO.HIGH)
			# miantain it
			time.sleep(1/speed)
			# stop the current flow
			GPIO.output(self.pin_puls, GPIO.LOW)
			# wait a bit and start again for the next step.
			time.sleep(1/speed)
