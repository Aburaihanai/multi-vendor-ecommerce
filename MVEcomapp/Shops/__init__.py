from flask import Flask, current_app
from .config import Config
from .extensions import db, migrate, login_manager, mail, moment

# Import blueprints
from .customer import customer_bp
from .auth import auth_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    # Register blueprints
    app.register_blueprint(customer_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # User loader for Flask-Login
    from Shops.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
