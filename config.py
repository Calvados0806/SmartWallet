"this module contains configure settings for database"

DB_NAME = #point database name
USER = #point your user name
HOST = #point host of database
PASSWORD = #point password to your database

TABLES = dict()
TABLES["cash"] = (
	"CREATE TABLE `cash` ("
	"  `general` INT NOT NULL DEFAULT 0"
	") ENGINE=InnoDB"
)
TABLES["history"] = (
	"CREATE TABLE `history` ("
	"	`id` INT NOT NULL AUTO_INCREMENT,"
	"	`sum` INT NOT NULL DEFAULT 0,"
	"	`message` VARCHAR(30),"
	"	PRIMARY KEY (id)"
	") ENGINE=InnoDB"
)