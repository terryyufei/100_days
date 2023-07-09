class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def cal_total_price(self):
        return self.price * self.quantity

item1 = Item("phone", 100, 5)    
print(item1.cal_total_price())

item2 = Item("laptop", 1000, 3)
print(item2.cal_total_price())


