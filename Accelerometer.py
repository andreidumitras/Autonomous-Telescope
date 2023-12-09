# (C) Andrei Dumitras, July 2022
#
#  > Faculty of Automation and Computer Science | Automation and Applied Informatics
#  > Bachelor's Thesis: AUTONOMPUS TELESCOPE
#
#  > Accelerometer module

import mpu9250_i2c as mpu9250
import threading
from time import sleep

class Accelerometer:
	'''
	__init__()
	Initialize a new Accelerometer object with all the axis values to be 0
	'''
	def __init__(self):
		# initial accelerometer data is set to 0
		self.ax, self.ay, self.az = 0

	'''
	start()
	start a new thread for the accelerometer chip: mpu6050
	'''
	def start(self):
		threading.Thread(target = self.mpu6050).start()

	'''
	mpu6050()
	Accuire data from the sensor.
	'''
	def mpu6050(self):
		# delay necessary to allow mpu9250 to settle
		sleep(1)
		# accuire data continuously
		while True:
			try:
				# fill in the axis of the accelerometer with data read by mpu6050 sensor
				self.ax, self.ay, self.az = mpu9250.mpu6050_conv()
			except:
				# if something goes wrong, read data again next iteration
				continue
			sleep(0.01)
