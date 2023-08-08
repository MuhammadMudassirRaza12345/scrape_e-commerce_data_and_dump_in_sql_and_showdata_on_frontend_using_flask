import pymysql
from pymysql import cursors
 

def create_connection():
    connection = pymysql.connect(host='127.0.0.1',
                            user='root',
                            password='',
                            database='bgaller_db',
                            cursorclass=pymysql.cursors.DictCursor)
    return connection    

connection = create_connection()

query = '''
        CREATE TABLE if not exists bgallery_tables ( 
    `id` int IDENTITY(101, 1) AUTO_INCREMENT PRIMARY KEY,
    `product_name` varchar(255) NOT NULL,
    `product_price` varchar(255) NOT NULL,
    `discount_price` varchar(255) NOT NULL,
    `product_image` varchar(1024) NOT NULL);
    '''
 
# # Now execute query
with connection:
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cursor.execute(query)
    connection.commit()
 

# # to start with insert record first create  connection:
# # connection = create_connection()
def insert(data):
    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO `bgallery_tables` (`product_name`,`product_price`,`discount_price,product_image`) VALUES  (%s,%s,%s,%s) "
            cursor.executemany(query,data)
            connection.commit()


 
