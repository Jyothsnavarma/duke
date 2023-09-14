import socket
import threading
import json

# Function to handle receiving messages from the client
def receive_messages(client_socket, buffer_size):
    while True:
        try:
            client_message = client_socket.recv(buffer_size).decode()
            if client_message == "exit":
                exit(0)
            print(f"client: {client_message}")
        except Exception as e:
            # Handle any exceptions here (e.g., client disconnects)
            print(f"Error: {e}")
            exit(0)

# Server Configuration
def load_config():
    with open("mulconfig.json") as config_file:
        config = json.load(config_file)
        host = config['server2_ip']
        port = config['server2_port']
        buffer_size = config['bytes']
        return host, port, buffer_size

def start_server(host, port, buffer_size):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket, buffer_size))
    receive_thread.start()

    while True:
        try:
            server_message = input(" ")
            client_socket.send(f"Server 2: {server_message}".encode())
            if server_message.lower() == "exit":
                exit(0)
        except Exception as e:
            print(f"Error: {e}")
            exit(0)

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    host, port, buffer_size = load_config()
    start_server(host, port, buffer_size)

