
from flask import Blueprint, render_template, request, url_for, flash, session
from werkzeug.utils import redirect

from .. import db
from .. import models
from proj.models import Survey_title, Survey1, Survey2, Survey3, Survey4, Survey5
from proj.forms import Survey1Form

bp = Blueprint('survey', __name__, url_prefix='/survey')

@bp.route('/survey1/', methods=['GET', 'POST'])
def survey1():
    form = Survey1Form()
    '''
    if request.method == 'POST' and form.validate_on_submit():
        survey = Survey1(gender=form.gender.data, school=form.school.data, year=form.year.data, location=form.location.data)
        db.session.add(survey)
        db.session.commit()
        #return redirect(url_for('main.index'))
    '''
    return render_template('survey/survey1.html', form=form)

@bp.route('/list/')
def _list():
    survey_title_list=Survey_title.query.order_by()
    return render_template('survey/survey1.html', survey_title_list=survey_title_list)


@bp.route('/<int:survey_title_id>/', methods=('GET', 'POST'))
def detail(survey_title_id):
    survey_title=Survey_title.query.get_or_404(survey_title_id)
    if request.method == 'POST':
        ip = request.remote_addr
        if(survey_title_id==1):
            ans=[0 for i in range(9)]
            cnt=0

            for survey_content in survey_title.survey_content_set:
                if survey_content.usage == 4:
                    alist = request.form.getlist(str(survey_content.id))

                    ans[cnt]=""
                    for a in alist:
                        ans[cnt]+=", "+a
                    ans[cnt]=ans[cnt][2:]

                else:
                    ans[cnt]=request.form.get(str(survey_content.id))
                cnt+=1

            survey = Survey1(a1=ans[0],a2=ans[1],a3=ans[2],a4=ans[3],a5=ans[4],a6=ans[5],a7=ans[6],a8=ans[7],a9=ans[8])
            db.session.add(survey)
            db.session.commit()
            session.clear()
            session['survey_id']=survey.id
            return redirect(url_for('survey.detail', survey_title_id=2))

        elif survey_title_id==2:
            ans=[0 for i in range(7)]
            cnt=0

            for survey_content in survey_title.survey_content_set:
                a=request.form.get(str(survey_content.id))
                if a=="매우 불만족":
                    ans[cnt]=1
                elif a=="불만족":
                    ans[cnt]=2
                elif a=="보통":
                    ans[cnt]=3
                elif a=="만족":
                    ans[cnt]=4
                elif a=="매우 만족":
                    ans[cnt]=5
                else:
                    ans[cnt]=6
                cnt+=1

            survey_id=session.get('survey_id')
            survey = Survey2(survey_id=survey_id, a1=ans[0],a2=ans[1],a3=ans[2],a4=ans[3],a5=ans[4],a6=ans[5],a7=ans[6])
            db.session.add(survey)
            db.session.commit()
            return redirect(url_for('survey.detail', survey_title_id=3))

        elif survey_title_id==3:
            ans=[0 for i in range(4)]
            cnt=0

            for survey_content in survey_title.survey_content_set:
                a=request.form.get(str(survey_content.id))
                if a=="매우 불만족":
                    ans[cnt]=1
                elif a=="불만족":
                    ans[cnt]=2
                elif a=="보통":
                    ans[cnt]=3
                elif a=="만족":
                    ans[cnt]=4
                elif a=="매우 만족":
                    ans[cnt]=5
                else:
                    ans[cnt]=6
                cnt+=1
            survey_id = session.get('survey_id')
            survey = Survey3(survey_id=survey_id, a1=ans[0],a2=ans[1],a3=ans[2],a4=ans[3])
            db.session.add(survey)
            db.session.commit()
            return redirect(url_for('survey.detail', survey_title_id=4))

        elif survey_title_id==4:
            ans=[0 for i in range(22)]
            cnt=0

            for survey_content in survey_title.survey_content_set:
                a=request.form.get(str(survey_content.id))
                if a=="매우 불만족":
                    ans[cnt]=1
                elif a=="불만족":
                    ans[cnt]=2
                elif a=="보통":
                    ans[cnt]=3
                elif a=="만족":
                    ans[cnt]=4
                elif a=="매우 만족":
                    ans[cnt]=5
                else:
                    ans[cnt]=6
                cnt+=1
            survey_id = session.get('survey_id')
            survey = Survey4(survey_id=survey_id, a1=ans[0],a2=ans[1],a3=ans[2],a4=ans[3],a5=ans[4],a6=ans[5],a7=ans[6],a8=ans[7],a9=ans[8],a10=ans[9],
                             a11=ans[10],a12=ans[11],a13=ans[12],a14=ans[13],a15=ans[14],a16=ans[15],a17=ans[16],a18=ans[17],a19=ans[18],a20=ans[19],
                             a21=ans[20],a22=ans[21])
            db.session.add(survey)
            db.session.commit()
            return redirect(url_for('survey.detail', survey_title_id=5))

        elif survey_title_id==5:
            ans=[0 for i in range(4)]
            cnt=0

            for survey_content in survey_title.survey_content_set:
                if survey_content.usage == 4:
                    alist = request.form.getlist(str(survey_content.id))

                    ans[cnt] = ""
                    for a in alist:
                        ans[cnt] += ", " + a
                    ans[cnt] = ans[cnt][2:]

                else:
                    ans[cnt] = request.form.get(str(survey_content.id))
                cnt += 1
            survey_id = session.get('survey_id')
            survey = Survey5(survey_id=survey_id, a1=ans[0],a2=ans[1],a3=ans[2],a4=ans[3])
            db.session.add(survey)
            db.session.commit()
            return redirect(url_for('survey.finish'))

    return render_template('survey/survey1.html', survey_title=survey_title)

@bp.route('/finish')
def finish():
    return '만족도 조사가 완료되었습니다. 감사합니다!'