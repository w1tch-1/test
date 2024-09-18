from flask import render_template, request, redirect
from flask_login import login_user, current_user, login_required


from app.config import app, login_manager
from app.db import User, db, Post, Comments
from .forms import RegistrationForm, LoginForm


__all__ = ('index', 'load_user', 'registration', 'login',)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def index():
    posts = Post.query.all()
    return render_template('index.html', title='Home', posts=posts)


@app.route('/delete-post', methods=['GET', 'POST'])
def delete_post():
    post = Post.query.get(request.args.get('id'))
    db.session.delete(post)
    db.session.commit()
    return redirect('/')


@app.route('/view-post/<int:id>')
def view_post(id):
    post = Post.query.get(id)
    user = User.query.get(post.user)
    date = post.date_posted.strftime("%d.%m.%Y")
    return render_template('posts.html', post=post, user=user, date=date)


@app.route('/view-profiles/<int:profiles_id>')
def profiles(profiles_id):
    user = User.query.get(profiles_id)
    return render_template('profiles.html', user=user)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    forms = RegistrationForm()
    if forms.validate_on_submit():
        username = forms.username.data
        email = forms.email.data
        password = forms.password.data
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('registration.html', forms=forms)


@app.route('/login', methods=['GET', 'POST'])
def login():
    logins = LoginForm()
    if logins.validate_on_submit():
        username = logins.username.data
        password = logins.password.data
        # remember_me = request.form.get('remember_me') == 'on'
        user = User.query.filter_by(username=username).first()
        if user is None or user.password != password:
            return render_template('login.html', message='Invalid username or password')
        login_user(user)
        return redirect('/')
    return render_template('login.html', logins=logins)


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        text = request.form.get('post_text')
        post = Post(text=text, user=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('create.html')


@app.route('/add-post', methods=['POST'])
def add_post():
    text = request.form['text']
    comm = Comments(text=text)
    db.session.add(comm)
    db.session.commit()
    return {'post': request.form['text']}
