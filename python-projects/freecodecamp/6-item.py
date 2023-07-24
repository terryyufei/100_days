import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)  
        for item in items:
            Item(
                name=item.get('name'),
                price=item.get('price'),
                quantity=item.get('quantity'),
            )

Item.instantiate_from_csv()
print(Item.all)
   

