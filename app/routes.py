from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfilePostForm, PostForm
from app.models import User, Post
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('homepage.html', title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    # posts = [
    #     {'author': user, 'body': 'Test post #1'},
    #     {'author': user, 'body': 'Test post #2'}
    # ]
    posts = user.posts
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_list', methods=['GET', 'POST'])
@login_required
def edit_list():
    form = EditProfilePostForm()
    if form.validate_on_submit():
        current_user.title = form.title.data
        current_user.body = form.body.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_list'))
    elif request.method == 'GET':
        form.title.data = current_user.title
        form.body.data = current_user.body
    return render_template('edit_list.html', title='Edit List',
                           form=form)

@app.route('/new_list', methods=['GET', 'POST'])
@login_required
def new_list():
    form = PostForm()
    username = current_user.username
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('user', username=username)) # redirect to user profile and pass current username
    return render_template('add_list.html', title='New Post', user=user, 
                           form=form)