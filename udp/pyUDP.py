# pyUDP.py
# 
# M J Stanway 	<m.j.stanway@alum.mit.edu>
# created:    12 May 2009
# updated:

from socket import *

host = '213.123.1.101'
port = 10102
buf = 1024
addr = (host, port)

UDPsock = socket(AF_INET,SOCK_DGRAM)

print 'Enter message to send to Prosilica Camera ', host, ':', port 

while (True):
    msg = raw_input('+>> ')
    if not msg: break
    else:
        if(UDPsock.sendto(msg,addr)):
            print 'Sending message: ', msg, '...'

UDPsock.close()
