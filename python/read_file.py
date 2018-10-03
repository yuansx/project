filenames = ['helloworld.py', 'helloworld.txt', 'guest.txt']
for filename in filenames:
    try:
        with open(filename) as fileObj:
            print(fileObj.read().rstrip())
    except FileNotFoundError:
        if filename == 'guest.txt':
            pass
        else:
            print('file ' + filename + " is not exist")
    except:
        print('uknow exception')

