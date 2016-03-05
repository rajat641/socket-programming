# importing socket module containing various functions
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# SOCK_STREAM-CONNECTION TYPR TCP/IP
#AF_INET-it is an address family that is used to designate the type of addresses that your socket can communicate(IPv4)


# get local machine name-ip address of machine/server
host = socket.gethostname()                           
port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes of data 
tm = s.recv(1024)                                     
print tm
s.close()# close the socket

