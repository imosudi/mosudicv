from flask import Flask


def miocv():
    app = Flask(__name__)

    from .views import main
    app.register_blueprint(main)
    return app
    pass