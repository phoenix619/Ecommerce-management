from flask import Blueprint, request, jsonify
import sqlite3

order_api = Blueprint('order_api', __name__)

def get_db():
    """
    Establishes and returns a connection to the 'ecom.db' SQLite database.
    
    Returns:
        sqlite3.Connection: A connection object to the 'ecom.db' database.
    """
    return sqlite3.connect('ecom.db')

@order_api.route('/buy', methods=['POST'])
def buy():
    """
    Handles a POST request to place a new order with the specified user and item IDs.
    
    Expects a JSON payload containing `user_id` and `item_id`, inserts a new order into the database, and returns a confirmation message as JSON.
    """
    data = request.json
    user_id = data.get('user_id')
    item_id = data.get('item_id')
    con = get_db()
    cur = con.cursor()
    # No validation, SQL injection
    cur.execute(f"INSERT INTO orders (user_id, item_id) VALUES ({user_id}, {item_id})")
    con.commit()
    con.close()
    return jsonify({'msg': 'order placed'})

@order_api.route('/order/<id>', methods=['GET'])
def get_order(id):
    """
    Retrieve an order by its ID and return its details as a JSON response.
    
    Parameters:
        id (int): The unique identifier of the order to retrieve.
    
    Returns:
        Response: A Flask JSON response containing the order's id, user_id, and item_id.
    """
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM orders WHERE id={id}")
    order = cur.fetchone()
    # Null pointer risk
    return jsonify({'id': order[0], 'user_id': order[1], 'item_id': order[2]})
