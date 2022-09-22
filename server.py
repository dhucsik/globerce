
import socket
from _thread import *
 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
IP_address = socket.gethostname()
 
Port = 5000

server.bind((IP_address, Port))
 
server.listen(100)
 
list_of_clients = []

nicks_of_clients = dict()
 
def clientthread(conn, addr):
 
    conn.send("Welcome to this chatroom!".encode())
 
    while True:
            try:
                message = conn.recv(1024).decode()
                if message:
 
                    print ("<" + nicks_of_clients[addr[0]] + "> " + message)
 
                    # Calls broadcast function to send message to all
                    message_to_send = "<" + nicks_of_clients[addr[0]] + "> " + message
                    broadcast(message_to_send, conn)
 
                else:
                    remove(conn)
 
            except:
                continue
 
def broadcast(message, connection):
    for clients in list_of_clients:
        try:
            clients.send(message.encode())
        except:
            clients.close()
            remove(clients)
 
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
 
while True:
 
    conn, addr = server.accept()
 
    nicks_of_clients[addr[0]] = conn.recv(1024).decode()
    print("Connecttion from: " + nicks_of_clients[addr[0]])
    
    list_of_clients.append(conn)

 
    # prints the address of the user that just connected
    print (addr[0] + " connected")
 
    # creates and individual thread for every user
    # that connects
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()