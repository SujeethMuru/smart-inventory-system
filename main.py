from product import Product 
from inventory import InventoryManager

#create inventory manager object
manager = InventoryManager()
manager.add_product(Product("Coke", "Bevarage", 2, 1.50, 5))
manager.add_product(Product("Water", "Beverage", 10, 1.00, 5))
manager.add_product(Product("Juice", "Beverage", 3, 2.00, 4))


print("Low stock items:")
for product in manager.list_low_stock():
    print(product)

