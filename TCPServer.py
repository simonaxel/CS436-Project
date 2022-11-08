from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while 1:
    



    connectionSocket, addr = serverSocket.accept()
    print("CONNECTION ESTABLISHED with {}".format(serverSocket))
    request = connectionSocket.recv(1024).decode()
    #do something with request
    #Request = filepath
    with open(request, 'r') as file:
        data = file.read()
        file.close()
    connectionSocket.send(data.encode())
    connectionSocket.close()
