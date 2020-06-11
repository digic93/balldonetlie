import os

from flask import Flask, redirect, url_for

path_json_playres = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'players.json')

def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .views import players
    app.register_blueprint(players.bp)

    @app.route('/')
    def app_index():
        return redirect(url_for('players.index'))

    return app
