# pytalk
This is a console based chat room app in python that can hold multiple rooms and multiple users. This application was made using threads and socket programming in pure python.

# Set up
1. Copy this link: https://github.com/DejunJackson/pytalk.git or go to the main page of the Github Repo and select the green "Code" button.
2. Open a terminal emulator on your desktop, Mac the application “Terminal” should be installed by default. Windows users will have “Windows PowerShell” or “Command Prompt”.
3. Change directory to the place you'd like the file to be stored, eg. cd -file path
4. In the desired location type "git clone" and paste the link from step 1.
5. Go to client.py and server.py and change HOST and PORT to your private IP address for HOST and desired port number for post.
    - `HOST = '192.168.0.96'` ***Must Change***
    - `PORT = 8000` *Optional Change*
6. Open atleast 2 or more terminals
7. In each terminal, cd or navigate into the folder that has the client and server files.
8. In one terminal type `python server.py` ***It is important that you do this before the next step as this starts the server***
9. In the other terminals type `python client.py`


# Features
```
$ python client.py

Welcome to pytalk. What is your nickname?


Hi DJ, type '<options>' to view what you can do.



Your options are below.


Enter: '<rooms>' to show a list of rooms
Enter: '<create> room_name' to create a room and assign it a name.
Enter: '<join> room_name' to join an existing chat room.


Enter: '<users>' to list the users' names in your current room.


Enter: '<leave>' to leave your current room.
```

- Upon start up you are asked to enter your nickname.
- Typing '<options>' grants you access to all of the powers you have.
- In this application, you can:
    - Create a room with a name
    - See other rooms that were created by you or other users and how many users are in them
    - Join rooms and talk to other users in the room
    - See who else is in the room
    - Leave a room
  
# To-do
1. Add an option to change username
2. Add admin powers to the owner:
    - Delete the room
    - Kick users from a room
    - Ban users from a room
3. Fix spacing of messages in console
4. Add a better UI (Tkinter?)
    

# Resources 

