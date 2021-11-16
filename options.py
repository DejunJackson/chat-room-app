"""Shows options"""


def show_options():
    options = ["\nYour options are below.",
               "\nEnter: '<rooms>' to show a list of rooms",
               "\nEnter: '<create> room_name' to create a room and assign it a name.",
               "\nEnter: '<join> room_name' to join an existing chat room.",
               "\nEnter: '<users>' to list the users' names in your current room.",
               "\nEnter: '<leave>' to leave your current room."
               ]

    return options
