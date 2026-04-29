class Cart:
    def __init__(self):
        self.items = []
    def add_item(self, name, price, quantity):
        if price < 0 or quantity <= 0:
            raise ValueError("Invalid price or quantity")
        self.items.append({
            "name":name,
            "price":price,
            "quantity":quantity
        })
    def get_total(self):
        return sum(item['price']* item['quantity'] for item in self.items)

    def apply_discount(self, discount):
        total = self.get_total()
        return total - (discount/100 * total)
