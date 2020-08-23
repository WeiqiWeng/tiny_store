USE `tiny_store`;

SET SQL_SAFE_UPDATES=0;

DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS products (	
  	productId INT unsigned NOT NULL AUTO_INCREMENT,
    productName VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    imageURL TEXT NOT NULL,
    PRIMARY KEY (productId)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO products (productName, manufacturer, price, imageURL) VALUES ('textbook', 'textbook_manufacturer', 28.88, 'https://img.alicdn.com/imgextra/i2/2523168234/TB2aRgeXXOWBuNjy0FiXXXFxVXa_!!2523168234.png');

INSERT INTO products (productName, manufacturer, price, imageURL) VALUES ('textbook1', 'textbook_manufacturer1', 23.00, 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3135065576,2368998984&fm=26&gp=0.jpg');

INSERT INTO products (productName, manufacturer, price, imageURL) VALUES ('textbook2', 'textbook_manufacturer2', 38.99, 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1811570007,3966066128&fm=26&gp=0.jpg');

INSERT INTO products (productName, manufacturer, price, imageURL) VALUES ('textbook3', 'textbook_manufacturer3', 17.00, 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1598080750113&di=e3594af60c23150034a515bbba13fcc7&imgtype=0&src=http%3A%2F%2Fimg11.360buyimg.com%2Fn0%2Fjfs%2Ft7426%2F315%2F1274976902%2F97089%2F9796496c%2F599bceffNdf6c05e7.jpg');

SELECT * FROM products;

DROP TABLE IF EXISTS groupIdToProductIdMappings;

CREATE TABLE IF NOT EXISTS groupIdToProductIdMappings (
	productGroupId INT unsigned NOT NULL,
  	productId INT unsigned NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SELECT * FROM groupIdToProductIdMappings;

INSERT INTO groupIdToProductIdMappings (productGroupId, productId) VALUES (0, 1);
INSERT INTO groupIdToProductIdMappings (productGroupId, productId) VALUES (0, 2);
INSERT INTO groupIdToProductIdMappings (productGroupId, productId) VALUES (0, 4);

INSERT INTO groupIdToProductIdMappings (productGroupId, productId) VALUES (1, 3);
INSERT INTO groupIdToProductIdMappings (productGroupId, productId) VALUES (1, 4);
INSERT INTO groupIdToProductIdMappings (productGroupId, productId) VALUES (1, 1);

DELETE FROM groupIdToProductIdMappings WHERE productGroupId = 1;


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
				a.userId = 'd491d8d0-e2f3-11ea-bd67-4a8ad69052e6' AND
                a.productGroupId != 0

