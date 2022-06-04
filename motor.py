import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# declarare pini ce trebe folositi.
pinMotor = 11

GPIO.setup(pinMotor, GPIO.OUT)

pwmMotor = GPIO.PWM(pinMotor, 100)
pwmMotor.start(50)

haida = True
while haida:
	dutyc = input("Enter ducy cycle (1 for exit): ")
	if dutyc == 1:
		haida = False
	pwmMotor.ChangeDutyCycle(int(ducyc))

GPIO.cleanup()

print("Finish!")
