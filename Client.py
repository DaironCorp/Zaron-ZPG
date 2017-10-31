import socket

class Client:
    address = '127.0.0.1'
    port = 1234
    coding = 'utf-8'

    def __init__(self):
        #Установление соединения
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((address, port))
        self.main()

    def send(self, msg):
        #Отправка сообщения на сервер
        self.s.send(msg.encode(coding))

    def recv(self, size = 1024):
        #Получение сообщения от сервера
        return self.s.recv(size).decode(coding)

    def authorization(self):
        self.send(input(self.recv())) #'Введите логин и пароль (Через пробел): '
        msg = self.recv()
        if msg == 'Авторизация прошла успешно': #'Авторизация прошла успешно'
            print(msg)
            return True
        else: #'Ошибка авторизации, повторить попытку? (y/n): '
            msg = input(msg)
            self.send(msg)
            if msg == y:
                authorization()
            else:
                return False

    def main(self):
        if input('Авторизоваться? (y/n): ').lower() == 'y':
            authorization()

player = Client()