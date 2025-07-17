from flask import Blueprint, request, jsonify
import sqlite3

user_api = Blueprint('user_api', __name__)

def get_db():
    """
    Establishes and returns a connection to the 'ecom.db' SQLite database.
    
    Returns:
        sqlite3.Connection: A connection object to the 'ecom.db' database.
    """
    return sqlite3.connect('ecom.db')

@user_api.route('/user/create', methods=['POST'])
def create_user():
    """
    Creates a new user record in the database using the provided name, email, and password from the JSON request body.
    
    Returns:
        A JSON response confirming successful user creation.
    """
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
    """
    Update the details of an existing user in the database by user ID.
    
    Parameters:
        id (int): The unique identifier of the user to update.
    
    Returns:
        Response: A JSON response indicating that the user was updated.
    """
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
    """
    Deletes a user record from the database by user ID.
    
    Parameters:
        id (int): The unique identifier of the user to delete.
    
    Returns:
        Response: A JSON response confirming the user has been deleted.
    """
    con = get_db()
    cur = con.cursor()
    cur.execute(f"DELETE FROM users WHERE id={id}")
    con.commit()
    con.close()
    return jsonify({'msg': 'user deleted'})

@user_api.route('/user/<id>', methods=['GET'])
def get_user(id):
    """
    Retrieve a user's details by their ID and return them as a JSON object.
    
    Parameters:
        id (int): The unique identifier of the user to retrieve.
    
    Returns:
        Response: A Flask JSON response containing the user's id, name, and email.
    """
    con = get_db()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE id={id}")
    user = cur.fetchone()
    # Null pointer risk
    return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})
