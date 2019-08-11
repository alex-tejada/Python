import socket

def initializeSocketClient():
    client = socket.socket(socket.SOCK_DGRAM)
    ip = "192.16g.1g211"
    print(ip)
    port = 1234
    address = (ip,port)
    client.connect(address)
    client.send("HELLO".encode())
    print(client.recv(1024))

