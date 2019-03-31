from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentnce = clientSocket.recv(1024)
print("from server:", modifiedSentnce)
clientSocket.close()