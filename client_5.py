import socket
import pickle
def cypher(s, K):
    cyphered_string = [chr(ord(s[i]) ^ K) for i in range(len(s))]
    return ''.join(cyphered_string)

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 19, 25, 13
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
B = pickle.loads(sock.recv(1024))
K = B ** a % p
print(K)
msg = input('Введите сообщение\n')
sock.send(pickle.dumps(cypher(msg, K)))
result = pickle.loads(sock.recv(1024))
print(f"Ответ сервера: {cypher(result, K)}")
sock.close()