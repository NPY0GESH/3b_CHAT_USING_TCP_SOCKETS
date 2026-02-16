import socket
s=socket.socket()
s.connect(('localhost', 8000))
print("Connected to server")
while True:
    msg = input("Client > ")
    s.send(msg.encode())
    if msg.lower() == "exit":
        print("Disconnected from server")
        break
    serverReply = s.recv(1024).decode()    
    if serverReply.lower() == "exit":
        print("Server closed connection")
        break 
    print("Server >", serverReply)
s.close()