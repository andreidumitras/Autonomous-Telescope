from mpu9250_i2c import *
import threading

class Magnetometer:
	def __init__(self):
		self.mx, self.my, self.mz = 0 # initialize the magnetometer data

	def start(self):
        threading.Thread(target = self.ak8963).start()

	def ak8963(self):
		# time.sleep(1)	# delay necessary to allow mpu9250 to settle
		while True:
			try:
				self.mx, self.my, self.mz = AK8963_conv() # read and convert mpu6050 data
			except:
				continue
			time.sleep(0.01)
