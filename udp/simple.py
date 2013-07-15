#!/usr/bin/env python
# Server program

from socket import *

# Set the socket parameters
#host = "127.127.0.1"
#host = "localhost"
host = "198.17.154.199"
port = 33333
buf = 1024*4
addr = (host,port)

# Create socket and bind to address
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)

# Receive messages
while True:
	data,addr = UDPSock.recvfrom(buf)
	if not data:
		print "Client has exited!"
		break
	else:
		print "\nReceived message '", data,"'"

# Close socket
UDPSock.close()
