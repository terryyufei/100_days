class Item:
    pay_rate = 0.8 # class attribute
    all = [] # we want to capture all the atrributes

    def __init__(self, name, price, quantity=0):
        """these are instance atrributes"""
        self.name = name
        self.price = price
        self.quantity = quantity

        # adding attributes to the list
        Item.all.append(self)
    
    def cal_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        """override an instance"""
        self.price = self.price * self.pay_rate

    def __repr__(self):
        """Represent your  instances"""
        return f"Item('{self.name}', {self.price}, {self.quantity})"   
   

item1 = Item("phone", 100, 5)    
item2 = Item("laptop", 1000, 3)
item3 = Item("cable", 10, 5)
item4 = Item("mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

print(Item.all) # prints all the intsances
"""
for instance in Item.all:
    print(instance.name) # prints names of all instances
"""
