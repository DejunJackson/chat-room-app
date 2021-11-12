import socket
import threading
import sys


HOST = '192.168.0.96'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = {}


def broadcast(message):
    for client in clients:
        clients[client].send(message.encode('utf-8'))


def handle(communication_socket):
    while True:
        try:
            while True:
                received_msg = communication_socket.recv(1024).decode('utf-8')
                nickname = list(clients.keys())[
                    list(clients.values()).index(communication_socket)]
                sent_msg = f"<{nickname}> {received_msg}"
                print(sent_msg)
                sys.stdout.flush()
                broadcast(sent_msg)
                sys.stdout.flush()
        except Exception as e:
            print(f"At handling: {e}")
            sys.stdout.flush()

        finally:
            communication_socket.close()
            break


def receive():
    while True:
        try:
            communication_socket, address = server.accept()
            communication_socket.setblocking(1)
            print(f"Connected to {address}")
            sys.stdout.flush()
            communication_socket.send(
                "Welcome to the chat room. What is your nickname?".encode('utf-8'))
            nickname = communication_socket.recv(1024).decode('utf-8')
            broadcast(f"{nickname} joined the chatroom.")
            clients[nickname] = communication_socket
            communication_socket.send(
                f"Hi {nickname}, type a message and press enter to send!".encode('utf-8'))
            handle_thread = threading.Thread(
                target=handle, args=(communication_socket,))
            handle_thread.start()
        except Exception as e:
            print(f"At receiving: {e}")


print("Server running...")
sys.stdout.flush()
receive()
