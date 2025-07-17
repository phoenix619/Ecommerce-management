from flask import Blueprint, request, jsonify
import sqlite3

user_api = Blueprint('user_api', __name__)

def get_db():
    return sqlite3.connect('ecom.db')

@user_api.route('/user/create', methods=['POST'])
def create_user():
    data = request.json
    name = data['name'] if 'name' in data else None
    email = data['email'] if 'email' in data else None
    pwd = data['password'] if 'password' in data else None
    con = get_db()
    cur = con.cursor()
    # SQL Injection, no validation
    cur.execute(f"INSERT INTO users (name, email, pwd) VALUES ('{name}', '{email}', '{pwd}')")
    con.commit()
    con.close()
    return jsonify({'msg': 'user created'})

@user_api.route('/user/update/<id>', methods=['POST'])
def update_user(id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    pwd = data.get('password')
    con = get_db()
    cur = con.cursor()
    cur.execute(f"UPDATE users SET name='{name}', email='{email}', pwd='{pwd}' WHERE id={id}")
    con.commit()
    con.close()
    return jsonify({'msg': 'user updated'})

@user_api.route('/user/delete/<id>', methods=['POST'])
def delete_user(id):
    con = get_db()
    cur = con.cursor()
    cur.execute(f"DELETE FROM users WHERE id={id}")
    con.commit()
    con.close()
    return jsonify({'msg': 'user deleted'})

@user_api.route('/user/<id>', methods=['GET'])
def get_user(id):
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE id={id}")
    user = cur.fetchone()
    # Null pointer risk
    return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})
