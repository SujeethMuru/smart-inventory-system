import os
from flask import Flask, render_template, request, redirect, session
from db import (
    create_table,
    add_product_to_db,
    get_all_products_from_db,
    delete_product_from_db,
    get_product_from_db,
    update_product_in_db
)
from product import Product


app = Flask(__name__)
app.secret_key = "super-secret-dev-key"
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

create_table()

# Sample inventory setup
#manager = InventoryManager()
#manager.add_product(Product("Sprite", "Beverage", 6, 1.50, 5))
#manager.add_product(Product("Coke", "Beverage", 4, 2.00, 5))
#manager.add_product(Product("Fanta", "Beverage", 3, 1.75, 5))

@app.route("/")
def inventory_page():
    query = request.args.get("search", "").lower()
    all_products = get_all_products_from_db()

    if query:
        filtered = [p for p in all_products if query in p["name"].lower()]
    else:
        filtered = all_products

    return render_template("inventory.html", products=filtered, search=query)

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect("/")
        else:
            return "❌ Incorrect password", 401
    
    return ''' 
        <h2>🔐 Admin Login</h2>
        <form method="post">
            <input type="password" name="password" placeholder="Enter admin password" required>
            <button type="submit">Login</button>
        </form>
    '''

@app.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    return redirect("/admin")

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if not session.get("admin_logged_in"):
        return redirect("/admin")
    
    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        threshold = request.form.get("threshold")

        if all([name, category, quantity, price, threshold]):
            quantity = int(quantity)
            price = float(price)
            threshold = int(threshold)

            new_product = Product(name, category, quantity, price, threshold)
            add_product_to_db(new_product)

        return redirect("/")

    return render_template("add_product.html")

@app.route("/delete/<name>")
def delete_product(name):
    if not session.get("admin_logged_in"):
        return redirect("/admin")
    
    delete_product_from_db(name)
    return redirect("/")

@app.route("/edit/<name>", methods=["GET", "POST"])
def edit_product(name):
    if not session.get("admin_logged_in"):
        return redirect("/admin")
    
    product_data = get_product_from_db(name)

    if not product_data:
        return redirect("/")

    if request.method == "POST":
        new_name = request.form.get("name")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        threshold = request.form.get("threshold")

        if all([new_name, category, quantity, price, threshold]):
            updated = Product(new_name, category, int(quantity), float(price), int(threshold))
            update_product_in_db(name, updated)

        return redirect("/")

    return render_template("edit_product.html", product=product_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
    