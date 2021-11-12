import socket
import threading
import sys

HOST = '192.168.0.96'
PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:

                print('\033[K')
                print(message)
                sys.stdout.flush()

        except Exception as e:
            print(e)
            sock.close()
            break


def write():
    while True:
        try:
            msg = input("")
            print('\033[1A \033[K')
            sys.stdout.flush()
            sock.send(msg.encode('utf-8'))

        except Exception as e:
            print(e)
            sys.stdout.flush()
            sock.close()
            break


write_thread = threading.Thread(target=write)

write_thread.start()
receive()
