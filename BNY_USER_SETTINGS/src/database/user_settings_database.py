from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy_mptt.mixins import *
from src.models.user_settings_model import UserSettings

engine = create_engine('postgresql://postgres:Ugesh@1995@localhost:5432/BNY')
Session = sessionmaker(bind=engine)
session = Session()


class UserSettingDatabase:

    def save_settings(self, user_settings):
        try:
            result = session.add(user_settings)
            session.commit()
            return {"pdf1": "Success", "pdf2": result}
        except Exception as e:
            print(e)
            return {"pdf1": "Failure", "pdf2": "Error while saving the settings "}

    def check_file_name(self, user_id, settings_type, file_name):
        try:
            new_file_name = file_name.replace(".csv", '')
            search = "%{}%".format(new_file_name)
            print(new_file_name)
            ealias = aliased(UserSettings)
            result = session.query(UserSettings).filter(UserSettings.user_id == user_id,
                                                        UserSettings.user_settings_type == settings_type,
                                                        UserSettings.file_name.like(search)).\
                order_by(desc(UserSettings.created_time)).first()
            print(result)
            return {"pdf1": "Success", "pdf2": result}
        except Exception as e:
            print(e)
            return {"pdf1": "Failure", "pdf2": "Error occurred while checking file name in database"}

    def get_settings(self, user_id, settings_type):
        try:
            ealias = aliased(UserSettings)
            result = session.query(ealias.content).filter(ealias.user_id == user_id). \
                filter(ealias.user_settings_type == settings_type).order_by(desc(ealias.created_time)).first()
            print(result)
            return {"pdf1": "Success", "pdf2": result}
        except Exception as e:
            print(e)
            return {"pdf1": "Failure", "pdf2": "Error occurred while get settings from database"}


    def settings_history(self, user_id, settings_type):
        try:
            ealias = aliased(UserSettings)
            result = session.query(ealias.file_name, ealias.created_time)\
                .filter(ealias.user_id == user_id).filter(ealias.user_settings_type == settings_type).all()
            print(result)
            return {"pdf1": "Success", "pdf2": result}
        except Exception as e:
            print(e)
            return {"pdf1": "Failure", "pdf2": "Error occurred while getting settings history from database"}
