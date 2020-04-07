from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy_mptt.mixins import *
from src.models.user_settings_model import UserSettings

engine = create_engine('postgresql://postgres:Ugesh@1995@localhost:5432/BNY')
Session = sessionmaker(bind=engine)
session = Session()


class UserSettingDatabase:

    @staticmethod
    def save_settings(user_settings):
        try:
            session.add(user_settings)
            session.commit()
            return {"Status": "Success", "Data": "settings saved successfully"}
        except Exception as e:
            print(e)
            session.rollback()
            return {"Status": "Failure", "Data": "Error while saving the settings "}

    @staticmethod
    def check_file_name(user_id, settings_type, file_name):
        try:
            new_file_name = file_name.replace(".csv", '')
            search = "%{}%".format(new_file_name)
            result = session.query(UserSettings).filter(UserSettings.user_id == user_id,
                                                        UserSettings.user_settings_type == settings_type,
                                                        UserSettings.file_name.like(search)). \
                order_by(desc(UserSettings.created_time)).first()
            return {"Status": "Success", "Data": result}
        except Exception as e:
            print(e)
            session.rollback()
            return {"Status": "Failure", "Data": "Error occurred while checking file name in database"}

    @staticmethod
    def get_settings(user_id, settings_type):
        try:
            result = session.query(UserSettings.content).filter(UserSettings.user_id == user_id). \
                filter(UserSettings.user_settings_type == settings_type)\
                .order_by(desc(UserSettings.created_time)).first()
            return {"Status": "Success", "Data": result}
        except Exception as e:
            print(e)
            session.rollback()
            return {"Status": "Failure", "Data": "Error occurred while get settings from database"}

    @staticmethod
    def settings_history(user_id, settings_type):
        try:
            result = session.query(UserSettings.file_name, UserSettings.created_time) \
                .filter(UserSettings.user_id == user_id).filter(UserSettings.user_settings_type == settings_type).all()
            return {"Status": "Success", "Data": result}
        except Exception as e:
            print(e)
            session.rollback()
            return {"Status": "Failure", "Data": "Error occurred while getting settings history from database"}

    @staticmethod
    def check_user_id_type(user_id, settings_type):
        try:
            if settings_type == '':
                result = session.query(UserSettings).filter(UserSettings.user_id == user_id).all()
                print("Printing in check user_id and type")
                print(result)
                print(user_id)
                return {"Status": "Success", "Data": result}

            else:
                result = session.query(UserSettings) \
                    .filter(UserSettings.user_id == user_id)\
                    .filter(UserSettings.user_settings_type == settings_type).all()
                return {"Status": "Success", "Data": result}
        except Exception as e:
            print(e)
            session.rollback()
            return {"Status": "Failure", "Data": "Error occurred while check userId & type from database"}

    @staticmethod
    def get_settings_list(user_id):
        try:
            result = session.query(UserSettings.user_id, UserSettings.user_settings_type,
                                   UserSettings.file_name, UserSettings.created_time) \
                                    .filter(UserSettings.user_id == user_id).all()
            return {"Status": "Success", "Data": result}
        except Exception as e:
            print(e)
            session.rollback()
            return {"Status": "Failure", "Data": "Error occurred in get_settings_list from database"}
