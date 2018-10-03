class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("restaurant_name: " + self.restaurant_name + ", cuisine_type: " + self.cuisine_type)
    def open_restaurant(self):
        print("restaurant_name " + self.restaurant_name + " is openning")

restaurant = Restaurant("derek", "yue")
restaurant.describe_restaurant()
restaurant.open_restaurant()

