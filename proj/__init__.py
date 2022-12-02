from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os
import csv

import config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    with app.app_context():
        if (models.Item_area.query.get(1) == None):
            area_count = 0
            title_count = 0
            count=0
            target = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.csv')
            with open(target, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for i in reader:
                    # print(i)

                    if (int(i[1]) > area_count):
                        area_count += 1
                        new_entry = models.Item_area(area=i[2])
                        db.session.add(new_entry)
                        db.session.commit()
                    if(int(i[3])>title_count):
                        title_count+=1
                        new_entry =models.Item_title(area=models.Item_area.query.get(area_count),
                                                     title=i[4])
                        db.session.add(new_entry)
                        db.session.commit()
                    new_entry = models.Item_content(title=models.Item_title.query.get(title_count),
                                                    content=i[5],
                                                    usage=i[6])
                    db.session.add(new_entry)
                    db.session.commit()
                    count+=1
                    if(int(i[6])!=3):
                        for j in range(7,24):
                            if(i[j]==''):
                                break
                            new_entry = models.Item_example(content=models.Item_content.query.get(count),
                                                            example=i[j])
                            db.session.add(new_entry)
                            db.session.commit()

        #만족도조사
        if (models.Survey_title.query.get(1) == None):
            title_count = 0
            content_count = 0
            count=0
            target = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'survey_data.csv')
            with open(target, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for i in reader:
                    count+=1
                    if (int(i[1]) > title_count):
                        title_count += 1
                        content_count = 0
                        new_entry = models.Survey_title(num=title_count, title=i[2])
                        db.session.add(new_entry)
                        db.session.commit()
                    if(int(i[3])>content_count):
                        content_count+=1
                        new_entry =models.Survey_content(title=models.Survey_title.query.get(title_count),
                                                     num=content_count, content=i[4], usage=i[5])
                        db.session.add(new_entry)
                        db.session.commit()

                    if(int(i[5])!=3):
                        for j in range(6,23):
                            if(i[j]==''):
                                break
                            new_entry = models.Survey_example(content=models.Survey_content.query.get(count),
                                                            example=i[j])
                            db.session.add(new_entry)
                            db.session.commit()

    #블루프린트
    from .views import main_views, question_views, answer_views, auth_views,item_area_views, survey_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(item_area_views.bp)
    app.register_blueprint(survey_views.bp)

    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(models.User, db.session, endpoint="users_"))
    #admin.add_view(ModelView(models.Question, db.session, endpoint="questions_"))
    #admin.add_view(ModelView(models.Answer, db.session, endpoint="answers_"))
    admin.add_view(ModelView(models.Item_area, db.session, endpoint="item_area_"))
    admin.add_view(ModelView(models.Item_title, db.session, endpoint="item_title_"))
    admin.add_view(ModelView(models.Item_content, db.session, endpoint="item_content_"))
    admin.add_view(ModelView(models.Item_example, db.session, endpoint="item_example_"))
    admin.add_view(ModelView(models.Survey_title, db.session, endpoint="survey_title_"))
    admin.add_view(ModelView(models.Survey_content, db.session, endpoint="survey_content_"))
    admin.add_view(ModelView(models.Survey_example, db.session, endpoint="survey_example_"))
    admin.add_view(ModelView(models.Survey1, db.session, endpoint="survey1_"))
    admin.add_view(ModelView(models.Survey2, db.session, endpoint="survey2_"))
    admin.add_view(ModelView(models.Survey3, db.session, endpoint="survey3_"))
    admin.add_view(ModelView(models.Survey4, db.session, endpoint="survey4_"))
    admin.add_view(ModelView(models.Survey5, db.session, endpoint="survey5_"))

    return app
