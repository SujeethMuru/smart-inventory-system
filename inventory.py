class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        # Store product in the dictionary using its name as the key
        self.products[product.name] = product

    def remove_product(self, name):
        return self.products.pop(name, None)

    def get_product(self, name):
        return self.products.get(name, None)

        # if name in self.products:
        #     return self.products[name]
        # else:
        #     return  None

    def update_stock(self, name, quantity_change):
        pass

    def list_low_stock(self):
        restock_list = []
        for product in self.products.values():
            if product.needs_restock():
                restock_list.append(product)

        return restock_list

