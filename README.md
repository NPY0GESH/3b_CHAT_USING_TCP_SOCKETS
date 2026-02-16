# 3b.CREATION FOR CHAT USING TCP SOCKETS
## AIM
To write a python program for creating Chat using TCP Sockets Links.
## ALGORITHM:
Start

Import socket module

Create socket

Bind socket with localhost and port 8000

Listen for connection

Accept client connection

Receive message from client

If message is "exit", stop

Display client message

Send reply to client

Repeat steps 7–10

Close socket

Stop

Algorithm – Client
Start

Import socket module

Create socket

Connect to server

Enter message

Send message to server

If message is "exit", stop

Receive reply from server

Display reply

Repeat steps 5–9

Close socket

Stop

## PROGRAM
client.py
```
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
```
server.py
```
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
```

## OUPUT
server.py
![alt text](<Screenshot 2026-02-16 155838.png>)
client.py
![alt text](<Screenshot 2026-02-16 155846.png>)
## RESULT
Thus, the python program for creating Chat using TCP Sockets Links was successfully 
created and executed.
