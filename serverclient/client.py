import socket
import json
with open("config.json", 'r') as config_file:
    config = json.load(config_file)
port = config["port"]
ip= config ["ip"]
client = socket.socket()
client.connect((ip, port))
while True:
        message = input(" client message: ")
        client.send(message.encode())
        data = client.recv(config["buffer_size"]).decode() # receive response
        print('Received from server: ' + data)  # show in terminal
        if data == 'bye':
            print(" server connection closed")
            break
client.close()
