import socket
import os
import threading
#1
def main():
    server_host = '127.0.0.1'
    server_port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    print("[CLIENT] Connected to the server.")

    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print_board(data)

            move = input("Enter your move (0-8): ")
            client_socket.sendall(move.encode())

            game_status = client_socket.recv(1024).decode()
            if game_status == 'over':
                print("Game over. You win!" if 'X' in data else "Game over. You lose!")
                break
        except Exception as e:
            print(f"[ERROR] {e}")
            break

    client_socket.close()


def print_board(data):
    print("Board:")
    for i in range(3):
        print(' | '.join(data[i * 3:i * 3 + 3]))
        if i < 2:
            print("-" * 5)


if __name__ == "__main__":
    main()


#2
def send_file(server_socket, filename):
    filesize = os.path.getsize(filename)
    server_socket.sendall(filename.encode())
    server_socket.recv(1024)
    server_socket.sendall(str(filesize).encode())
    response = server_socket.recv(1024).decode()
    if response == "Ready to receive file.":
        with open(filename, 'rb') as file:
            server_socket.sendfile(file)


def main():
    server_host = '127.0.0.1'
    server_port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    print("[CLIENT] Connected to the server.")

    filename = input("Enter the filename to send: ")
    send_file(client_socket, filename)

    response = client_socket.recv(1024).decode()
    print("[CLIENT]", response)

    client_socket.close()


if __name__ == "__main__":
    main()


#3
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
        except:
            break


def main():
    server_host = '127.0.0.1'
    server_port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    print("[CLIENT] Connected to the server.")

    username = input("Enter your username: ")
    client_socket.send(username.encode())

    welcome_message = client_socket.recv(1024).decode()
    print(welcome_message)

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("")
        if message.lower() == "exit":
            break
        client_socket.send(message.encode())

    client_socket.close()


if __name__ == "__main__":
    main()
