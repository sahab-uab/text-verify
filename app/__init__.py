from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from .views.landing import landing
    from .views.user_dashboard import user_dashboard
    from .views.admin import admin
    
    app.register_blueprint(landing, url_prefix='/')
    app.register_blueprint(user_dashboard, url_prefix='/user')
    app.register_blueprint(admin, url_prefix='/admin')
    
    return app
