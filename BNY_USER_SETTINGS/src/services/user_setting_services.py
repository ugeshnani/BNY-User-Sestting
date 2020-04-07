import json
from src.database.user_settings_database import UserSettingDatabase
from src.models.user_settings_model import UserSettings
from src.validations.validations import Validations

validations = Validations()
user_database = UserSettingDatabase()


class UserSettingService:

    @staticmethod
    def save_settings(user_id, settings_type, content):
        try:
            file_name = content['file_name']
            result = user_database.check_file_name(user_id, settings_type, file_name)
            print(result)
            if result["Data"] is not None and result["Status"] == "Success":
                file_name_data = result['Data']
                db_file_name = file_name_data.file_name
                new_db_file_name = db_file_name.replace(".csv", '')
                file_name_list = new_db_file_name.split('--')
                file_version = float(file_name_list[1])+0.1
                new_file_name = file_name.replace(".csv", "--"+str(file_version)+".csv")
                print(new_file_name)
                user_setting = UserSettings(user_id, settings_type, json.dumps(content).encode('utf-8'), new_file_name)
            elif result['Status'] == 'Failure':
                return result
            else:
                new_file_name = file_name.replace(".csv", "--1.0.csv")
                user_setting = UserSettings(user_id, settings_type, json.dumps(content).encode('utf-8'), new_file_name)
            result = user_database.save_settings(user_setting)
            return result
        except Exception as e:
            print(e)
            return {"Status": "Failure", "Data": "Error occurred while save settings in service"}

    @staticmethod
    def get_settings(user_id, settings_type):
        try:
            validations_result = validations.check_user_id_type(user_id, settings_type)
            if validations_result["Status"] == "Success":
                result = user_database.get_settings(user_id, settings_type)
                res_dict = {}
                if result["Status"] == "Success":
                    for contents in result['Data']:
                        res_dict = json.loads(contents.decode('utf-8'))
                    return {"Status": "Success", "Data": res_dict}
                else:
                    return result
            else:
                return validations_result
        except Exception as e:
            print(e)
            return {"Status": "Failure", "Data": 'Error occurred while get settings in service'}

    @staticmethod
    def settings_history(user_id, settings_type):
        try:
            validations_result = validations.check_user_id_type(user_id, settings_type)
            if validations_result["Status"] == "Success":
                result = user_database.settings_history(user_id, settings_type)
                if result["Status"] == "Success":
                    data = {'user_id': user_id, 'type': settings_type, 'history': result['Data']}
                    return {"Status": "Success", "Data": data}
                else:
                    return result
            else:
                return validations_result
        except Exception as e:
            print(e)
            return {"Status": "Failure", "Data": 'Error occurred while get settings_history in service'}

    @staticmethod
    def get_settings_list(user_id):
        try:
            validations_result = validations.check_user_id_type(user_id)
            if validations_result["Status"] == "Success":
                result = user_database.get_settings_list(user_id)
                if result["Status"] == "Success":
                    return {"Status": "Success", "Data": result["Data"]}
                else:
                    return result
            else:
                return validations_result
        except Exception as e:
            print(e)
            return {"Status": "Failure", "Data": 'Error occurred while get settings list in service'}
