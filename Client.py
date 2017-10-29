import socket

class Connection:
    adress = '127.0.0.1'
    port = 1234
    coding = 'utf-8'

class Client:
    #Сетевая часть клиента.
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((Connection.adress, Connection.port))

    def send(self, msg):
        #Отправка сообщения на сервер
        self.s.send(msg.encode(Connection.coding))

    def recv(self, size = 1024):
        #Получение сообщения от сервера
        return self.s.recv(size).decode(Connection.coding)
