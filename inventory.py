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
        #Look up product by name
        product = self.get_product(name)

        #Handle case where product doesn't exist
        if product is None:
            return False
        
        #calculate future stock after exchange
        new_quanitity = product.current_quantity + quantity_change
        #protect against going negative
        if new_quanitity < 0:
            return False
        
        #Safely update the stock
        product.current_quantity = new_quanitity
        return True #confirm success

    def list_low_stock(self):
        # returns list of stock that is lower than  or equal to minimum threshold
        restock_list = []
        for product in self.products.values():
            if product.needs_restock():
                restock_list.append(product)

        return restock_list

