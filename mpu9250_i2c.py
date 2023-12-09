# (C) Andrei Dumitras, July 2022
#
#  > Faculty of Automation and Computer Science | Automation and Applied Informatics
#  > Bachelor's Thesis: AUTONOMPUS TELESCOPE
#
#  > mpu9250_i2c module

# This module was addapted after one module found online

# this is to be saved in the local folder under the name "mpu9250_i2c.py"
# it will be used as the I2C controller and function harbor for the project 
# refer to datasheet and register map for full explanation

import smbus
from time import sleep

def MPU6050_start():
	# alter sample rate (stability)
	# sample rate = 8 kHz/(1 + samp_rate_div)
	samp_rate_div = 0
	bus.write_byte_data(MPU6050_ADDR, SMPLRT_DIV, samp_rate_div)
	sleep(0.1)

	# reset all sensors
	bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0x00)
	sleep(0.1)
	
	# power management and crystal settings
	bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0x01)
	sleep(0.1)
	
	# Write to Configuration register
	bus.write_byte_data(MPU6050_ADDR, CONFIG, 0)
	sleep(0.1)
	
	# Write to Accel configuration register
	accel_config_sel = [0b00000, 0b01000, 0b10000, 0b11000]				# byte registers
	accel_config_vals = [2.0, 4.0, 8.0, 16.0]							# g (g = 9.81 m/s^2)
	accel_indx = 0
	bus.write_byte_data(MPU6050_ADDR, ACCEL_CONFIG, int(accel_config_sel[accel_indx]))
	sleep(0.1)
	
	# interrupt register (related to overflow of data [FIFO])
	bus.write_byte_data(MPU6050_ADDR, INT_ENABLE, 1)
	sleep(0.1)
	
	return accel_config_vals[accel_indx]
	
def read_raw_bits(register):
	# read accel and gyro values
	high = bus.read_byte_data(MPU6050_ADDR, register)
	low = bus.read_byte_data(MPU6050_ADDR, register+1)

	# combine higha and low for unsigned bit value
	value = ((high << 8) | low)
	
	# convert to +- value
	if(value > 32768):
		value -= 65536
	return value

def mpu6050_conv():
	# raw acceleration bits
	acc_x = read_raw_bits(ACCEL_XOUT_H)
	acc_y = read_raw_bits(ACCEL_YOUT_H)
	acc_z = read_raw_bits(ACCEL_ZOUT_H)

	#convert to acceleration in g and gyro dps
	a_x = (acc_x / (2.0**15.0)) * accel_sens
	a_y = (acc_y / (2.0**15.0)) * accel_sens
	a_z = (acc_z / (2.0**15.0)) * accel_sens

	return a_x, a_y, a_z

def AK8963_start():
	bus.write_byte_data(AK8963_ADDR, AK8963_CNTL, 0x00)
	sleep(0.1)
	AK8963_bit_res = 0b0001				# 0b0001 = 16-bit
	AK8963_samp_rate = 0b0110 			# 0b0010 = 8 Hz, 0b0110 = 100 Hz
	
	# bit conversion
	AK8963_mode = (AK8963_bit_res << 4) + AK8963_samp_rate
	bus.write_byte_data(AK8963_ADDR, AK8963_CNTL, AK8963_mode)
	sleep(0.1)
	
def AK8963_reader(register):
	# read magnetometer values
	low = bus.read_byte_data(AK8963_ADDR, register-1)
	high = bus.read_byte_data(AK8963_ADDR, register)
	
	# combine higha and low for unsigned bit value
	value = ((high << 8) | low)
	
	# convert to +- value
	if(value > 32768):
		value -= 65536
	return value

def AK8963_conv():
	# raw magnetometer bits
	loop_count = 0
	while 1:
		mag_x = AK8963_reader(HXH)
		mag_y = AK8963_reader(HYH)
		mag_z = AK8963_reader(HZH)

		# the next line is needed for AK8963
		if bin(bus.read_byte_data(AK8963_ADDR, AK8963_ST2)) == '0b10000':
			break
		loop_count += 1

	#convert to acceleration in g and gyro dps
	m_x = (mag_x / (2.0**15.0)) * mag_sens
	m_y = (mag_y / (2.0**15.0)) * mag_sens
	m_z = (mag_z / (2.0**15.0)) * mag_sens

	return m_x, m_y, m_z
	
# MPU6050 Registers
MPU6050_ADDR = 0x68
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
ACCEL_CONFIG = 0x1C
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
TEMP_OUT_H   = 0x41

# AK8963 registers
AK8963_ADDR  = 0x0C
AK8963_ST1   = 0x02
HXH          = 0x04
HYH          = 0x06
HZH          = 0x08
AK8963_ST2   = 0x09
AK8963_CNTL  = 0x0A

# magnetometer sensitivity: 4800 uT
mag_sens = 4900.0 

# start I2C driver
# start comm with i2c bus
bus = smbus.SMBus(1)

# instantiate gyro/accel
accel_sens = MPU6050_start() 
# instantiate magnetometer
AK8963_start() 
