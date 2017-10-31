import socket

class Server:
    timeout = 5
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

    def authorization(self, conn):
        #Авторизация клиента, возвращает login или 'error'
        self.send(conn, 'Введите логин и пароль (Через пробел): ')
        login, password = self.recv(conn).split()
        with open('Passwords.txt', 'r') as f:
            for line in f:
                if login + ' ' + password == line:
                    return login
                    self.send(conn, 'Авторизация прошла успешно')
                    break
            else:
                self.send(conn, 'Ошибка авторизации, повторить попытку? (y/n): ')
                if self.recv(conn).lower() == 'y':
                    f.close()
                    self.authorization(conn)
                else:
                    return 'error'