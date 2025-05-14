# Smart Inventory System

A comman-line-based inventory managaments system that models real-world stock tracking using core data strucutres and software engineering practices.


## 📁 Project Structure

- 'main.py': Entry point for the program. This is where user interacts with the system. (the remote control of the program)

- 'product.py': Contains the Product class, which represents individual inventory and includes attributes like name, category, price, quanitity, and restock threshold.

- 'inventory.py': Will manage the collectionof products- adding, removing, searching, and sorting- using data structures like dictionaires and heaps.

- '.gitingore': Keeps unecessary files out of version control (e.g. Python cache files, VS Code setting.)

- 'README.md': You're reading it Lol!. Describes the project and how it's structured.

- 'test/': Will contain unit tests for validating components Product class and Inventory Manager logic.

- 'data/': Will sotre saved inventory data in JSON or other formats later on.


## 🧠 Design Philosopy

The project is designed using **modular principles** and **separation of concerns**, just like a real software engineer would strucutre a scalable system:

- Each file/module has a **single responsibility**
- Logic is broken down into **reusable, testable components**
- Project is structured to **scale up** - from CLI to full stack if needed


## Structure:
| Question                          | Leads To       | Purpose               |
| --------------------------------- | -------------- | --------------------- |
| "What is the user running?"       | `main.py`      | Entry point logic     |
| "What object am I modeling?"      | `product.py`   | Object definition     |
| "What logic controls the system?" | `inventory.py` | Management/controller |
| "How do I prevent repo clutter?"  | `.gitignore`   | Clean version control |
| "How do I describe the project?"  | `README.md`    | Communicate clearly   |
| "How do I prove it works?"        | `tests/`       | Maintainability       |


## Inventory Manager:
| Responsibility                 | What it means in code                     |
| -------------------------------| ----------------------------------------- |
| 🧾 Store products              | A list or dictionary of `Product` objects |
| ➕ Add product                 | Insert a new product to the collection    |
| ➖ Remove product              | Delete a product by name or ID            |
| 🔍 Search product              | Find and view a product                   |
| 🪙 Update stock                | Increase or decrease quantity             |
| ⚠️ Restock alert               | Show all products below threshold         |
| 💾 (Later) Save/load inventory | Persist inventory to file                 |


## DSA Concepts for Invetory Manager:
| Task                    | Best Data Structure                  |
| ----------------------- | ------------------------------------ |
| Fast lookup by name     | `dict` (HashMap) ✅                  |
| Sorted product display  | `list` + sorting                     |
| Priority restocking     | `heap` (for advanced features later) |
| Storing product details | `Product` class (already done) ✅    |



