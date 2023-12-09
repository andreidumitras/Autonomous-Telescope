# (C) Andrei Dumitras, July 2022
#
#  > Faculty of Automation and Computer Science | Automation and Applied Informatics
#  > Bachelor's Thesis: AUTONOMPUS TELESCOPE
#
#  > main module

import Motor
import Accelerometer
import Magnetometer
import GPS
import sys
from time import sleep

'''
The polar_alignment_assistant function:
Parameters:
	RA = Right Ascension (int)
	DEC = Declination (int)
Behavior:
 - lights the red LEDs until the polar alignment is reached
 - lights the green LEDs when the polar alignment is met.
 - for joint 1, the telescope must be aligned to the Geographic North. This is done with the help of Magnetometer form MPU9250.
 - for joint 2, the telescope must be aligned to the Earth's Latitude. This is done with the help of GPS sensor form MPU9250.
 - when the joint 1 is aligned by the user to the Geographic North, the green LED1 will be lit.
 - when the joint 2 is aligned by the user to the Earth's Latitude, the green LED2 will be lit.
 - until then, both red LEDs will be on.
'''
# def polar_alignment_assistant():
# 	TO DO:
#
# 	pin_led1_red = 5
# 	pin_led1_green = 6
# 	pin_led2_red = 16
# 	pin_led2_green = 26
# 	GPIO.setmode(GPIO.BCM)
# 	GPIO.setwarnings(False)
# 	GPIO.setup(pin_led1_green, GPIO.OUT)
# 	GPIO.setup(pin_led1_red, GPIO.OUT)
# 	GPIO.setup(pin_led2_green, GPIO.OUT)
# 	GPIO.setup(pin_led2_red, GPIO.OUT)
# 	while True:
# 	GPIO.output(14,GPIO.HIGH)

'''
The pinpoint function:
Parameters:
	RA = Right Ascension (int)
	DEC = Declination (int)
Behavior:
 - actuates the stepper motors to move the telescope end to the given coordinates
'''
def pinpoint(RA, DEC):
	# set the directions for the two motors to be left or right.
	# direction for the first motor
	if RA < 0:
		direction1 = 0
	else:
		direction1 = 1
	# direction for the second motor
	if DEC < 0:
		direction2 = 0
	else:
		direction2 = 1
	# actuate on the first motor to follow RA with 100 speed
	stepper1.spin_deg(abs(RA), direction1, 100)
	# actuate on the second motor to follow DEC with 100 speed
	stepper2.spin_deg(abs(DEC), direction2, 100)

'''
The star_tracking function:
Parameters: None
Behavior:
 - 	actuates the stepper motors to move continuous the telescope end along the sky, until is stopped.
'''
def star_tracking():
	# always track the fixed point
	while True:
		# step after 1.125 seconds with only 1 microstep. The direction is always the same for the Northern Hemisphere.
		stepper1.step(1)
		sleep(1.125)


# ----------------- main -----------------
try:
	# It expects to recieve 2 arguments beside the name of the module.
	# If the arguments are not fully provided, the user should be notified.
	if len(sys.argv) != 3:
		print("Error: bad number of arguments")
		print("usage: python3 main.py [Right Ascension] [Declination]")
		sys.exit(0)

	# fill the values for RA and DEC from the command line arguments
	RA = int(sys.argv[1])		# RA = Right Ascension
	DEC = int(sys.argv[2])		# Declination

	# first function to be started is the polar_alignment_assistant.
	# polar_alignment_assistant(RA, DEC)

	# initialize the stepper motors (pulse_pin, direction_pin):
	stepper1 = Motor(17, 27)
	stepper2 = Motor(22, 23)
	# action the motors:
	pinpoint(RA, DEC)

	# start the star tracking process:
	star_tracking()

except KeyboardInterrupt:
	# turn off the entire execution
	sys.exit(0)
