from .base_model import BaseModel
from .user_model import UserModel
from .product_model import ProductModel


class AdminModel(UserModel, ProductModel):

	def get_all_products(self):

		query = "SELECT productId, productName FROM products;"

		all_products = self.query_many(query)

		return all_products

	def get_all_groups(self):

		query = "SELECT productGroupId, description FROM productGroups;"

		all_groups = self.query_many(query)

		return all_groups

	def get_all_ordinary_users(self):

		query = "SELECT id, username FROM users WHERE usertype != 1;"

		all_users = self.query_many(query)

		return all_users

	def check_duplicated_product_id_to_group_id_mapping(self, group_id, product_id):

		query = """
			SELECT 
				count(productId) as duplication 
			FROM 
				groupIdToProductIdMappings 
			WHERE 
				productGroupId = %d AND
				productId = %d;
		"""

		duplication = self.query_one(query % (group_id, product_id))
		
		return (duplication['duplication'] > 0)

	def check_duplicated_user_id_to_group_id_mapping(self, group_id, user_id):

		query = """
			SELECT 
				count(userId) as duplication 
			FROM 
				userIdToProductGroupIdMappings 
			WHERE 
				productGroupId = %d AND
				userId = '%s';
		"""

		duplication = self.query_one(query % (group_id, user_id))
		
		return (duplication['duplication'] > 0)


	def add_product_id_to_group_id_mapping(self, group_id, product_id):

		query = "INSERT INTO groupIdToProductIdMappings (productGroupId, productId) VALUES (%d, %d);"
		return self.execute_one_with_boolean_return(query % (group_id, product_id))

	def add_user_id_to_group_id_mapping(self, group_id, user_id):

		query = "INSERT INTO userIdToProductGroupIdMappings (productGroupId, userId) VALUES (%d, '%s');"
		return self.execute_one_with_boolean_return(query % (group_id, user_id))

	def add_product_group(self, group_description):

		query = "INSERT INTO productGroups (description) VALUES ('%s');"
		return self.execute_one_with_boolean_return(query % (group_description))

