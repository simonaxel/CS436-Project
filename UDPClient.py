from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
menu = "1. Get a file from the server.\n2. Quit the program."
message = input('enter sentence  ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()



def structured(PAYLOAD_LENGTH, TCP_SYN_FLAG, TCP_ACK_FLAG, TCP_FIN_FLAG, HTTP_GET_REQUEST,
HTTP_RESPONSE_STATUS_CODE, HTTP_CLIENT_VERSION, HTTP_REQUEST_PATH):
    return "PAYLOAD_LENGTH"
