import socket
import threading

LOCALHOST = "127.0.0.1"
PORT = 1488

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((LOCALHOST, PORT))
print('Server is available!')

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New User: ", clientAddress)

    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()
            print(msg)
            if msg == 'STOP':
                print('Disconnection...')
                break
            elif msg == 'Как дела?':
                self.csocket.send(bytes("Отлично!", "UTF-8"))
            elif msg[0:2] == 'DH':
                b = 12
                lst = list(map(int, msg[4:].split(',')))
                B = lst[0]**b % lst[1]
                K = lst[2]**b % lst[1]
                print(K)
                self.csocket.send(bytes(f"{B}", "UTF-8"))
            else:
                self.csocket.send(bytes("Умею отвечать только на как дела.", "UTF-8"))

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
