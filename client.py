import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    nickname = input("Enter your nickname:")

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server



    message = nickname  # take input
    client_socket.send(message.encode())
    print(client_socket.recv(1024).decode())
    while message.lower().strip() != 'bye':
        message = input("Enter message:")
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print(data)
        

    client_socket.close() 

if __name__ == '__main__':
    client_program()
