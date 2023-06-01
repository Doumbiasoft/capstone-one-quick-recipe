from app.extensions import Flask, db,DebugToolbarExtension,Session,Object2Json,numpy
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize the session extension
    Session(app)
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

    @app.context_processor
    def utility_simplenamespace():
        def obj_to_json(obj):
            return Object2Json(obj)
        return dict(obj_to_json=obj_to_json)

    @app.context_processor
    def utility_processor():
        def generate_float_range(x:float,y:float):
            return numpy.arange(x, y)
        return dict(generate_float_range=generate_float_range)


    return app