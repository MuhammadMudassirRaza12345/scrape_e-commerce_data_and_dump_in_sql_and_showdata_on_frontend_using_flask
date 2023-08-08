import pymysql
from pymysql import cursors
 

# from app3 import data

# print(data)
# before this go to mysql and create database named daraz_db amd 
# DROP TABLE new_names;  



def create_connection():
    connection = pymysql.connect(host='127.0.0.1',
                            user='root',
                            password='',
                            database='daraz_db',
                            cursorclass=pymysql.cursors.DictCursor)
    return connection    

connection = create_connection()

# create new table using execute command
# table query

# -- SELECT * FROM daraz_db.daraz_tables; 

# --  Alter table daraz_tables modify id INT NOT NULL   AUTO_INCREMENT;
#  desc daraz_tables
#  `id` int(9) NOT NULL AUTO_INCREMENT ,
#     `name` varchar(255) NOT NULL,
# 	`product_image_url` varchar(1024) NOT NULL,
# 	`product_original_price` varchar(255) NOT NULL,
# 	`discount` varchar(255) NOT NULL,
# 	`product_current_price` varchar(255) NOT NULL,
# 	`productUrl` varchar(1024) NOT NULL,
	
    # PRIMARY KEY (`id`)
query = '''
       CREATE TABLE if not exists daraz_tables ( 
    `id` int NOT NULL AUTO_INCREMENT  PRIMARY KEY  ,
    `name` varchar(255) NOT NULL,
	`product_image_url` varchar(1024) NOT NULL,
	`product_original_price` varchar(255) NOT NULL,
	`discount` varchar(255) NOT NULL,
	`product_current_price` varchar(255) NOT NULL,
	`productUrl` varchar(1024) NOT NULL); 
    '''

# query = '''CREATE TABLE IF NOT EXIST `daraz_tables` (
   
# ) ENGINE=InnoDB
# AUTO_INCREMENT=1 ;'''


# # Now execute query
with connection:
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cursor.execute(query)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

# # Now insert the data into table
# from app3 import data

# # i have already data in tuple format

# print(data)

# # to start with insert record first create  connection:
# # connection = create_connection()
def insert(data):
    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO `daraz_tables` (`id`,`name`,`product_image_url`,`product_original_price`, `discount`,`product_current_price`, `productUrl`) VALUES  (%s, %s, %s,%s, %s, %s, %s) "
            cursor.executemany(query, data)
            connection.commit()


# connection = create_connection()
