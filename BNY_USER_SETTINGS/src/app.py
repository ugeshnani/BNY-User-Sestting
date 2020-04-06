from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.services.user_setting_services import UserSettingService
from flask_cors import CORS

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ugesh@1995@localhost:5432/BNY'
db = SQLAlchemy(app)
CORS(app)

@app.route("/")
def start():
    return "Welcome to home page"


@app.route('/save_settings', methods=['POST', 'OPTIONS'])
def save_settings():
    user_id = request.args.get('user_id')
    settings_type = request.args.get('type')
    content = request.args.get('content')
    con = json.loads(content)
    user_service = UserSettingService()
    result = user_service.save_settings(user_id, settings_type, con)
    return jsonify(result)


@app.route('/get_settings', methods=['GET'])
def get_settings():
    user_id = request.args.get('user_id')
    settings_type = request.args.get('type')
    user_service = UserSettingService()
    result = user_service.get_settings(user_id, settings_type)
    return jsonify(result)


@app.route('/settings_history', methods=['GET'])
def settings_history():
    user_id = request.args.get('user_id')
    settings_type = request.args.get('type')
    user_service = UserSettingService()
    result = user_service.settings_history(user_id, settings_type)
    return jsonify(result)


if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(host="10.80.9.229", port=6008, debug=False)
