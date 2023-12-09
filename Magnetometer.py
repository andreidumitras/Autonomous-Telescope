# (C) Andrei Dumitras, July 2022
#
#  > Faculty of Automation and Computer Science | Automation and Applied Informatics
#  > Bachelor's Thesis: AUTONOMPUS TELESCOPE
#
#  > Magnetometer module

import mpu9250_i2c as mpu9250
import threading
from time import sleep

class Magnetometer:
	'''
	__init__()
	Initialize a new Magnetometer object with all the axis values to be 0
	'''
	def __init__(self):
		# initial magnetometer data is set to 0
		self.mx, self.my, self.mz = 0

	'''
	start()
	start a new thread for the magnetometer chip: ak8963
	'''
	def start(self):
		threading.Thread(target = self.ak8963).start()

	'''
	ak8963()
	Accuire data from the sensor.
	'''
	def ak8963(self):
		# delay necessary to allow mpu9250 to settle
		sleep(1)
		# accuire data continuously
		while True:
			try:
				# fill in the axis of the magnetometer with data read by ak8963 sensor
				self.mx, self.my, self.mz = mpu9250.AK8963_conv()
			except:
				# if something goes wrong, read data again next iteration
				continue
			sleep(0.01)
