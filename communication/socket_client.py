import socket


def send_string(client_socket, message):

    data = message.encode()
    client_socket.sendall(data)


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    dest_pair = ('127.0.0.1', 1234)
    s.connect(dest_pair)

    send_string(s, 'hello')




