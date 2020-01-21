from flask import Flask


def create_app():
    app = Flask(__name__)

    from .blueprints.views import views as vw_blueprint
    app.register_blueprint(vw_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
