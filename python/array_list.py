students = ['derek', 'leo', 'Tom']
for name in students:
    print(name)
print(students[-1])

students.append('jennie')
print(students)

students.insert(2, 'duang')
print(students)

del students[1]
print(students)

stu1 = students.pop()
print(students)
print(stu1)

stu1 = students.pop(0)
print(students)
print(stu1)

students.remove('Tom')
print(students)


students = ['derek', 'Jennie', 'leo', 'Tom', 'Jimmy']
print(students)
students.sort()
print(students)
students.sort(reverse=True)
print(students)

students = ['derek', 'Jennie', 'leo', 'Tom', 'Jimmy']
print(sorted(students))
print(students)

students.reverse()
print(students)
