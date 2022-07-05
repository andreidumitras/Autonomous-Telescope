from mpu9250_i2c import *
import threading

class Accelerometer:
	def __init__(self):
		self.ax, self.ay, self.az = 0	# initialize the accelerometer data	

	def start(self):
        threading.Thread(target = self.mpu6050).start()

	def mpu6050(self):
		# time.sleep(1)	# delay necessary to allow mpu9250 to settle
		while True:
			try:
				self.ax, self.ay, self.az = mpu6050_conv() # read and convert mpu6050 data
			except:
				continue
			time.sleep(0.01)
