from proj import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Item_area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(200), nullable=False)

class Item_title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_id = db.Column(db.Integer, db.ForeignKey('item_area.id', ondelete='CASCADE'))
    area = db.relationship('Item_area', backref=db.backref('item_title_set', cascade='all, delete-orphan'))
    title = db.Column(db.String(200), nullable=False)


class Item_content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_id = db.Column(db.Integer, db.ForeignKey('item_title.id', ondelete='CASCADE'))
    title = db.relationship('Item_title', backref=db.backref('item_content_set', cascade='all, delete-orphan'))
    content = db.Column(db.String(200), nullable=False)
    usage = db.Column(db.Integer, nullable=False)

class Item_example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('item_content.id', ondelete='CASCADE'))
    content = db.relationship('Item_content', backref=db.backref('item_example_set', cascade='all, delete-orphan'))
    example = db.Column(db.String(200), nullable=False)

class Item_answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('item_content.id', ondelete='CASCADE'))
    content = db.relationship('Item_content', backref=db.backref('item_answer_set', cascade='all, delete-orphan'))
    answer = db.Column(db.String(200), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Survey_title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)


class Survey_content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_id = db.Column(db.Integer, db.ForeignKey('survey_title.id', ondelete='CASCADE'))
    title = db.relationship('Survey_title', backref=db.backref('survey_content_set', cascade='all, delete-orphan'))
    num = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    usage = db.Column(db.Integer, nullable=False)

class Survey_example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('survey_content.id', ondelete='CASCADE'))
    content = db.relationship('Survey_content', backref=db.backref('survey_example_set', cascade='all, delete-orphan'))
    example = db.Column(db.String(200), nullable=False)
class Survey1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a1 = db.Column(db.String(100), nullable=False)
    a2 = db.Column(db.String(100), nullable=False)
    a3 = db.Column(db.String(100), nullable=False)
    a4 = db.Column(db.String(100), nullable=False)
    a5 = db.Column(db.String(100), nullable=False)
    a6 = db.Column(db.String(100), nullable=False)
    a7 = db.Column(db.String(100), nullable=False)
    a8 = db.Column(db.String(100), nullable=False)
    a9 = db.Column(db.String(100), nullable=False)

class Survey2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a1 = db.Column(db.Integer, nullable=False)
    a2 = db.Column(db.Integer, nullable=False)
    a3 = db.Column(db.Integer, nullable=False)
    a4 = db.Column(db.Integer, nullable=False)
    a5 = db.Column(db.Integer, nullable=False)
    a6 = db.Column(db.Integer, nullable=False)
    a7 = db.Column(db.Integer, nullable=False)

class Survey3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a1 = db.Column(db.Integer, nullable=False)
    a2 = db.Column(db.Integer, nullable=False)
    a3 = db.Column(db.Integer, nullable=False)
    a4 = db.Column(db.Integer, nullable=False)

class Survey4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a1 = db.Column(db.Integer, nullable=False)
    a2 = db.Column(db.Integer, nullable=False)
    a3 = db.Column(db.Integer, nullable=False)
    a4 = db.Column(db.Integer, nullable=False)
    a5 = db.Column(db.Integer, nullable=False)
    a6 = db.Column(db.Integer, nullable=False)
    a7 = db.Column(db.Integer, nullable=False)
    a8 = db.Column(db.Integer, nullable=False)
    a9 = db.Column(db.Integer, nullable=False)
    a10 = db.Column(db.Integer, nullable=False)
    a11 = db.Column(db.Integer, nullable=False)
    a12 = db.Column(db.Integer, nullable=False)
    a13 = db.Column(db.Integer, nullable=False)
    a14 = db.Column(db.Integer, nullable=False)
    a15 = db.Column(db.Integer, nullable=False)
    a16 = db.Column(db.Integer, nullable=False)
    a17 = db.Column(db.Integer, nullable=False)
    a18 = db.Column(db.Integer, nullable=False)
    a19 = db.Column(db.Integer, nullable=False)
    a20 = db.Column(db.Integer, nullable=False)
    a21 = db.Column(db.Integer, nullable=False)
    a22 = db.Column(db.Integer, nullable=False)

class Survey5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a1 = db.Column(db.String(100), nullable=False)
    a2 = db.Column(db.String(100), nullable=False)
    a3 = db.Column(db.Text(), nullable=False)
    a4 = db.Column(db.Text(), nullable=False)