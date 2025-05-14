class Product:
    def __init__(self, name, category, current_quantity, unit_price, restock_threshold):
        self.name = name
        self.category = category
        self.current_quantity = current_quantity
        self.unit_price = unit_price
        self.restock_threshold = restock_threshold

    def __str__(self):
        # Return a nice string like: "Sprite (Bevarge): 6 in stock @ $2.00"
        return f"{self.name} ({self.category}): {self.current_quantity} in stock @ ${self.unit_price:.2f}"

    def needs_restock(self):
        return self.current_quantity <= self.restock_threshold