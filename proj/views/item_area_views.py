
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from proj.models import Item_area
from proj.forms import QuestionForm, AnswerForm

bp = Blueprint('item_area', __name__, url_prefix='/item_area')

@bp.route('/list/')
def _list():
    item_area_list=Item_area.query.order_by()
    return render_template('item_area/item_area_list.html', item_area_list=item_area_list)


@bp.route('/detail/<int:item_area_id>/')
def detail(item_area_id):
    form = AnswerForm()
    item_area=Item_area.query.get_or_404(item_area_id)
    return render_template('item_area/item_area_detail.html', item_area=item_area, form=form)
'''
@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)
'''