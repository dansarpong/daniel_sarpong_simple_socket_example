# Simple Socket App

This project demonstrates a basic socket communication setup using Python, featuring a client and a server.

## Features

- **Server**:
  - Listens for incoming client connections.
  - Accepts messages from the client and sends an acknowledgment.
  - Gracefully closes the connection when the client sends a "close" message.

- **Client**:
  - Connects to the server.
  - Sends user-input messages to the server.
  - Displays server responses and terminates upon receiving a "closed" message.

## Requirements

- Python 3.x

## How to Use

1. **Run the Server**:
   - Start the server using:
     ```bash
     python server.py
     ```
   - The server will begin listening on `127.0.0.1:8000`.

2. **Run the Client**:
   - Start the client in a separate terminal using:
     ```bash
     python client.py
     ```
   - Enter messages to send to the server. Type `close` to terminate the connection.
