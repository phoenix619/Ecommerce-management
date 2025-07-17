from flask import Blueprint, request, jsonify
import sqlite3

item_api = Blueprint('item_api', __name__)

def get_db():
    return sqlite3.connect('ecom.db')

@item_api.route('/item/create', methods=['POST'])
def create_item():
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
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM items WHERE id={id}")
    item = cur.fetchone()
    # Null pointer risk
    return jsonify({'id': item[0], 'name': item[1], 'price': item[2], 'category': item[3]})
