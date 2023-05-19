from app.extensions import Flask, db,DebugToolbarExtension
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    DebugToolbarExtension(app)
    """Initialize Flask extensions here"""
    db.init_app(app)
    """------------------END----------------------------------------------"""

    """Register blueprint here"""
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.search import bp as search_bp
    app.register_blueprint(search_bp, url_prefix='/search')

    """------------------END----------------------------------------------"""
    
    """Route for testing Application Factory Pattern"""
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app