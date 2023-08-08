from flask import Flask ,jsonify 
import pymysql
from pymysql import cursors

 
 

app = Flask(__name__)
connection = pymysql.connect(host='127.0.0.1',
                            user='root',
                            password='mudassir786110',
                            database='daraz_db',
                            cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    query = "SELECT * FROM daraz_tables limit 10"
    cursor=connection.cursor()
    cursor.execute(query)
    data=cursor.fetchall() 
    return  jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)


#  python -m pip install "connexion[swagger-ui]==2.14.1"