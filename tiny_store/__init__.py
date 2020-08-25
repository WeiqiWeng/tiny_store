from flask import Flask
from tiny_store.controllers import ConfigHelper

import os


config_helper = ConfigHelper()
tiny_store_app = Flask(__name__)
config_file_path = os.path.join(os.getcwd(), 'tiny_store/config.yml')
app_config, db_config = config_helper.get_configs(yaml_file_path=config_file_path)

tiny_store_app.jinja_env.auto_reload = app_config['JINJA_ENV_AUTO_RELOAD']
tiny_store_app.secret_key = app_config['FLASK_APP_KEY']

tiny_store_app = config_helper.set_config_to_app(tiny_store_app, db_config)


from tiny_store.controllers import homepage_controller, user_controller, product_controller, admin_controller
