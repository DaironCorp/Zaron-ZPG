import socket

class Server:
    timeout = 5
    address = '127.0.0.1'
    port = 1234
    players = 2
    coding = 'utf-8'

    def __init__(self):
        #Установление соединения
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(timeout)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((address, port))
        self.socket.listen(players)

    def accept(self):
        #Установление связи с клиентом
        return self.socket.accept()

    def send(self, conn, msg):
        #Отправка сообщения клиенту
        conn.send(msg.encode(coding))

    def recv(self, conn, size = 1024):
        #Получение сообщения от клиента
        return conn.recv(size).decode(coding)