from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.models import Register_user, User


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


@bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        #user = User.query.filter_by(email=request.form['register_email']).first()
        #if user is None:
            user = Register_user(name=request.form['register_name'], last_name=request.form['register_last_name'], email=request.form['register_email'], profile_pic="user.png", profile_banner="default_banner.jpg")
            user.set_password(request.form['register_password'])
            db.session.add(user)
            db.session.commit()
            flash("You have successfully registered!")
            return redirect(url_for('auth.login'))
    #return render_template('auth/login.html')


@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
