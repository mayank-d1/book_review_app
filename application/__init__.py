from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Globally accessible libraries
db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from .routes import user, book
        from .models.user import User
        from .models.book import Book

        # Register Blueprints
        app.register_blueprint(user.user_bp)
        app.register_blueprint(book.book_bp)

        db.create_all()

        return app
