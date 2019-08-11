import socket

def initializeSocketServer():
    server = socket.socket(socket.SOCK_DGRAM)
    name = socket.gethostname()
    print(name)
    ip = socket.gethostbyname(name)
    port = 1234
    address = (ip,port)
    server.bind(address)
    server.listen(1)
    print("Server Started on ip ",ip," port ",port)
    client,addr = server.accept()
    print("New Conecction from ",addr[0]," port ",addr[1])
    while True:
        data = client.recv(1024)
        print("Data received: ",data.decode())
        client.send("hello client".encode())
        print("reply sended ",client)

