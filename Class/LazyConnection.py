# -*-coding:utf-8-*-

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, tb):
        self.sock.close()
        self.sock = None


if __name__ == '__main__':
    from functools import partial
    conn = LazyConnection('www.python.org', 80)
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'HOST: www.python.org\r\n')
        s.send(b'\r\n')
        resp = ''.join(iter(partial(s.recv, 8192),''))

