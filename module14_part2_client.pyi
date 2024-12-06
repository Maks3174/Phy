import socket

def main():
    server_host = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"З'єднання з сервером {server_host}:{server_port} встановлено")

    while True:
        message = input("Введіть повідомлення: ")
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print("Отримано відповідь від сервера:", response)

    client_socket.close()

if __name__ == "__main__":
    main()
