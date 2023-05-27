from flask import Blueprint, url_for, render_template, flash, request, abort, session, g, redirect
from flask_login import login_user, logout_user, current_user, login_required, current_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from proj import db
from proj.forms import UserCreateForm, UserLoginForm
from proj.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
@bp.route('/admin')
@login_required
@permission_required('admin')
def admin():
    return "관리자 페이지 입니다."

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            user = User(email=form.email.data,
                        password=generate_password_hash(form.password1.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('존재하지 않는 사용자입니다.')
        elif not check_password_hash(user.password, form.password.data):
            flash('비밀번호가 올바르지 않습니다.')
        else:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)


'''
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
'''
'''
@bp.before_app_request
def is_logged_in_user():
    if current_user.is_authenticated:
        g.user = current_user
    else:
        g.user = None

'''
@bp.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))