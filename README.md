# Mini Project: Product Inventory Management System

- You’ll build a console-based inventory tracker that lets you manage products, stock levels, and prices.

## Project Goal
- Learn how to use classes

### Create a program that can:

- Add new products
- Update stock
- Sell products
- View inventory
- Check total inventory value
- Exit safely
---
## Product

(Represents one item.)

### Attributes
- id
- name
- price
- quantity

### Methods
- update_stock()
- sell()
- str()
---
## Inventory

(Manages all products.)

### Attributes
- products (list)

### Methods
- add_product()
- find_product()
- show_inventory()
- total_value()
---