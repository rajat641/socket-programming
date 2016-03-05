import socket                                         

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# SOCK_STREAM-CONNECTION TYPR TCP/IP
#AF_INET-it is an address family that is used to designate the type of addresses that your socket can communicate(IPv4)


# get local machine name-ip address of machine/server
host = socket.gethostname()                           
port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests/clients
serversocket.listen(5)                                           


 # establish a connection
clientsocket,addr = serversocket.accept()      

clientsocket.send("hello eclipse")# message to be send from server to client
clientsocket.close()#close the socker