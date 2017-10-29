import socket

class Client:
    address = '127.0.0.1'
    port = 1234
    coding = 'utf-8'

    def __init__(self):
        #Установление соединения
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((address, port))

    def send(self, msg):
        #Отправка сообщения на сервер
        self.s.send(msg.encode(coding))

    def recv(self, size = 1024):
        #Получение сообщения от сервера
        return self.s.recv(size).decode(coding)
