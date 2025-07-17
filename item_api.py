from flask import Blueprint, request, jsonify
import sqlite3

item_api = Blueprint('item_api', __name__)

def get_db():
    """
    Establishes and returns a connection to the 'ecom.db' SQLite database.
    
    Returns:
        sqlite3.Connection: A connection object to the 'ecom.db' database.
    """
    return sqlite3.connect('ecom.db')

@item_api.route('/item/create', methods=['POST'])
def create_item():
    """
    Creates a new item in the database using the provided JSON data.
    
    Expects a JSON payload with `name`, `price`, and `category` fields in the request body. Returns a JSON message confirming item creation.
    """
    data = request.json
    name = data.get('name')
    price = data.get('price')
    category = data.get('category')
    con = get_db()
    cur = con.cursor()
    # SQL Injection, no validation
    cur.execute(f"INSERT INTO items (name, price, category) VALUES ('{name}', {price}, '{category}')")
    con.commit()
    con.close()
    return jsonify({'msg': 'item created'})

@item_api.route('/item/<id>', methods=['GET'])
def get_item(id):
    """
    Retrieve an item by its ID from the database and return its details as a JSON object.
    
    Parameters:
        id (int): The unique identifier of the item to retrieve.
    
    Returns:
        Response: A Flask JSON response containing the item's id, name, price, and category.
    
    Note:
        If no item with the specified ID exists, this function may raise an exception due to attempting to access fields of a None value.
    """
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM items WHERE id={id}")
    item = cur.fetchone()
    # Null pointer risk
    return jsonify({'id': item[0], 'name': item[1], 'price': item[2], 'category': item[3]})
