import socket
from googletrans import Translator
import threading
import json
#1
def server():
    host = "127.0.0.1"
    port = 12345
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    print("Waiting for connection...")
    conn, addr = s.accept()
    print("Connected:", addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Client:", data)
        if data.lower() == 'exit':
            print("Exiting conversation...")
            break
        message = input("Server: ")
        conn.send(message.encode())

    conn.close()

if __name__ == "__main__":
    server()

#2
weather_data = {
    "Ukraine": {
        "Kyiv": {
            "Monday": "Sunny",
            "Tuesday": "Cloudy",
            "Wednesday": "Rainy",
            "Thursday": "Sunny",
            "Friday": "Rainy",
            "Saturday": "Cloudy",
            "Sunday": "Sunny"
        },
        "Lviv": {
            "Monday": "Rainy",
            "Tuesday": "Cloudy",
            "Wednesday": "Cloudy",
            "Thursday": "Sunny",
            "Friday": "Rainy",
            "Saturday": "Sunny",
            "Sunday": "Sunny"
        }
    },
    "USA": {
        "New York": {
            "Monday": "Sunny",
            "Tuesday": "Cloudy",
            "Wednesday": "Rainy",
            "Thursday": "Sunny",
            "Friday": "Rainy",
            "Saturday": "Cloudy",
            "Sunday": "Sunny"
        },
        "Los Angeles": {
            "Monday": "Cloudy",
            "Tuesday": "Sunny",
            "Wednesday": "Sunny",
            "Thursday": "Sunny",
            "Friday": "Sunny",
            "Saturday": "Sunny",
            "Sunday": "Sunny"
        }
    }
}


def handle_client(client_socket, country, city):
    if country in weather_data and city in weather_data[country]:
        client_socket.send(json.dumps(weather_data[country][city]).encode())
    else:
        client_socket.send(b"No weather data available for the specified country and city.")

    client_socket.close()


def server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Сервер запущено на {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Новий клієнт підключився: {addr[0]}:{addr[1]}")

        data = client_socket.recv(1024).decode()
        country, city = data.split(',')

        client_thread = threading.Thread(target=handle_client, args=(client_socket, country.strip(), city.strip()))
        client_thread.start()


if __name__ == "__main__":
    server()

#3
def server():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))

        s.listen()

        print("Сервер запущено...")
        while True:
            conn, addr = s.accept()
            with conn:
                print('Підключено до', addr)
                data = conn.recv(1024).decode()
                print("Отримано:", data)
                translator = Translator()
                translation = translator.translate(data, dest='uk').text
                conn.sendall(translation.encode())

if __name__ == "__main__":
    server()

