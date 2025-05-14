from product import Product 
from inventory import InventoryManager

coke = Product("Coke", "Bevarage", 5, 1.50, 10)
# print("Does", coke.name, "need restock?", coke.needs_restock())

sprite = Product("Sprite", "Bevarage", 6, 2.00, 10)
manager = InventoryManager()
manager.add_product(sprite)
# print(manager.products)
print(sprite)