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
    def __init__(self):
        self.new_product_info = []

    def add_new_product(self):

        product_id = input('Enter Product Id: ')
        name = input('Enter Product Name: ')
        price = input('Enter Product Price: ')
        quantity = input('Enter Product Quantity: ')
        self.new_product_info.extend([product_id,name,price,quantity])

        create_connection1 = None

        try:
            create_connection1 = sqlite3.connect('inventory_mgmt.db', timeout=10)
            create_cursor = create_connection1.cursor()
            create_cursor.execute('INSERT INTO products (product_id, name, price, quantity) VALUES (?, ?, ?, ?)', self.new_product_info)
            create_connection1.commit()
            create_connection1.close()

            print(f'Product Successfully Added:\nProduct Id: {self.new_product_info[0]}\n'
                  f'Description: {self.new_product_info[1]}\n'
                  f'Price: ${self.new_product_info[2]}\n'
                  f'Quantity: {self.new_product_info[3]}')

        except sqlite3.OperationalError:
            print('Database is locked')

        except sqlite3.IntegrityError:
            print('Product Already Exists')

        finally:
            if create_connection1:
                create_connection1.close()

    def run_menu(self):
        create_db_connection()

        # Controls whether the program continues running
        user_exit = True

        while user_exit:
            # Display the menu options
            print('''-------------------------------- MENU -------------------------------------
        
            1. Add a new product                2. Sell a product
        
            3. Search product by product id     4. Update price of product
        
            5. Display all products             0. Exit
        
            -------------------------------------------------------------------------------''')

            try:
                # User chooses a menu option
                user_selection = int(input('Select a number from the menu to continue: \n'))

                # match-case handles the menu logic cleanly
                match user_selection:

                    case 1:
                        # Add a new product into inventory
                        print('Enter new product information.')
                        self.add_new_product()

                    case 2:
                        # Sell a product by product id and update amount in inventory
                        print('Enter product id to sell.')

                    case 3:
                        # Find and display a product by product id
                        print('Enter product id to find.')

                    case 4:
                        # Update the price of an existing product
                        print('Enter product id to update.')
                    case 5:
                        # Display all products stored in the inventory
                        print('Display all products.')

                    case 0:
                        # Stop the loop and exit program
                        user_exit = False
                        break

                    case _:
                        # Handles numbers that are not valid menu choices
                        print('Invalid input! Please select an item from the menu.')

            except ValueError:
                # Handles any non-numeric entry in the menu
                print('Invalid input! Please select an item from the menu.')


