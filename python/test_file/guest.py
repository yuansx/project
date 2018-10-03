filename='guest.txt'
with open(filename, 'w') as guestObj:
    while True:
        name = input('Please write your name(q for quit): ')
        if name == 'q':
            break
        print('Hello ' + name.title())
        guestObj.write(name.title() + '\n')

