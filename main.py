import sqlite3

def create_db_connection():
    create_connection = sqlite3.connect('inventory_mgmt.db')
    create_cursor = create_connection.cursor()
    create_cursor.execute('CREATE TABLE IF NOT EXISTS products ('
                          'product_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                          'name TEXT NOT NULL,'
                          'price REAL NOT NULL,'
                          'quantity INTEGER)')
    create_connection.commit()

create_db_connection()

class Product:
    def __init__(self,product_id,name,price,quantity):
        self.product_id = product_id,
        self.name = name,
        self.price = price,
        self.quantity = quantity

        product = [int(product_id),
                   str(name).replace(' ','').strip(),
                   float(price),
                   int(quantity)]

        try:
            create_connection = sqlite3.connect('inventory_mgmt.db')
            create_cursor = create_connection.cursor()
            create_cursor.execute('INSERT INTO products (product_id, name, price, quantity) VALUES (?, ?, ?, ?)', product)
            create_connection.commit()
            print(f'Product Successfully Added:\nProduct Id: {product_id}\nDescription: {name}\nPrice: ${price}\nQuantity: {quantity}')
        except sqlite3.IntegrityError:
            print('Product Already Exists')
            return


p1 = Product(111111,"Wheel Hub",250.45,10)

