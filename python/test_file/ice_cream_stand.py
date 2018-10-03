import restaurant as res

class IceCreamStand(res.Restaurant):
    """ 注释 """
    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        self.flavors = flavors

    #def describe_ice_cream(self):
    #    self.describe_restaurant()
    def describe_restaurant(self):
        super().describe_restaurant()
        print("ice flavors is " + self.flavors)

ice_cream = IceCreamStand("derek", "yue", "milk")
#ice_cream.describe_ice_cream()
ice_cream.describe_restaurant()

