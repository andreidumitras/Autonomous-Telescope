from Motor import *
from Accelerometer import *
from Magnetometer import *
from GPS import *

# def polar_alignment_assistant():
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

def pinpoint(RA, DEC):
	if RA < 0:
		direction1 = 0
	else
		direction1 = 1
	if DEC < 0:
		direction2 = 0
	else
		direction2 = 1
	stepper1.spin_deg(abs(RA), direction1, 100)
	stepper2.spin_deg(abs(DEC), direction2, 100)

def star_tracking():
	while True:
		stepper1.step(1)
		time.sleep(1.125)

try:
	if len(sys.argv) != 2:
		print("Error: bad number of arguments")
		sys.exit(0)
	# polar_alignment_assistant()
	RA = int(sys.argv[1])
	DEC = int(sys.argv[2])
	stepper1 = Motor(17, 27)
	stepper2 = Motor(22, 23)
	pinpoint(RA, DEC)
	star_tracking()

except KeyboardInterrupt:
	# opreste toate thread-urile
	sys.exit(0)
