from watchlist import app,db
from watchlist.models import User,Movie
from flask import render_template,url_for,request,flash,redirect
from flask_login import login_user,login_required,logout_user,current_user

@app.route('/',methods=['GET','POST'])
@app.route('/index')
@app.route('/home')
def index():
    if request.method == "POST":
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('index'))
        movie = Movie(title = title, year = year)
        db.session.add(movie)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)

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

@app.route('/movie/edit/<int:movie_id>',methods=['GET',"POST"])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit',movie_id=movie_id))
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))
    return render_template('edit.html',movie=movie)

@app.route('/movie/delete/<int:movie_id>',methods=["POST"])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input')
            return redirect(url_for('login'))

        user = User.query.first()
        if username == user.username and  user.validate_password(password):
            login_user(user)
            flash('login success')
            return  redirect(url_for('index'))
        flash('Invalid username or password')

        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye')
    return redirect(url_for('index'))

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']
        if not name or len(name) > 20:
              flash('Invalid input.')
              return redirect(url_for('settings'))
        current_user.name = name
# current_user 会返回当前登录用户的数据库记录对象
# 等同于下面的用法
# user = User.query.first()
# user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))
    return render_template('settings.html')
