import socket
import threading

# Data structures to store information about published files and clients
published_files = {}
clients = {}

# Server Configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# Function to handle client requests
def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        parts = data.split()
        if parts[0] == "PUBLISH":
            handle_publish_file(client_socket, parts[1], parts[2])
        elif parts[0] == "FETCHCLIENT":
            handle_fetch_file_location(client_socket, parts[1])
        elif parts[0] == "INFORM":
            handle_inform_fetched_file(client_socket, parts[1], parts[2])
        else:
            print("Invalid command")

# Function to publish a file to the server
def handle_publish_file(client_socket, client_id, file_name):
    # Store file information in the published_files data structure
    if file_name in published_files:
        # If the file is already in the dictionary, append the client_id to the existing list
        published_files[file_name].append(client_id)
    else:
        # If the file is not in the dictionary, create a new list with the client_id
        published_files[file_name] = [client_id]
    response = "File published successfully"
    client_socket.send(response.encode())

# Function to fetch target clients that have a file
def handle_fetch_file_location(client_socket, file_name):
    target_clients = published_files.get(file_name, [])
    response = " ".join(target_clients)
    if(not response): response = "none"
    client_socket.send(response.encode())

# Function to fetch a file from a target client

# Function to inform the server about a fetched file
def handle_inform_fetched_file(client_socket, client_id, file_name):
    # You can update data structures or perform any necessary actions
    published_files[file_name].append(client_id)
    response = "File information updated"
    client_socket.send(response.encode())

# Function to discover file names of a client
def discover_file_names(client_id):
    client_files = []
    for file, clients in published_files.items():
        for client in clients:
            if client == client_id: client_files.append(file)
    response = " ".join(client_files)
    print(response)

# Function to ping a host
def ping_host(client_id):
    ip_address, port = client_id.split(':')
    port = int(port)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, port))
    request = "PING " + client_id
    client_socket.send(request.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def handle_command():
    while True:
        command = input("Enter a command for the server (ping, discover): ").strip().split()
        if not command: continue
        elif command[0] == "ping":
            try:
                ping_host(command[1])
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif command[0] == "discover":
            try:
                discover_file_names(command[1])
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid command")

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(5)
print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")
command_handler = threading.Thread(target=handle_command)
command_handler.start()

while True:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
