# (C) Andrei Dumitras, July 2022
#
#  > Faculty of Automation and Computer Science | Automation and Applied Informatics
#  > Bachelor's Thesis: AUTONOMPUS TELESCOPE
#
#  > GPS module

import serial
from time import sleep
import threading

class GPS:
	'''
	__init__(serial_port)
	Initialize a new GPS object with the specified serial port.
	'''
	def __init__(self, serial_port):
		self.serial_port = serial_port
	
	'''
	convert_to_degrees(raw_value)
	It converts to degrees from the raw value that is read by the sensor.
	'''
	def convert_to_degrees(raw_value):
		# convert to decimal value
		decimal_value = raw_value / 100.00
		# convert to integer degrees
		degrees = int(decimal_value)
		# compute the minutes
		mins = (decimal_value - int(decimal_value)) / 0.6
		# compute the position in degrees and minutes
		position = degrees + mins
		return position

	'''
	start()
	start a new thread for the GPS chip: vk2828u7g5lf
	'''
	def start(self):
		threading.Thread(target = self.vk2828u7g5lf).start()

	'''
	vk2828u7g5lf()
	Accuire data from the sensor.
	'''
	def vk2828u7g5lf(self):
		# accuire data from the serial protocol
		ser = serial.Serial(self.serial_port)
		# initialize the buffers
		gpgga_info = "$GPGGA,"
		GPGGA_buffer = 0
		NMEA_buff = 0
		try:
			# accuire data continuously
			while True:
				# read NMEA string received
				received_data = (str)(ser.readline())
				# check for NMEA GPGGA string
				GPGGA_data_available = received_data.find(gpgga_info)
				if (GPGGA_data_available > 0):
					# store data coming after "$GPGGA," string
					GPGGA_buffer = received_data.split("$GPGGA,", 1)[1]
					NMEA_buff = (GPGGA_buffer.split(','))
					nmea_latitude = []
					# extract latitude from GPGGA string
					nmea_latitude = NMEA_buff[1]
					lat = (float)(nmea_latitude)
					lat = self.convert_to_degrees(lat)
		except Exception as e:
			print(e)
