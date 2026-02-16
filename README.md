# 3b.CREATION FOR CHAT USING TCP SOCKETS
## AIM
To write a python program for creating Chat using TCP Sockets Links.
## ALGORITHM:
## Algorithm-server
1 Start

2 Import socket module

3 Create socket

4 Bind socket with localhost and port 8000

6 Listen for connection

7 Accept client connection

8 Receive message from client

9 If message is "exit", stop

10 Display client message

12 Send reply to client

13 Repeat steps 7–10

14 Close socket

15 Stop

## Algorithm – Client
1 Start

2 Import socket module

3 Create socket

4 Connect to server

5 Enter message

6 Send message to server

7 If message is "exit", stop

8 Receive reply from server

9 Display reply

10 Repeat steps 5–9

11 Close socket

12 Stop

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
