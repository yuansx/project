filename = 'operator_array_list.py'
with open(filename) as fileObj:
    words = fileObj.read().split()
    print('count: ' + str(len(words)))
    print('words: ' + str(len(set(words))))
    print('count of print: ' + str(words.count('num')))
