from flask import Flask, render_template, request, redirect
from inventory import InventoryManager
from product import Product

app = Flask(__name__)

# Sample inventory setup
manager = InventoryManager()
manager.add_product(Product("Sprite", "Beverage", 6, 1.50, 5))
manager.add_product(Product("Coke", "Beverage", 4, 2.00, 5))
manager.add_product(Product("Fanta", "Beverage", 3, 1.75, 5))

@app.route("/")
def inventory_page():
    query = request.args.get("search", "") # Read 'search' from URL
    if query:
        filtered = manager.search_by_name(query)
    else:
        filtered = manager.products.values()

    products = [p.to_dict() for p in filtered]
    return render_template("inventory.html", products=products, search = query)

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        # 1. Get form data from the request
        name = request.form.get("name")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        threshold = request.form.get("threshold")

        print(f"Received: {name}, {category}, {quantity}, {price}, {threshold}")

        # 2. Basic validation: make sure all fields are filled
        if all([name, category, quantity, price, threshold]):
            # 3. Convert numeric fields to correct types
            quantity = int(quantity)
            price = float(price)
            threshold = int(threshold)

            # 4. Create a new product and add it
            new_product = Product(name, category, quantity, price, threshold)
            manager.add_product(new_product)
    
        # 5. Redirect to homepage (whether valid or not for now)
        return redirect("/") 
    
    # If GET, just show the form
    return render_template("add_product.html")

@app.route("/delete/<name>")
def delete_product(name):
    #Check if the product exists in the inventory
    if name in manager.products:
        removed = manager.remove_product(name)
        print(f"Deleted: {removed}")
    else:
        print(f"Delete failed: {name} not found")
    
    return redirect("/")

@app.route("/edit/<name>", methods=["GET", "POST"])
def edit_product(name):
    product = manager.get_product(name)

    if not product:
        print(f"Edit failed: {name} not found")
        return redirect("/")
    
    if request.method == "POST":
        # Get updated values from the form
        new_name = request.form.get("name")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        threshold = request.form.get("threshold")

        # Validate and update
        if all([new_name, category, quantity, price, threshold]):
            product.name = new_name
            product.category = category
            product.current_quantity = int(quantity)
            product.unit_price = float(price)
            product.restock_threshold = int(threshold)

            # If name changed, update the dictionary key
            if new_name != name:
                manager.products[new_name] = product
                del manager.products[name]

        return redirect("/")
    
    # If GET, show the edit form with current product info
    return render_template("edit_product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
    