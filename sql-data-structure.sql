CREATE TABLE
"auth_user" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password" varchar(128) NOT NULL,
	"last_login" datetime NULL,
	"is_superuser" bool NOT NULL,
	"username" varchar(150) NOT NULL UNIQUE,
	"last_name" varchar(150) NOT NULL,
	"email" varchar(254) NOT NULL,
	"is_staff" bool NOT NULL,
	"is_active" bool NOT NULL,
	"date_joined" datetime NOT NULL,
	"first_name" varchar(150) NOT NULL
)

-- DROP TABLE "auth_user"

-- table RENAME
-- ALTER TABLE table_name RENAME TO new_table_name;

-- add new column
ALTER TABLE auth_user ADD COLUMN "is_cool" bool DEFAULT True NOT NULL;

-- rename column
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;

-- delete column
ALTER TABLE auth_user DROP COLUMN is_cool;