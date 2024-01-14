import socket

HOST = "127.0.0.1"
PORT = 8888

while True:
    try:
        connection = socket.create_connection((HOST, int(PORT)))
        message = input("Enter a message to send: ")
        if message == "exit":
            connection.close()
            break
        connection.sendall(message.encode())
        data = connection.recv(1024).decode()
        print(f"Server response: {data}")
        connection.close()
    except Exception as e:
        print(e)
        break
