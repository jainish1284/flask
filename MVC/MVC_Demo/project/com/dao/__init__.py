import pymysql

def con_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb',
        cursorclass = pymysql.cursors.DictCursor
    )
