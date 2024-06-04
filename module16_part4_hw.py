#server
import socket
import threading
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen()

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Не вдалося надіслати повідомлення клієнту: {e}")

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                # Зберігання повідомлення у Redis
                r.rpush('chat_messages', message)
                print(f"Отримано повідомлення: {message.decode()}")
                broadcast(message, client_socket)
            else:
                client_socket.close()
                clients.remove(client_socket)
                break
        except Exception as e:
            print(f"Помилка при обробці клієнта: {e}")
            client_socket.close()
            clients.remove(client_socket)
            break

def main():
    print("Сервер запущений і чекає підключень...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Клієнт підключений: {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()


#client
import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Новий повідомлення: {message.decode()}")
            else:
                print("З'єднання з сервером втрачено.")
                break
        except Exception as e:
            print(f"Помилка при отриманні повідомлення: {e}")
            break

def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == "__main__":
    threading.Thread(target=receive_messages).start()
    send_message()
