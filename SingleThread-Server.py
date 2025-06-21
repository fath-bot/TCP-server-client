from socket import *
import sys
import time

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket 
serverPort = 5555
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)
print('The server is ready to receive')

while True:
    # Establish the connection
    print("Ready to serve...")
    
    # Accept the connection
    connectionSocket, addr = serverSocket.accept()
    print(f'Connection received from: {addr}')

    try:
        start_time = time.time()  # Record the start time of request processing
        
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

        end_time = time.time()  # Record the end time of request processing
        print(f"Request from {addr} processed in {end_time - start_time:.5f} seconds.")

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        
        # Close client socket
        connectionSocket.close()

        end_time = time.time()  # Record the end time of request processing
        print(f"Request from {addr} failed: File not found. Processed in {end_time - start_time:.5f} seconds.")

serverSocket.close()
sys.exit()
