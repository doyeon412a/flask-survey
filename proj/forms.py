from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력해주세요')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요')])

class UserCreateForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])

#만족도 조사
class Survey1Form(FlaskForm):
    gender = RadioField('1. 선생님의 성별은 무엇입니까?',
                        choices=[('M', '남성'), ('F', '여성')], validators=[DataRequired()])
    school = RadioField('2. 선생님이 재직하는 학교급은 무엇입니까?',
                        choices=[('E', '초등'), ('M', '중학'), ('H', '고교')], validators=[DataRequired()])
    year = RadioField('3. 선생님의 재직기간은 몇 년입니까?',
                        choices=[('20+', '20년 이상'), ('10-19', '20년 미만'), ('7-9', '10년 미만'), ('3-6', '7년 미만'), ('0-2', '3년 미만')], validators=[DataRequired()])
    location = RadioField('4. 선생님의 소속 시ㆍ도는 무엇입니까?',
                      choices=[('강원', '강원'), ('경기', '경기'), ('경남', '경남'), ('경북', '경북'), ('광주', '광주'), ('대구', '대구'), ('대전', '대전'), ('부산', '부산'),
                               ('서울', '서울'), ('울산', '울산'), ('인천', '인천'), ('전남', '전남'), ('전북', '전북'), ('제주', '제주'), ('충남', '충남'), ('충북', '충북'), ('세종', '세종')]
                          , validators=[DataRequired()])