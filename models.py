import sqlite3

def create_db_connection():
    create_connection = sqlite3.connect('inventory_mgmt.db', timeout=10)
    create_cursor = create_connection.cursor()
    create_cursor.execute('CREATE TABLE IF NOT EXISTS products ('
                          'product_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                          'name TEXT NOT NULL,'
                          'price REAL NOT NULL,'
                          'quantity INTEGER)')
    create_connection.commit()
    create_connection.close()



class Product:
    def __init__(self,product_id,name,price,quantity):
        self.product_id = product_id,
        self.name = name,
        self.price = price,
        self.quantity = quantity

        global product
        product = [int(product_id),
                   str(name).replace(' ','').strip(),
                   float(price),
                   int(quantity)]


    def product_to_db(self):
        try:
            create_connection1 = sqlite3.connect('inventory_mgmt.db', timeout=10)
            create_cursor = create_connection1.cursor()
            create_cursor.execute('INSERT INTO products (product_id, name, price, quantity) VALUES (?, ?, ?, ?)', product)
            create_connection1.commit()
            create_connection1.close()

            print(f'Product Successfully Added:\nProduct Id: {self.product_id}\n'
                  f'Description: {self.name}\n'
                  f'Price: ${self.price}\n'
                  f'Quantity: {self.quantity}')

        except sqlite3.OperationalError:
            print('Database is locked')

        except sqlite3.IntegrityError:
            print('Product Already Exists')





