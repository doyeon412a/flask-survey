from proj import db
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
import os
import csv
import pickle


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')

    def can(self, permissions):
        return self.role is not None and permissions in self.role.permissions

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return str(self.id)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    permissions = db.Column(db.PickleType, default=[])

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def remove_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)

    def reset_permissions(self):
        self.permissions = []

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'permissions': pickle.dumps(self.permissions).decode()
        }
        return data

class Roles:
    USER = 'user'
    ADMIN = 'admin'
    SUPERADMIN = 'superadmin'

def create_roles():
    role = Role.query.filter_by(name=Roles.USER).first()
    if role is None:
        user_role = Role(name=Roles.USER, permissions=[])

        admin_role = Role(name=Roles.ADMIN, permissions=[])
        admin_role.add_permission('admin')

        superadmin_role = Role(name=Roles.SUPERADMIN, permissions=[])
        superadmin_role.add_permission('admin')
        superadmin_role.add_permission('superadmin')

        db.session.add_all([user_role, admin_role, superadmin_role])
        db.session.commit()

def create_superadmin():
    superadmin_role = Role.query.filter_by(name=Roles.SUPERADMIN).first()

    user = User.query.filter_by(email='superadmin@aaaa.aa').first()
    if user is None:
        user = User(email='superadmin@aaaa.aa',
                    password=generate_password_hash('password412')
        )
        user.role = superadmin_role
        db.session.add(user)
        db.session.commit()

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
    a3 = db.Column(db.Text(), nullable=False)
    a4 = db.Column(db.String(100), nullable=False)
    a5 = db.Column(db.String(100), nullable=False)
    a6 = db.Column(db.String(100), nullable=False)
    a7 = db.Column(db.String(100), nullable=False)
    a8 = db.Column(db.String(100), nullable=False)
    a9 = db.Column(db.String(100), nullable=False)
    a10 = db.Column(db.String(100), nullable=False)
    a11 = db.Column(db.String(100), nullable=False)
    a12 = db.Column(db.String(100), nullable=False)

class Survey2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer)
    a1 = db.Column(db.Integer, nullable=False)
    a2 = db.Column(db.Integer, nullable=False)
    a3 = db.Column(db.Integer, nullable=False)
    a4 = db.Column(db.Integer, nullable=False)
    a5 = db.Column(db.Integer, nullable=False)
    a6 = db.Column(db.Integer, nullable=False)
    a7 = db.Column(db.Integer, nullable=False)

class Survey3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer)
    a1 = db.Column(db.Integer, nullable=False)
    a2 = db.Column(db.Integer, nullable=False)
    a3 = db.Column(db.Integer, nullable=False)
    a4 = db.Column(db.Integer, nullable=False)

class Survey4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer)
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

class Survey5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer)
    a1 = db.Column(db.String(100), nullable=False)
    a2 = db.Column(db.String(100), nullable=False)
    a3 = db.Column(db.Text(), nullable=False)
    a4 = db.Column(db.Text(), nullable=False)

def create_data():
    if (Item_area.query.get(1) == None):
        area_count = 0
        title_count = 0
        count = 0
        target = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.csv')
        with open(target, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for i in reader:
                # print(i)

                if (int(i[1]) > area_count):
                    area_count += 1
                    new_entry = Item_area(area=i[2])
                    db.session.add(new_entry)
                    db.session.commit()
                if (int(i[3]) > title_count):
                    title_count += 1
                    new_entry = Item_title(area=Item_area.query.get(area_count),
                                                  title=i[4])
                    db.session.add(new_entry)
                    db.session.commit()
                new_entry = Item_content(title=Item_title.query.get(title_count),
                                                content=i[5],
                                                usage=i[6])
                db.session.add(new_entry)
                db.session.commit()
                count += 1
                if (int(i[6]) != 3):
                    for j in range(7, 24):
                        if (i[j] == ''):
                            break
                        new_entry = Item_example(content=Item_content.query.get(count),
                                                        example=i[j])
                        db.session.add(new_entry)
                        db.session.commit()

    # 만족도조사
    if (Survey_title.query.get(1) == None):
        title_count = 0
        content_count = 0
        count = 0
        target = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'survey_data2.csv')
        with open(target, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for i in reader:
                count += 1
                if (int(i[1]) > title_count):
                    title_count += 1
                    content_count = 0
                    new_entry = Survey_title(num=title_count, title=i[2])
                    db.session.add(new_entry)
                    db.session.commit()
                if (int(i[3]) > content_count):
                    content_count += 1
                    new_entry = Survey_content(title=Survey_title.query.get(title_count),
                                                      num=content_count, content=i[4], usage=i[5])
                    db.session.add(new_entry)
                    db.session.commit()

                if (int(i[5]) != 3):
                    for j in range(6, 23):
                        if (i[j] == ''):
                            break
                        new_entry = Survey_example(content=Survey_content.query.get(count),
                                                          example=i[j])
                        db.session.add(new_entry)
                        db.session.commit()