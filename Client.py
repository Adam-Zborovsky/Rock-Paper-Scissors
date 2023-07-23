import socket

def connect():
    global sock
    sock = socket.socket()
    sock.connect(('192.168.1.120', 7648))

def send(msg):
    sock.send(msg.encode())

def receive():
    msg = sock.recv(8).decode().lstrip('0')
    sock.close()
    return msg