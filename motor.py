import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# declarare pini ce trebe folositi.
GPIO.setup(14,GPIO.OUT)

# While loop
while True:
        # set GPIO14 pin to HIGH
        GPIO.output(14, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)

        # set GPIO14 pin to LOW
        GPIO.output(14,GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)