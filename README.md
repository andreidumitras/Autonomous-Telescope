# Autonomous Telescope
This project was my Bachelor's Degree Thesis.
The code controls an automated telescope built from a manual equatorial mount.
The telescope contains:
 - Raspberry Pi3 - the controller
 - one accelerometer
 - one magnetometer
 - one GPS sensor
 - two stepper motors
 - two drivers for the stepper motors
 - one DC source
 - two red LEDs
 - two green LEDs

# What the Autonomous Telescope is offering
The telescope implements three main features:
 - polar alignment assistance
	- guides the user when the telescope is properly polar aligned
	- it uses green and red LEDs to inform the user if he/she has to further adjust the telescope's position, while the accelerometer sensor sends the inclination values with respect to the gravitational acceleration.
 - pinpoint a specified celestial object by its Right Ascension and Declination coordinates.
 - star tracking the specified object over long periods of time
	 - a helpful feature for astrophotography.

# Usage
The telescope is controlled by a Raspberry Pi3. The user should connect to the Raspberry Pi through ssh and start the control algorithm from there.
The program must receive as arguments the Right Ascension and Declination values to start.

# Further development
1. The power source can be portable.
2. An LCD small screen can be added in order to display additional information
3. A mobile application and an online server can be developed. The server will host a database with celestial objects and their coordinates, while the mobile application will let the user specify the celestial object that he/she wants. The application then will send the RA and DEC values to the Raspberry Pi controller connected to the user's smartphone.
