import pymysql


class BaseModel(object):

	def __init__(self, db_config):

		self.mysql_connection, self.cursor = self.connect_to_database(db_config)		

	def connect_to_database(self, db_config):

		connection = pymysql.connect(
			host=db_config["MYSQL_HOST"],
			port=db_config["MYSQL_PORT"],
			user=db_config["MYSQL_USER"],
			passwd=db_config["MYSQL_PASSWORD"],
			db=db_config["MYSQL_DB"],
			charset='utf8'
		)

		cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

		return connection, cursor

	def query_one(self, query):

		self.cursor.execute(query)
		result = self.cursor.fetchone()
		return result

	def query_many(self, query):

		self.cursor.execute(query)
		result = self.cursor.fetchall()
		return result

	def execute_one(self, query):

		self.cursor.execute(query)
		self.mysql_connection.commit()

	def execute_many(self, query):

		self.cursor.executemany(query)
		self.mysql_connection.commit()

	def close(self):
		self.cursor.close()
		self.mysql_connection.close()

	def execute_one_with_boolean_return(self, query):

		success = True
		try:
			self.execute_one(query)
		except Exception as e:
			print(e)
			success = False

		return success

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()

