from socket import *
PAYLOAD_LENGTH = 0
TCP_SYN_FLAG = 0
TCP_ACK_FLAG = 0
TCP_FIN_FLAG = 0
HTTP_GET_REQUEST = 0
HTTP_RESPONSE_STATUS_CODE = 0
HTTP_CLIENT_VERSION = 0
HTTP_REQUEST_PATH = 0



serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print("TCP Connection Established\n")

menu = "1. Get a file from the server.\n2. Quit the program."
print(menu)
menuOption = input('\n--Choose an option from the above: --\n')

if menuOption == "1":
    print("Option 1 Se")
    print("1. Use HTTP version 1.0 (non-persistent).\n2. Use HTTP version 1.1 (persistent).")
    HTTPOption = input("\n--Choose an option from the above: --\n")
    if HTTPOption == "1":
        print("-Option 1 selected-\nEnter File Path: ")
        filepath = input()
        clientSocket.send(filepath.encode())

    elif HTTPOption == "2":
        print("-Option 2 selected-\n")
        filepath = input
        clientSocket.send(b"GET / HTTP/1.1\r\nHost:localhost/{}\r\n\r\n".format(filepath))

elif menuOption == "2":
    quit()

#sentence = input('Input lowercase sentence:')
#clientSocket.send(sentence.encode())
output = clientSocket.recv(1024)
print ('From Server:', output.decode())
clientSocket.close()
