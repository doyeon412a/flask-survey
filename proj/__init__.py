from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

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

    #블루프린트
    from .views import main_views, question_views, answer_views, auth_views,item_area_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(item_area_views.bp)


    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(models.User, db.session, endpoint="users_"))
    #admin.add_view(ModelView(models.Question, db.session, endpoint="questions_"))
    #admin.add_view(ModelView(models.Answer, db.session, endpoint="answers_"))
    admin.add_view(ModelView(models.Item_area, db.session, endpoint="item_area_"))
    admin.add_view(ModelView(models.Item_title, db.session, endpoint="item_title_"))
    admin.add_view(ModelView(models.Item_content, db.session, endpoint="item_content_"))

    return app
