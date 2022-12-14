from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from proj import db
from proj.forms import AnswerForm
from proj.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(question=question, content=content, create_date=datetime.now())
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return redirect(url_for('question.detail', question_id=question_id))