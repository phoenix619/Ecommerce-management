import sqlite3

def createdb():
    con = sqlite3.connect('ecom.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, pwd TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL, category TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER, item_id INTEGER)')
    # No foreign keys, no constraints
    con.commit()
    con.close()

if __name__ == '__main__':
    createdb()
