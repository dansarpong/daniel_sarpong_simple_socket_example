"""
Creates a server socket that listens for incoming connections
from a client. It receives messages from the client and sends an "accepted"
message back to the client. The server stops when the client sends a "close"
message.
"""

import socket

# Define the host server, port and buffer size
SERVER_HOST = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 1024


def run_server():
    """
    Run a server that listens for incoming messages from a client
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((SERVER_HOST, PORT))
        server.listen()
        print(f"Listening on {SERVER_HOST}:{PORT}")

        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        with client_socket:
            while True:
                request = client_socket.recv(BUFFER_SIZE)
                request = request.decode("utf-8")

                if not request or request.lower() == "close":
                    client_socket.sendall("closed".encode("utf-8"))
                    break

                print(f"Received: {request}")
                client_socket.sendall("accepted".encode("utf-8"))
    
    print("Connection to client closed")


# Run the server
if __name__ == "__main__":
    run_server()
