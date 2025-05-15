from product import Product 
from inventory import InventoryManager

#create inventory manager object
manager = InventoryManager()
manager.add_product(Product("Sprite", "Bevarage", 6, 1.50, 5))
manager.add_product(Product("Coke", "Bevarage", 7, 2.50, 5))
manager.add_product(Product("CocaCola", "Bevarage", 6, 1.50, 5))
manager.add_product(Product("Fanta", "Bevarage", 8, 3.50, 5))

results = manager.search_by_name("a")
if results:
    print("Matching products:")
    for product in results:
        print(product)
else:
    print("No matches found.")
