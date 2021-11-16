"""Handles the server side (listening, and accepting new connections)"""

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
                    for option in show_options():
                        user.sock.send(
                            f"{option}".encode('utf-8'))
                    continue
                # lists currently available rooms
                elif received_msg == '<rooms>':
                    if len(rooms) == 0:
                        user.sock.send(
                            "No rooms available to list.".encode('utf-8'))
                        user.sock.send(
                            "Create a room with '<create> room_name'.".encode('utf-8'))
                        continue
                    else:
                        user.sock.send(
                            f"Listing rooms...".encode('utf-8'))
                        for room_name, room in rooms.items():
                            user.sock.send(
                                f"\n{room_name}: {room.show_num_users()} users".encode('utf-8'))
                        continue
                # creates rooms
                elif '<create>' in received_msg:
                    room_name = received_msg.split()[1]
                    if room_name in rooms.keys():
                        user.sock.send(
                            "This name already exists. Try another room.".encode('utf-8'))
                        continue
                    room = Room(room_name)
                    rooms[room_name] = room
                    user.sock.send(
                        f"You created the room: {room_name}".encode('utf-8'))
                    continue
                # joins a currently available rooms
                elif '<join>' in received_msg:
                    room_name = received_msg.split()[1]
                    if room_name not in rooms.keys():
                        user.sock.send(
                            "Can't join a room that doesn't exist.".encode('utf-8'))
                        continue
                    rooms[room_name].join_room(
                        user.name, user.sock)
                    user.current_room_name = room_name
                    user.current_room = rooms[room_name]
                    user.sock.send(
                        f"You have now joined {room_name}.".encode('utf-8'))
                    user.current_room.broadcast(
                        f"<{user.name}> has joined the room")
                    continue
                # lists users in a room
                elif received_msg == '<users>':
                    if user.current_room == 'None':
                        user.sock.send(
                            "Can't list rooms because you haven't joined one.".encode('utf-8'))
                        continue
                    else:
                        users = user.current_room.show_users()
                        for name in users.keys():
                            user.sock.send(name.encode('utf-8'))
                        continue
                # leaves a room, if player is in one
                elif received_msg == '<leave>':
                    if user.current_room == 'None':
                        user.sock.send(
                            "Can't leave a room if you haven't joined one.".encode('utf-8'))
                        continue
                    else:
                        user.current_room.broadcast(
                            f"{user.name} left the chat room.")
                        user.current_room.leave_room(user.name, user.sock)
                        user.current_room_name = 'None'
                        user.current_room = 'None'
                        continue
                # packages message to be sent
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
                "Welcome to pytalk. What is your nickname?".encode('utf-8'))
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
