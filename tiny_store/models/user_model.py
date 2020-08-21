from .base_model import BaseModel


class UserModel(BaseModel):

	def get_login_account_info(self, username, password):
		
		account_info = self.query_one("SELECT id, username, usertype FROM users WHERE username = '%s' AND password = '%s'" % (username, password))

		return account_info

	def check_duplicated_username(self, username):

		duplication = self.query_one("SELECT count(username) as duplication FROM users WHERE username = '%s'" % (username))
		
		return (duplication['duplication'] > 0)

	def register_ordinary_user(self, username, password, email):

		success = True

		try:
			self.execute_one("INSERT INTO users (id, username, password, email, usertype) VALUES ((SELECT uuid()), '%s', '%s', '%s', 0);" % (username, password, email))			
		except Exception as e:
			print(e)
			success = False

		return success	