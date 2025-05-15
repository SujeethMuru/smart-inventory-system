import sqlite3

DB_NAME = "products.db" # SQLite database file

# Opens connection to the database file
def get_connection():
    return sqlite3.connect(DB_NAME)

# Sets up table if not already created
def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                name TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                threshold INTEGER NOT NULL
            )
        """)
        conn.commit()

def add_product_to_db(product):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO products (name, category, quantity, price, threshold)
            VALUES (?, ?, ?, ?, ?)
        """, (product.name, product.category, product.current_quantity, product.unit_price, product.restock_threshold))
        conn.commit()


def get_all_products_from_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, category, quantity, price, threshold FROM products")
        rows = cursor.fetchall()
        return [
            {
                "name": row[0],
                "category": row[1],
                "quantity": row[2],
                "price": row[3],
                "threshold": row[4]
            }
            for row in rows
        ]


def get_product_from_db(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, category, quantity, price, threshold FROM products WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return {
                "name": row[0],
                "category": row[1],
                "quantity": row[2],
                "price": row[3],
                "threshold": row[4]
            }
        return None


def delete_product_from_db(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE name = ?", (name,))
        conn.commit()


def update_product_in_db(name, product):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE products
            SET name = ?, category = ?, quantity = ?, price = ?, threshold = ?
            WHERE name = ?
        """, (product.name, product.category, product.current_quantity, product.unit_price, product.restock_threshold, name))
        conn.commit()
