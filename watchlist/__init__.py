import os
import click

from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控
app.config['SECRET_KEY'] = 'dev'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    user = models.User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'


@app.context_processor
def inject_user():
    user = models.User.query.first()
    return dict(user=user)

from watchlist import views,commands,models,errors
