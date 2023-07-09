class Item:
    pay_rate = 0.8 # class attribute

    def __init__(self, name, price, quantity=0):
        """these are instance atrributes"""
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def cal_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        """override an instance"""
        self.price = self.price * self.pay_rate

item1 = Item("phone", 100, 5)    
item1.apply_discount() #access from class level
print(item1.price)

item2 = Item("laptop", 1000, 3)
item2.pay_rate = 0.7 # access from instance level
item2.apply_discount()
print(item2.price)



"""
#shows class atrribute is accessible to instances
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__) # all attributes for class level
print(item1.__dict__) # all attributes at instance level

"""
