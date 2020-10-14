import socket


BUFFER_SIZE = 32
MAX_CONN = 10


def create_server_socket(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socket_pair = (host, port)
    s.bind(socket_pair)

    return s


def read_all(conn_socket):

    res = b''

    while True:
        data = conn_socket.recv(BUFFER_SIZE)
        res += data

        if len(data) < BUFFER_SIZE:
            break


def on_accept(conn_socket):

    try:

        #data = conn_socket.recv(BUFFER_SIZE)
        data = read_all(conn_socket)

        print(data)
    
    except ConnectionResetError as e:
        print('Closing connection (due to connection being reset by peer)')
        conn.close()

    if data is None:
        print("Closing connection (due to peer's closing its socket)")
        conn.close()


if __name__ == '__main__':

    srv_socket = create_server_socket('0.0.0.0', 1234)

    srv_socket.listen(MAX_CONN)

    while True:

        try:
            
            conn_socket, addr = srv_socket.accept()

            print('Accepted connection from', addr)
            
            on_accept(conn_socket)

        except KeyboardInterrupt:
            print('\nStopping the server due to keyborard interrupt')
            break
