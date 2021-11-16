# pytalk
This is a console based chat room app in python that can hold multiple rooms and multiple users. This application was made using threads and socket programming in pure python.

# Table of Contents

- [Set up](#set-up)
- [Features](#features)
- [To do](#to-do)
- [Resources](#resources)
- [License](#license)

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
- The options menu grants you access to all of the powers you have.
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
Here I list the resources I used to help make this app.
  
1. For threads and socket programming with python, here is a repo I made: https://github.com/DejunJackson/Python-Socket-Programming 


# License

MIT License

Copyright (c) 2021 Dejun Jackson

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
