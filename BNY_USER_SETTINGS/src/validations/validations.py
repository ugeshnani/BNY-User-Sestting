from src.database.user_settings_database import UserSettingDatabase


class Validations:
    @staticmethod
    def check_user_id_type(user_id, settings_type=''):
        try:
            user_database = UserSettingDatabase()
            result = user_database.check_user_id_type(user_id, settings_type)
            if len(result['Data']) > 0 and result["Status"] == "Success":
                return {"Status": 'Success'}
            elif result["Status"] == "Failure":
                return result
            else:
                return {"Status": "Failure", "Data": "Please enter valid user_id or type"}
        except Exception as e:
            print(e)
            return{"Status": "Failure", "Data": "Error occurred while validating user_id"}