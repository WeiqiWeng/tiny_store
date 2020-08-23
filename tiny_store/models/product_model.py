from .base_model import BaseModel


class ProductModel(BaseModel):

	DEFAULT_PRODUCT_GROUP_ID = 0

	def _get_products_by_group_id(self, group_id):

		query = """
			SELECT 
				b.productName, 
				b.manufacturer, 
				b.price, 
				b.imageURL 
			FROM
				groupIdToProductIdMappings a
			INNER JOIN
				products b
			ON
				a.productId = b.productId
			WHERE
				a.productGroupId = %d
		"""

		products = self.query_many(query % group_id)

		return products

	def get_default_products(self):
				
		return self._get_products_by_group_id(self.DEFAULT_PRODUCT_GROUP_ID)

	def get_personalized_products_by_user_id(self, user_id):

		query = """
			SELECT 
				c.productName, 
				c.manufacturer, 
				c.price, 
				c.imageURL 
			FROM
				userIdToProductGroupIdMappings a
			INNER JOIN	
				groupIdToProductIdMappings b
			ON
				a.productGroupId = b.productGroupId
			INNER JOIN
				products c
			ON
				b.productId = c.productId
			WHERE
				a.userId = '%s' AND
				a.productGroupId != %d
		"""

		products = self.query_many(query % (user_id, self.DEFAULT_PRODUCT_GROUP_ID))

		return products