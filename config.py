"this module contains configure settings for database"

import os

DB_NAME = "SmartWallet"
USER = "root"
HOST = "127.0.0.1"
PASSWORD = os.environ["PASSWORD"]

TABLES = dict()
TABLES["cash"] = (
	"CREATE TABLE `cash` ("
	"  `balance` INT NOT NULL DEFAULT 0"
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