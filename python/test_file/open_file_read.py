filename = 'helloworld.py'

print('-------------------------')
with open(filename) as fileObj:
    print(fileObj.read().rstrip())
print('-------------------------')

with open(filename) as fileObj:
    for line in fileObj:
        print(line.rstrip())
print('-------------------------')

with open(filename) as fileObj:
    lines = fileObj.readlines()
for line in lines:
    print(line.rstrip())

print('-------------------------')
fileObj = open(filename)
print(fileObj)
print(fileObj.read().rstrip())
fileObj.close()

