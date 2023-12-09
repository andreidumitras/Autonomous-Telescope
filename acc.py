
from mpu9250_i2c import *
from time import sleep

sleep(1) 

print('recording data')
while 1:
	try:
		ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
		mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
	except:
		continue
	
	print('{}'.format('-'*30))
	print('accel [g]: x = {0:2.2f}, y = {1:2.2f}, z {2:2.2f}= '.format(ax,ay,az))
	print('gyro [dps]:  x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(wx,wy,wz))
	print('mag [uT]:   x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(mx,my,mz))
	print('{}'.format('-'*30))
	sleep(1)
