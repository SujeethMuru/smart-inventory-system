class Product:
    def __init__(self, name, category, current_quantity, unit_price, restock_threshold):
        self.name = name
        self.category = category
        self.current_quantity = current_quantity
        self.unit_price = unit_price
        self.restock_threshold = restock_threshold

    def needs_restock(self):
        return self.current_quantity <= self.restock_threshold