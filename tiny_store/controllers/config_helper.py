import yaml
import os

from datetime import timedelta


class ConfigHelper(object):

	def __init__(self):

		pass

	def _get_key_from_env_var(self, key_name):

		return os.environ[key_name]

	def get_yaml_config_from_file(self, file_path):

		with open(file_path, 'r', encoding="utf-8") as pfile:
			yaml_config = yaml.load(pfile, Loader=yaml.FullLoader)

		return yaml_config

	def set_config_to_app(self, app, config_dict):

		for config_key, config_value in config_dict.items():
			app.config[config_key] = config_value

		return app

	def get_configs(self, yaml_file_path=None):

		try:
			yaml_config = self.get_yaml_config_from_file(yaml_file_path)
		except Exception as e:
			print(e)
			raise IOError('error when reading from yaml file')

		app_config = {}
		db_config = {}

		db_config['MYSQL_HOST'] = self._get_key_from_env_var('MYSQL_HOST')
		db_config['MYSQL_DB'] = self._get_key_from_env_var('MYSQL_DB')
		db_config['MYSQL_PORT'] = int(self._get_key_from_env_var('MYSQL_PORT'))

		db_config['MYSQL_USER'] = self._get_key_from_env_var('MYSQL_USER')
		db_config['MYSQL_PASSWORD'] = self._get_key_from_env_var('MYSQL_PASSWORD')

		flask_debug_mode = yaml_config['flask_debug']
		app_config['DEBUG'] = flask_debug_mode
		if flask_debug_mode:
			app_config['JINJA_ENV_AUTO_RELOAD'] = True
		else:
			app_config['JINJA_ENV_AUTO_RELOAD'] = False		
		app_config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=yaml_config['flask_static_file_max_age'])
		app_config['FLASK_APP_KEY'] = self._get_key_from_env_var('FLASK_APP_KEY')

		return app_config, db_config