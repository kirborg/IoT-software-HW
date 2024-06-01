import socket

# Задаем адрес сервера
SERVER_ADDRESS = ('localhost', 9090)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')
connection, address = server_socket.accept()

# Слушаем запросы
while True:
    print(f"new connection from {address}")

    data = connection.recv(1024)
    if not data:
        break
    print(str(data))
    connection.send(bytes('Hello from server!', encoding='UTF-8'))

connection.close()