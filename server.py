import socket

def server():
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname(socket.gethostname())
        port = 8000
        serversocket.bind((host, port))
        serversocket.listen()
    except:
        pass
    else:
        while True:
            try:
                (clientsocket, address) = serversocket.accept()
                data = clientsocket.recv(1024).decode()
                if data != '':
                    print(data)

            except:
                pass

while True:
    try:
        server()
    except:
        pass
