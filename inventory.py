class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        # Store product in the dictionary using its name as the key
        self.products[product.name] = product

    def remove_product(self, name):
        pass

    def get_product(self,name):
        pass

    def update_stock(self, name, quantity_change):
        pass

    def list_low_stock(self):
        pass