from flask import Flask
from flask_login import LoginManager
from .config import Config
from .db import DB


login = LoginManager()
login.login_view = 'users.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.db = DB(app)
    login.init_app(app)

    from .index import bp as index_bp
    app.register_blueprint(index_bp)

    from .users import bp as user_bp
    app.register_blueprint(user_bp)
    
    from .product_rating import bp as user_bp
    app.register_blueprint(user_bp)

    from .seller_rating import bp as user_bp
    app.register_blueprint(user_bp)

    from .products import bp as products_bp
    app.register_blueprint(products_bp)

    from .wishlist import bp as wishes_bp
    app.register_blueprint(wishes_bp)

    from .seller_inventory import bp as seller_inventory_bp
    app.register_blueprint(seller_inventory_bp)

    from .carts import bp as carts_bp
    app.register_blueprint(carts_bp)

    return app
