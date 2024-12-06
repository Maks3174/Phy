import socket
#1
def client():
    host = "127.0.0.1"
    port = 12345

    s = socket.socket()
    s.connect((host, port))

    while True:
        message = input("Client: ")
        s.send(message.encode())
        if message.lower() == 'exit':
            print("Exiting conversation...")
            break
        response = s.recv(1024).decode()
        print("Server:", response)
        if response.lower() == 'exit':
            print("Exiting conversation...")
            break

    s.close()

if __name__ == "__main__":
    client()

#2
import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))

    city = input("Введіть назву міста: ")

    client_socket.send(city.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()


if __name__ == "__main__":
    main()

#3
import socket

def client():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        text = input("Введіть рядок для перекладу: ")

        s.sendall(text.encode())

        translation = s.recv(1024).decode()
        print("Переклад:", translation)

if __name__ == "__main__":
    client()
