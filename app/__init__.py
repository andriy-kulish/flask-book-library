import os
from flask import Flask
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
exists = os.path.isfile(app.config['DATABASE'])
if not exists:
    import db_fill
from app import views, models