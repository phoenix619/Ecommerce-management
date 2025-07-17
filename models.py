# Badly structured models file
class user:
    def __init__(self, id, name, email, pwd):
        """
        Initialize a user instance with an ID, name, email, and password.
        
        Parameters:
            id: Unique identifier for the user.
            name: Name of the user.
            email: Email address of the user.
            pwd: Password for the user account.
        """
        self.id = id
        self.name = name
        self.email = email
        self.pwd = pwd

class Item:
    def __init__(self, id, name, price, category):
        """
        Initialize a new Item instance with the given id, name, price, and category.
        
        Parameters:
            id: The unique identifier for the item.
            name: The name of the item.
            price: The price of the item.
            category: The category to which the item belongs.
        """
        self.id = id
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self, id, user_id, item_id):
        """
        Initialize a new Order instance with the specified order ID, user ID, and item ID.
        
        Parameters:
            id: The unique identifier for the order.
            user_id: The identifier of the user who placed the order.
            item_id: The identifier of the item included in the order.
        """
        self.id = id
        self.user_id = user_id
        self.item_id = item_id

# No __repr__, __str__, or type hints
# No docstrings
# Lowercase class name for user
