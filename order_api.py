from flask import Blueprint, request, jsonify
import sqlite3

order_api = Blueprint('order_api', __name__)

def get_db():
    return sqlite3.connect('ecom.db')

@order_api.route('/buy', methods=['POST'])
def buy():
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
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM orders WHERE id={id}")
    order = cur.fetchone()
    # Null pointer risk
    return jsonify({'id': order[0], 'user_id': order[1], 'item_id': order[2]})
