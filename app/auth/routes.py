from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm
from app.models import User


@bp.after_request
def after_request(response):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    return response


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None or not user.check_password(request.form['password']):
            return redirect(url_for('auth.login'))
        login_user(user)
        flash("You have successfully logged in!")
        return redirect(url_for('dashboard.index'))
    return render_template('auth/login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("You have successfully registered!")
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
