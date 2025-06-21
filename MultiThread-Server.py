from socket import *
import sys
import threading
import time

# Function to handle client requests in separate threads
def handle_client(connectionSocket, addr):
    try:
        start_time = time.time()  # Record the start time of request processing

        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        # Send HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
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

# Main function to listen for incoming connections
def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverPort = 6789
    serverSocket.bind(('127.0.0.1', serverPort))
    serverSocket.listen(5)
    print('The server is ready to receive')

    while True:
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()
        print('Connection received from:', addr)

        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()

    serverSocket.close()

if __name__ == "__main__":
    main()
