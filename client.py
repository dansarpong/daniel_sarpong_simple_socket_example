"""
Creates a client socket, connects to the server, and sends messages
entered by the user. It receives and prints responses from the server until the
server sends a "closed" message.
"""

import socket

# Define the host server, port and buffer size
SERVER_HOST = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 1024


def run_client():
    """
    Run a client that sends messages to a server.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER_HOST, PORT))

        while True:
            msg = input("Enter message to send to server (type 'close' to quit): ")
            if msg.lower() == 'close':
                break
            client.sendall(msg.encode("utf-8"))

            response = client.recv(BUFFER_SIZE).decode("utf-8")
            if response.lower() == "closed":
                break

            print(f"Received: {response}")

    print("Connection to server closed")

# Run the client
if __name__ == "__main__":
    run_client()
