from product import Product 

coke = Product("Coke", "Bevarage", 5, 1.50, 10)
print("Does", coke.name, "need restock?", coke.needs_restock())