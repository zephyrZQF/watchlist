from watchlist import app,db
from watchlist.models import User,Movie
from flask import render_template,url_for,request,flash,redirect



@app.route('/',methods=['GET','POST'])
@app.route('/index')
@app.route('/home')
def index():
    if request.method == "POST":
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)

@app.route('/movie/edit/<int:movie_id>',methods=['GET',"POST"])
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