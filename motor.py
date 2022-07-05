import RPi.GPIO as GPIO
import time

class Motor:
	MAX_SPEED = 100000

	def __init__(self, pin_puls, pin_dir):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.pin_puls = pin_puls
		self.pin_dir = pin_dir
		GPIO.setup(self.pin_puls, GPIO.OUT)
		GPIO.setup(self.pin_dir, GPIO.OUT)
	
	def step(self, direction):
		if speed > MAX_SPEED:
			speed = MAX_SPEED
		GPIO.output(pin_dir, direction)
		GPIO.output(pin_puls, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(pin_puls, GPIO.LOW)

	def spin_deg(self, deg, direction, speed):
		resolution = 800	# from the switches register
		pulse = 360 / resolution	# the amount of degrees for 1 pulse
		steps = round(deg / pulse)
		GPIO.output(pin_dir, direction)
		if speed > MAX_SPEED:
			speed = MAX_SPEED
		for i in range(1, steps):
			GPIO.output(pin_puls, GPIO.HIGH)
			time.sleep(1/speed)
			GPIO.output(pin_puls, GPIO.LOW)
			time.sleep(1/speed)
		return steps
