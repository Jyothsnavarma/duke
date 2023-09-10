import socket
import json
with open("config.json", 'r') as config_file:
    config = json.load(config_file)

port = config["port"]
ip = config["ip"]
server_socket = socket.socket()
server_socket.bind((ip, port))
server_socket.listen(9)
conn, address = server_socket.accept()
print("Connection from: " + str(address))
while True:

        data = conn.recv(config["buffer_size"])
        if not data:
            # if data is not received break
            break
        print("from connected client: " + str(data))
        data = input(' server Message:  ')
        conn.send(data.encode())  # send data to the client
conn.close()  # close the connection
~                      
