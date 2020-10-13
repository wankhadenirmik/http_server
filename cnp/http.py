from socket import *
import sys
port = int(sys.argv[1])
server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', port))

server.listen(1)
print("Server is ready!! listening on port:", port)

while True:
    clientconnect, addr = server.accept()
    print('requested accepted:{}'.format(addr))
    request = clientconnect.recv(1024).decode() 
    header = request.split()
    print(header[0])
    if header[0] == 'GET':
        print("i am groot")
        filename = header[1]
        print(filename)
        if filename == '/':
            filename = '/index.html'
            print(filename)
        try:
            f = open('htdocs'+ filename, 'rb')
            c = f.read()
            f.close()
        except:
            c = "fiel not found:"
        httpresponse = 'HTTP/1.0 200 OK\n\n'+ c
        clientconnect.send(httpresponse.encode())
    clientconnect.close()