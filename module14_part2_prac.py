import socket
import threading
#1
def handle_client(client_socket, client_addr):
    print(f"З'єднання з клієнтом {client_addr} встановлено.")

    while True:
        message = client_socket.recv(1024).decode('utf-8')

        if not message:
            print(f"З'єднання з клієнтом {client_addr} завершено.")
            break

        print(f"Клієнт {client_addr}: {message}")

        response = input("Введіть вашу відповідь: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущено на {host}:{port}")

    while True:
        client_socket, client_addr = server_socket.accept()

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
        client_thread.start()

if __name__ == "__main__":
    main()


