from tiny_store import tiny_store_app, app_config


if __name__ == '__main__':

	tiny_store_app.run(debug=app_config['DEBUG'])