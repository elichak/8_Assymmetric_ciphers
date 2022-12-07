import socket
import pickle

def cypher(s, K):
    cyphered_string = [chr(ord(s[i]) ^ K) for i in range(len(s))]
    return ''.join(cyphered_string)

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

msg = conn.recv(1024)
p, g, A = pickle.loads(msg)
b = 4
B = g**b % p
conn.send(pickle.dumps(B))
K = A**b % p
print(K)
msg1 = cypher(pickle.loads(conn.recv(1024)), K)
print(msg1)

conn.send(pickle.dumps(cypher('О, Дивный новый мир!', K)))
conn.close()
