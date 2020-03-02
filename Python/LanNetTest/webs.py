# -*- coding:utf-8 -*-

import socket
import time
import sys

HOST = '127.0.0.1'
PORT = 1234

def ser():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    '''
    socket.AF_INET表示创建一个IP套接字；socket.SOCK_STREAM 表示流式socket , for TCP
    sock_DGRAM表示数据报式socket , for UDP
    '''
    server.bind((HOST, PORT))
    server.listen(1)

    conn, addr = server.accept()
    print(addr)

    with conn:
        print('Connected by %s:%s' % addr)
        while True:
            data = conn.recv(8192*8)
            if not data:
                break
            #print('ok')
            #conn.send("ok".encode('utf-8'))
        print('Disconnected %s:%s' % addr)

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        ser()
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        ser()
