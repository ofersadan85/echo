import socket

HOST = "0.0.0.0"
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established!")
            data = client_socket.recv(1024)
            print(f"Message received from {client_address}:\n{data.decode()}")
            client_socket.sendall(data)
            client_socket.close()
        except Exception as e:
            print(e)
            break
