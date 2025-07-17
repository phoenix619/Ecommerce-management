from flask import Flask
import user_api
import item_api
import order_api

app = Flask(__name__)

# Register blueprints in a messy way
app.register_blueprint(user_api.user_api)
app.register_blueprint(item_api.item_api)
app.register_blueprint(order_api.order_api)

# No error handling, no config, no structure

if __name__ == '__main__':
    app.run(debug=True)
