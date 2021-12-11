from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = "1m9n3gs5sa6j4sjf7h8hu829739kdh"
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')

    return app

