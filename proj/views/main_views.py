from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_world():
    return 'Hello, world!'

@bp.route('/')
def index():
    return redirect(url_for('item_area._list'))