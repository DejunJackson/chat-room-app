

class Room:
    def __init__(self, name):
        self.name = name
        self.room = {}

    def show_users(self):
        for name, sock in self.room.items():
            print(name)
