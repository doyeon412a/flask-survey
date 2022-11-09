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