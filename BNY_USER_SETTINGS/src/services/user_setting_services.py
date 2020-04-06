import json

from src.database.user_settings_database import UserSettingDatabase
from src.models.user_settings_model import UserSettings

user_database = UserSettingDatabase()


class UserSettingService:

    def save_settings(self, user_id, settings_type, content):
        try:
            file_name = content['file_name']
            result = user_database.check_file_name(user_id, settings_type, file_name)
            print(result)
            if result["pdf2"] is not None and result["pdf1"] == "Success":
                file_name_data = result['pdf2']
                db_file_name = file_name_data.file_name
                new_db_file_name = db_file_name.replace(".csv",'')
                file_name_list = new_db_file_name.split('--')
                file_version = float(file_name_list[1])+0.1
                new_file_name = file_name.replace(".csv", "--"+str(file_version)+".csv")
                print(new_file_name)
                user_setting = UserSettings(user_id, settings_type, json.dumps(content).encode('utf-8'), new_file_name)
            elif result['pdf2'] == 'Failure':
                return result
            else:
                new_file_name = file_name.replace(".csv","--1.0.csv")
                user_setting = UserSettings(user_id, settings_type, json.dumps(content).encode('utf-8'), new_file_name)
            result = user_database.save_settings(user_setting)
            return result
        except Exception as e:
            print(e)
            return {"pdf1":"Failure", "pdf2": "Error occurred while save settings in service"}

    def get_settings(self, user_id, settings_type):
        try:
            result = user_database.get_settings(user_id, settings_type)
            res_dict = {}
            if result["pdf1"] == "Success":
                for contents in result['pdf2']:
                    res_dict = json.loads(contents.decode('utf-8'))
                return {"pdf1":"Success", "pdf2": res_dict}
            else:
                return result
        except Exception as e:
            print(e)
            return {"pdf1":"Failure", "pdf2": 'Error occurred while get settings in service'}

    def settings_history(self, user_id, settings_type):
        try:
            result = user_database.settings_history(user_id, settings_type)
            data = {'user_id': user_id, 'type': settings_type, 'history': result}
            return {"pdf1":"Success","pdf2":data}
        except Exception as e:
            print(e)
            return {"pdf1":"Failure", "pdf2": 'Error occurred while get settings_history in service'}
