"""This thread handles the server side (listening, and accepting new connections)"""

import socket
import threading
import sys
from rooms import Room, User
from options import show_options

HOST = '192.168.0.96'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = {}
rooms = {}

# listens for messages from inducted socket connection


def handle(user):
    while True:
        try:
            while True:
                received_msg = user.sock.recv(1024).decode('utf-8')

                # shows option screen if user types '<options>'
                if received_msg == '<options>':
                    for option in show_options('None'):
                        user.sock.send(
                            f"\n\n{option}".encode('utf-8'))
                    user.sock.send(
                        "\n\nPlease send a choice.".encode('utf-8'))
                    choice = user.sock.recv(1024).decode('utf-8')
                    selected_option = show_options(choice)
                    if choice == '<rooms>':
                        if len(rooms) == 0:
                            user.sock.send(
                                "No rooms available to list.".encode('utf-8'))
                        else:
                            for room_name in rooms.keys():
                                user.sock.send(
                                    room_name.encode('utf-8'))
                    elif '<create>' in choice:
                        room = Room(selected_option)
                        rooms[selected_option] = room
                    elif '<join>' in choice:
                        room_name = choice.split()[1]
                        rooms[room_name].join_room(
                            user.name, user.sock)
                        user.current_room_name = room_name
                        user.current_room = rooms[room_name]
                        user.sock.send(
                            f"You have now joined {room_name}.".encode('utf-8'))
                        user.current_room.broadcast(
                            f"<{user.name}> has joined the room")
                    elif choice == '<users>':
                        if user.current_room == 'None':
                            user.sock.send(
                                "Can't list rooms because you haven't joined one.".encode('utf-8'))
                        else:
                            users = user.current_room.show_users()
                            for name, soc in users.items():
                                user.sock.send(name.encode('utf-8'))
                    continue
                sent_msg = f"<{user.name}> {received_msg}"
                print(sent_msg)
                sys.stdout.flush()
                if user.current_room == 'None':
                    user.sock.send(
                        "Until you join a room, you will continue screaming into the void.".encode('utf-8'))
                else:
                    user.current_room.broadcast(sent_msg)
                sys.stdout.flush()
        except Exception as e:
            print(f"At handling: {e}")
            sys.stdout.flush()

        finally:
            user.sock.close()
            break

# Handles recieving and inducting a new socket connection


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
            new_user = User(nickname, communication_socket, 'None', 'None')
            clients[nickname] = new_user
            communication_socket.send(
                f"Hi {nickname}, type '<options>' to view what you can do.".encode('utf-8'))

            # After add socket connection to list, starts listening for messages
            # on a separate thread so receive() can continue running
            handle_thread = threading.Thread(
                target=handle, args=(new_user,))
            handle_thread.start()
        except Exception as e:
            print(f"At receiving: {e}")


print("Server running...")
sys.stdout.flush()
receive()
