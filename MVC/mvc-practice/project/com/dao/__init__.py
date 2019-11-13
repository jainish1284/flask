import project.com.dao.RegisterDAO
import pymysql


def con_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='flaskmysql',
        cursorclass=pymysql.cursors.DictCursor
    )
