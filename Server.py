import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.1.120', 7648))
clients = []


def receive():
    msg0 = clients[0].recv(8)
    msg1 = clients[1].recv(8)
    clients[1].send(msg0)
    clients[0].send(msg1)


def main():
    while True:
        ss.listen()
        print("running")
        print()
        (client_socket, address) = ss.accept()
        clients.append(client_socket)
        print("Connected" + str(address))

        if len(clients) == 2:
            receive()
            clients.clear()


if __name__ == "__main__":
    main()