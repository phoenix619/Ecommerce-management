# Badly structured models file
class user:
    def __init__(self, id, name, email, pwd):
        self.id = id
        self.name = name
        self.email = email
        self.pwd = pwd

class Item:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self, id, user_id, item_id):
        self.id = id
        self.user_id = user_id
        self.item_id = item_id

# No __repr__, __str__, or type hints
# No docstrings
# Lowercase class name for user
