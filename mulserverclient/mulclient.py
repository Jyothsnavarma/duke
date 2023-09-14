import socket
import threading
import json
import os

# Create a list to store server sockets
server_sockets = []

# Function to handle receiving messages from the server
def receive_messages(server_socket, buffer_size):
    while True:
        try:
            server_message = server_socket.recv(buffer_size).decode()
            if not server_message:
                break
            print(server_message)  # Moved the print statement here

        except Exception as e:
            print(f"Error: {e}")
            break

# Function to send a message to multiple servers
def broadcast_message(message):
    for socket in server_sockets:
        try:
            socket.send(message.encode())
        except Exception as e:
            print(f"Error sending message: {str(e)}")

# Function to connect to a server, start a receive thread, and return the socket
def connect_to_server(host, port, buffer_size):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Start a thread to receive messages from the server
        server_thread = threading.Thread(target=receive_messages, args=(server_socket, buffer_size))
        server_thread.start()

        server_sockets.append(server_socket)

        return server_socket

    except Exception as e:
        print(f"Error connecting to server {host}:{port}: {str(e)}")
        return None

def load_config():
    with open('mulconfig.json', 'r') as config_file:
        config = json.load(config_file)

        host1, host2 = config['server1_ip'], config['server2_ip']
        port1, port2 = config['server1_port'], config['server2_port']
        buffer_size = config['bytes']
        return host1, port1, host2, port2, buffer_size

def main():
    host1, port1, host2, port2, buffer_size = load_config()

    # Connect to Server 1
    server1_socket = connect_to_server(host1, port1, buffer_size)

    # Connect to Server 2
    server2_socket = connect_to_server(host2, port2, buffer_size)  # Added buffer_size

    try:
        while True:
            message = input("\nclient: ")

            # Send the message to all server sockets in the list
            broadcast_message(message)

            if message.lower() == "exit":
                os._exit(0)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
