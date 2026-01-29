from models import *

def __main__():
    create_db_connection()
    p1 = Product(111111, 'Wheel Hub', 250.45, 10)
    p1.product_to_db()

    p2 = Product(234123, 'Fuse Box', 98.34, 5)
    p2.product_to_db()

if __name__ == '__main__':
    __main__()