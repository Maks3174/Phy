import socket
import threading
import os
#1
players = []
board = [' ' for _ in range(9)]
current_player = None
game_over = False


def handle_client(client_socket, player):
    global current_player, game_over

    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            handle_move(data, player)

            for p in players:
                p[0].sendall(board_to_str().encode())

            if check_winner() or check_draw():
                game_over = True
                break
        except Exception as e:
            print(f"[ERROR] {e}")
            break

    players.remove(player)
    client_socket.close()


def handle_move(data, player):
    global current_player
    move = int(data)
    if current_player == player and 0 <= move <= 8 and board[move] == ' ':
        board[move] = 'X' if player[1] == 1 else 'O'
        current_player = players[0] if player == players[1] else players[1]


def check_winner():
    global game_over
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            game_over = True
            return True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            game_over = True
            return True
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        game_over = True
        return True
    return False


def check_draw():
    global game_over
    if ' ' not in board:
        game_over = True
        return True
    return False


def board_to_str():
    return ''.join(board)


def main():
    global current_player

    server_host = '127.0.0.1'
    server_port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(2)

    print("[SERVER] Server is listening...")

    while len(players) < 2:
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Connection from {client_address} has been established.")

        players.append((client_socket, len(players)))
        client_socket.sendall(f"Player {len(players)} connected.".encode())

    current_player = players[0]

    for player in players:
        client_thread = threading.Thread(target=handle_client, args=(player[0], player))
        client_thread.start()


if __name__ == "__main__":
    main()


#2
def receive_file(client_socket, filename, filesize):
    received_bytes = 0
    with open(filename, 'wb') as file:
        while received_bytes < filesize:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
            received_bytes += len(data)
    return received_bytes == filesize


def main():
    server_host = '127.0.0.1'
    server_port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)

    print("[SERVER] Server is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Connection from {client_address} has been established.")

        filename = client_socket.recv(1024).decode()
        filesize = int(client_socket.recv(1024).decode())

        client_socket.sendall(b"Ready to receive file.")

        success = receive_file(client_socket, filename, filesize)
        if success:
            print(f"[SERVER] File '{filename}' received successfully.")
            client_socket.sendall(b"File received successfully.")
        else:
            print(f"[SERVER] Error receiving file '{filename}'.")
            client_socket.sendall(b"Error receiving file.")

        client_socket.close()


if __name__ == "__main__":
    main()


#3
clients = {}


def broadcast(message, sender_username):
    for client in clients:
        if client != sender_username:
            client.send(f"{sender_username}: {message}".encode())


def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"{username}: {message}")
                broadcast(message, username)
        except:
            print(f"{username} has left the chat.")
            client_socket.close()
            del clients[username]
            break


def main():
    server_host = '127.0.0.1'
    server_port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print("[SERVER] Server is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Connection from {client_address} has been established.")

        username = client_socket.recv(1024).decode()
        clients[username] = client_socket

        client_socket.send("Welcome to the chat!".encode())

        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()


if __name__ == "__main__":
    main()
