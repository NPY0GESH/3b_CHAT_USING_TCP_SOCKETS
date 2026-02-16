import socket
s=socket.socket()
s.bind(('localhost', 8000))
s.listen(1)
print("Waiting for connection...")
c, addr=s.accept()
print("Connected to", addr)
while True:
    clientMessage = c.recv(1024).decode()  
    if clientMessage.lower() == "exit":
        print("Client disconnected")
        break
    print("Client >", clientMessage)
    msg = input("Server > ")
    c.send(msg.encode())
    if msg.lower() == "exit":
        print("Server stopped")
        break
c.close()
s.close()