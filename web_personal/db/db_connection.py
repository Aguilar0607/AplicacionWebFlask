import pymysql

def get_connection():
    connection = pymysql.connect(host = 'localhost',
                                user = 'root',
                                password = 'class',
                                db = 'web_personal',
                                cursorclass=pymysql.cursors.DictCursor)

    return connection