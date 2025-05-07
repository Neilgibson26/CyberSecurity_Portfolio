#!/bin/python3

import sys #allows me to enter command line arguments, among other things
import socket

from datetime import datetime

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate a host name to IPV4
else:
	print("invalid amount of arguements")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()
	
#add banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		result = s.connect_ex((target, port)) #returns error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.error:
	print("Could not connect to server")
	sys.exit()