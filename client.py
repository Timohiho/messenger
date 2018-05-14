import socket
def client(host, message):
   host = socket.gethostbyname(str(host))
   port = 8000

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((host, port))
   s.send(str(message).encode())
   s.close()

client('server host name', 'message')

