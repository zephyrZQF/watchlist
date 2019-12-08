from watchlist import app
from watchlist.models import User,Movie
from flask import render_template,url_for



@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html',user=user,movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return 'User page : %s' %name

@app.route('/test')
def test_url_for():
    print(url_for('index'))
    print(url_for('user_page',name='greyzhu'))
    print(url_for('user_page',name='peter'))
    print(url_for('test_url_for'))
    return 'Test page'

@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html',user=user),404