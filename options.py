

def show_options(choice):
    options = ["Enter: '<rooms>' to show a list of rooms",
               "Enter: <create> 'room_name' to create a room and assign it a name."]
    if choice == 'None':
        return options
    elif '<create>' in choice:
        room_name = choice.split()[1]
        return room_name
