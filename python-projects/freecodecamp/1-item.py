class Item:
    def cal_total_price(self, x, y):
        return x * y

item1 = Item()    
item1.name = "phone"
item1.price = 100
item1.quantity = 5
print(item1.cal_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "laptop"
item2.price = 1000
item2.quantity = 3
print(item2.cal_total_price(item2.price, item2.quantity))

