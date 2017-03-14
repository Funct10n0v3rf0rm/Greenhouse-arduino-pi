#print functions are for live monitoring, duplicate info in each log file
#after 90 days, timer will continue to decrement until light timer goes to 0, this will take a very long time
import os
import time
import serial
from serial import SerialException
from threading import Timer
from nanpy import SerialManager
from nanpy import ArduinoApi
connection = SerialManager(device='/dev/ttyACM0')
a = ArduinoApi(connection = connection)
a.pinMode(13, a.OUTPUT) #board status LED
a.pinMode(2,a.OUTPUT) #relay output 1, for lights
a.pinMode(3,a.OUTPUT) #relay output 2, for lights, not used unless needed due to 10 Amp limit
a.pinMode(4,a.OUTPUT) #pump output 1
a.pinMode(5,a.OUTPUT) #pump output 2
os.chdir('/root/Documents/testlogs')
list = os.listdir('/root/Documents/testlogs')
number_files = len(list)
print number_files
file_count = number_files + 1
print file_count
day_counter = 0
now = time.strftime("%c")
time_increment = number_files*3
light_timer = 14
# 14400 = 4 hours 
# 300 = 5 minutes
# 25200 = 7 hours
# 1200 = 20 minutes

print "Startup BIT, LED on Board will Turn on for 5 Seconds, then off if communication is established\n"
print "if LED does not flash, check connections, and try the following from a terminal\n"
print ">>cd /dev\n"
print ">>ls\n"
print "if dev/ttyACM0 is missing from the list, you need to try another port, communication is not established\n"
print ("Current time %s"  % now )


if number_files <= 45:
	with open('testwithboard' + str(file_count), 'w') as f:
		f.write("Current time %s" '\nTest Successful!' % now )
		a.digitalWrite(13, a.HIGH)
		f.write("Led is on")
		print ("Led is on\n")
		time.sleep(5)
		a.digitalWrite(13,a.LOW)
		f.write("LED is OFF")
		print ("LED is OFF\n")
		a.digitalWrite(2,a.LOW)
		f.write("Digital Light Output 2 relay is closed, light should be on")
		print ("Digital Light Output 2 relay is closed, light should be on\n")
		time.sleep(light_timer)
		a.digitalWrite(2,a.HIGH)
		f.write("Digital Light Output 2 relay is open, light should be off")
		print ("Digital Light Output 2 relay is open, light should be off\n")
		light_timer = light_timer + time_increment
		f.write("light timer has incremented, it currently = %s" % light_timer)
		print ("light timer has incremented, it currently = %s\n" % light_timer)
		a.digitalWrite(4,a.LOW)
		f.write("Digital Pump Output 4 is closed, hydro pump should run for one minute")
		print ("Digital Pump Output 4 is closed, hydro pump should run for one minute\n")
		time.sleep(6)
		a.digitalWrite(4,a.HIGH)
		f.write("Digital Pump Output 4 is open, hydro pump should be off")
		print ("Digital Pump Output 4 is open, hydro pump should be off\n")
		f.write("Delaying 5 minutes for water to fill reservoir")
		print ("Delaying 5 minutes for water to fill reservoir\n")
		time.sleep(3)
		a.digitalWrite(5,a.LOW)
		f.write("Digital Pump Output 5 is closed, reservoir pump should be on")
		print ("Digital Pump Output 5 is closed, reservoir pump should be on\n")
		time.sleep(3)
		a.digitalWrite(5,a.HIGH)
		f.write("Digital Pump Output 5 is open, reservoir pump should be off")
		print ("Digital Pump Output 5 is open, reservoir pump should be off\n")
		#a.digitalWrite(2,a.HIGH)
		#a.digitalWrite(3,a.HIGH)
		#a.digitalWrite(4,a.HIGH)
		#a.digitalWrite(5,a.HIGH)
		a.pinMode(2,a.INPUT) #relay output 1, for lights
		a.pinMode(3,a.INPUT) #relay output 2, for lights, not used unless needed due to 10 Amp limit
		a.pinMode(4,a.INPUT) #pump output 1
		a.pinMode(5,a.INPUT) 
		
		time.sleep(10)
		print ("program complete")
		exit()
else:
	with open('testwithboard' + str(file_count), 'w') as f:
		f.write("Current time %s" '\nTest Successful!' % now )
		a.digitalWrite(13, a.HIGH)
		f.write("Led is on")
		print ("Led is on\n")
		time.sleep(5)
		a.digitalWrite(13,a.LOW)
		f.write("LED is OFF")
		print ("LED is OFF\n")
		a.digitalWrite(2,a.LOW)
		f.write("Digital Light Output 2 relay is closed, light should be on")
		print ("Digital Light Output 2 relay is closed, light should be on\n")
		time.sleep(light_timer)
		a.digitalWrite(2,a.HIGH)
		f.write("Digital Light Output 2 relay is open, light should be off")
		print ("Digital Light Output 2 relay is open, light should be off\n")
		light_timer = light_timer - time_increment
		f.write("light timer has incremented, it currently = %s" % light_timer)
		print ("light timer has incremented, it currently = %s\n" % light_timer)
		a.digitalWrite(4,a.LOW)
		f.write("Digital Pump Output 4 is closed, hydro pump should run for one minute")
		print ("Digital Pump Output 4 is closed, hydro pump should run for one minute\n")
		time.sleep(6)
		a.digitalWrite(4,a.HIGH)
		f.write("Digital Pump Output 4 is open, hydro pump should be off")
		print ("Digital Pump Output 4 is open, hydro pump should be off\n")
		f.write("Delaying 5 minutes for water to fill reservoir")
		print ("Delaying 5 minutes for water to fill reservoir\n")
		time.sleep(3)
		a.digitalWrite(5,a.LOW)
		f.write("Digital Pump Output 5 is closed, reservoir pump should be on")
		print ("Digital Pump Output 5 is closed, reservoir pump should be on\n")
		time.sleep(3)
		a.digitalWrite(5,a.HIGH)
		f.write("Digital Pump Output 5 is open, reservoir pump should be off")
		print ("Digital Pump Output 5 is open, reservoir pump should be off\n")
		#a.digitalWrite(2,a.HIGH)
		#a.digitalWrite(3,a.HIGH)
		#a.digitalWrite(4,a.HIGH)
		#a.digitalWrite(5,a.HIGH)
		a.pinMode(2,a.INPUT) #relay output 1, for lights
		a.pinMode(3,a.INPUT) #relay output 2, for lights, not used unless needed due to 10 Amp limit
		a.pinMode(4,a.INPUT) #pump output 1
		a.pinMode(5,a.INPUT) 
		
		time.sleep(10)
		print ("program complete")
		exit()
    
    
    
    
    
	
	



