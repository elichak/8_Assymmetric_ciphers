import socket
from threading import Thread
import threading


SERVER = "127.0.0.1"
PORT = 1488

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
p = 52
g = 10
a = 57
A = g**a % p
client.sendall(bytes(f"DH: {g}, {p}, {A}", "UTF-8"))
B = int(client.recv(4096).decode())
print(B**a%p)
def task():
    while True:
        in_data = client.recv(4096).decode()
        print("From server: ", in_data)

def task2():
    while True:
        out_data = input()
        client.sendall(bytes(out_data, "UTF-8"))
        print("Send: " + str(out_data))

t1 = Thread(target = task2)
t2 = Thread(target = task)

t1.start()
t2.start()

t1.join()
t2.join()