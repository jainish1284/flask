from project.com.dao import con_db


class RegisterDAO:

    def insert_data(self, firstname, lastname, username, password):
        con_db_obj = con_db()
        cursor = con_db_obj.connection.cursor()
        cursor.execute('''Insert into register_master_mvc (firstname, lastname, username, password) 
        values(%s, %s, %s, %s)''', (firstname, lastname, username, password))
        cursor.connection.commit()
        cursor.close()

    def search_data(self, id=None):
        con_db_obj = con_db()
        cursor = con_db_obj.connection.cursor()
        if id is not None:
            cursor.execute('select * from register_master_mvc where id=%s', str(id))
            return_data = cursor.fetchone()
        else:
            cursor.execute('select * from register_master_mvc')
            return_data = cursor.fetchall()
        cursor.close()
        return return_data

    def update_data(self, firstname, lastname, username, password, id):
        con_db_obj = con_db()
        cursor = con_db_obj.connection.cursor()
        cursor.execute('''update register_master_mvc set firstname=%s, lastname=%s, username=%s, password=%s 
        where id=%s''', (firstname, lastname, username, password, id))
        cursor.connection.commit()
        cursor.close()

    def delete_data(self, id):
        con_db_obj = con_db()
        cursor = con_db_obj.connection.cursor()
        cursor.execute('delete from register_master_mvc where id=%s', id)
        cursor.connection.commit()
        cursor.close()
