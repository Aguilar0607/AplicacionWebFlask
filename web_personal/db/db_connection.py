import pymysql

def get_connection():
    connection = pymysql.connect(host = 'localhost',
                                user = 'root',
                                password = '',
                                db_name = 'web_personal',
                                cursor_class=pymysql.cursors.DictCursor)

    return conection