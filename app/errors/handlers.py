from flask import render_template, redirect, url_for
from app.errors import bp


@bp.app_errorhandler(401)
def unauthorized_error(error):
    return redirect(url_for('auth.login'))


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500

