from tiny_store import tiny_store_app


ADMIN_USERTYPE = 1
DEFAULT_USERTYPE = 0
DB_CONFIG_KEYS = ['MYSQL_HOST', 'MYSQL_PORT', 'MYSQL_DB', 'MYSQL_USER', 'MYSQL_PASSWORD']
DB_CONFIG = {key: tiny_store_app.config[key] for key in DB_CONFIG_KEYS}

MIN_PASSWORD_LENGTH = 5

GRID_PER_ROW = 3