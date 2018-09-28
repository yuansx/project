def make_sandwich(*foods):
    for food in foods:
        print("food: " + str(food))
    print("add " + str(foods) + " to sandwich")


def get_foods():
    foods = []
    while True:
        food = input("Please input food which you want to add to this sandwich: ")
        if food == "quit":
            break;
        foods.append(food)
    return foods

make_sandwich('apple', 'banana')
for idx in range(0, 3):
    foods = get_foods()
    make_sandwich(foods[:])


