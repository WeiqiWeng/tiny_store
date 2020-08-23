USE `tiny_store`;

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
	id varchar(36) NOT NULL,
  	username varchar(50) NOT NULL,
  	password varchar(50) NOT NULL,
  	email varchar(50) NOT NULL,
    usertype tinyint(1) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO users (id, username, password, email, usertype) VALUES ('c0558f7a-e216-11ea-a0fd-cc37b0ccef47', 'root', 'root2020', 'root@tinystore.com', 1);

-- select uuid()

SELECT * FROM users LIMIT 10;

DELETE FROM users WHERE id IS NULL;

SELECT uuid();

INSERT INTO users (id, username, password, email, usertype) VALUES ('d491d8d0-e2f3-11ea-bd67-4a8ad69052e6', 'testuser', 'testuser', 'testuser@tinystore.com', 0);

INSERT INTO users (id, username, password, email, usertype) VALUES ((SELECT uuid()), 'aaa', 'aaa', 'root@tinystore.com', 0);

DROP TABLE IF EXISTS userIdToProductGroupIdMappings;

CREATE TABLE IF NOT EXISTS userIdToProductGroupIdMappings (
	userId varchar(36) NOT NULL,
  	productGroupId INT unsigned NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



SELECT * FROM userIdToProductGroupIdMappings;

INSERT INTO userIdToProductGroupIdMappings (userId, productGroupId) VALUES ('d491d8d0-e2f3-11ea-bd67-4a8ad69052e6', 0);

INSERT INTO userIdToProductGroupIdMappings (userId, productGroupId) VALUES ('d491d8d0-e2f3-11ea-bd67-4a8ad69052e6', 1);
