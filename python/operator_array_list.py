for num in range(1, 11):
    print(num)
print("\n------------------------------")

numbers = list(range(1,10))
print(numbers)
print("\n------------------------------")

numbers2 = []
for num in range(1, 10):
    numbers2.append(num * 2)
print(numbers2)
print("\n------------------------------")

numbers3 = list(range(1, 20, 2))
print(numbers3)
print("\n------------------------------")

numbers4 = [num **2 for num in range(1, 10)]
print(numbers4)
print(min(numbers4))
print(max(numbers4))
print(sum(numbers4))
print("\n------------------------------")

print(numbers)
print(numbers[1:3])
print(numbers[:3])
print(numbers[3:])
print(numbers[-3:])
print(numbers[:])
