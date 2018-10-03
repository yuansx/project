def add2int(n1, n2):
    return n1 + n2

def getNum():
    while True:
        try:
            num = input('input a num: ')
            num = int(num)
        except TypeError:
            print(num + ' is not a int num')
            continue
        except:
            print(num + ' is not a int num')
            continue
        else:
            return num

num1 = getNum()
num2 = getNum()
print(str(num1) + " + " + str(num2) + " = " + str(add2int(num1, num2)))
