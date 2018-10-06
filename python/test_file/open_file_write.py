filename = 'username.txt'
with open(filename, 'w') as fileObj:
    fileObj.write('derekyuan\n')

with open(filename, 'a') as fileObj:
    fileObj.write('Jennie\n')

fileObj = open(filename, 'r')
print(fileObj.read().rstrip())
fileObj.close()
