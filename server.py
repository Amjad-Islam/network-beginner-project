import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Client connected from {client_address}")

    data = client_socket.recv(1024)
    message = data.decode("utf-8")
    print(f"Received: {message}")

    client_socket.sendall(f"Echo: {message}".encode("utf-8"))
    client_socket.close()
