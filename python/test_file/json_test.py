import json

filename = 'username.txt'
try:
    with open(filename) as fileObj:
        username = json.load(fileObj)
        print('your name is ' + username)
except FileNotFoundError:
    with open(filename, 'w') as fileObj:
        username = input('Please input your name: ')
        json.dump(username, fileObj)

