import serial              
from time import sleep
import sys

class GPS:
	def __init__(self, serial_port):
		self.serial_port = serial_port
	
	def convert_to_degrees(raw_value):
		decimal_value = raw_value / 100.00
		degrees = int(decimal_value)
		mm_mmmm = (decimal_value - int(decimal_value)) / 0.6
		position = degrees + mm_mmmm
		position = "%.4f" % (position)
		return position

	def start(self):
		threading.Thread(target = self.vk2828u7g5lf).start()

	def vk2828u7g5lf(self):
		ser = serial.Serial(self.serial_port)
		gpgga_info = "$GPGGA,"
		GPGGA_buffer = 0
		NMEA_buff = 0
		try:
			while True:
				received_data = (str)(ser.readline())					#read NMEA string received
				GPGGA_data_available = received_data.find(gpgga_info)	#check for NMEA GPGGA string                
				if (GPGGA_data_available > 0):
					GPGGA_buffer = received_data.split("$GPGGA,", 1)[1]	#store data coming after “$GPGGA,” string
					NMEA_buff = (GPGGA_buffer.split(','))
					# nmea_time = []
					nmea_latitude = []
					# nmea_longitude = []
					# nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
					nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
					# nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string
					# print("NMEA Time: ", nmea_time,'\n')
					lat = (float)(nmea_latitude)
					lat = convert_to_degrees(lat)
					# longi = (float)(nmea_longitude)
					# longi = convert_to_degrees(longi)
					# print ("NMEA Latitude:", lat,"NMEA Longitude:", longi,'\n') 
		except Exception as e:
			print(e)
