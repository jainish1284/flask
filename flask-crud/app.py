from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskmysql'

mysql = MySQL(app)


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('Select * from register_master')
    result = cursor.fetchall()
    cursor.close()
    return render_template('index.html', results=result)


@app.route('/register', methods=['GET', 'POST'])
def register_user():

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        address = request.form['address']
        city = request.form['city']
        hobby = request.form.getlist('hobby')
        hobby = ', '.join(hobby)

        cursor = mysql.connection.cursor()
        cursor.execute('Insert into register_master (firstname, lastname, username, password, gender, address, city, hobby) values(%s, %s, %s, %s, %s, %s, %s, %s)', (firstname, lastname, username, password, gender, address, city, hobby))
        cursor.connection.commit()
        cursor.close()
        return redirect('/')

    else:
        return render_template('register.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('select * from register_master where id = {}'.format(id))
        result = cursor.fetchone()
        cursor.close()
        return render_template('update.html', result=result)

    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        address = request.form['address']
        city = request.form['city']
        hobby = request.form.getlist('hobby')
        hobby = ', '.join(hobby)

        cursor = mysql.connection.cursor()
<<<<<<< HEAD
        cursor.execute('update register_master set firstname = %s, lastname = %s, username = %s, password = %s, gender = %s, address = %s, city = %s, hobby = %s where id = %s', (firstname, lastname, username, password, gender, address, city, hobby, id))
=======
        cursor.execute('update register_master set firstname=%s, lastname=%s, username=%s, password=%s, gender=%s, address=%s, city=%s, hobby=%s where id=%s', (firstname, lastname, username, password, gender, address, city, hobby, id))
>>>>>>> 8303cbc1d98c1911675a2cdd2717b8bed51aa66e
        cursor.connection.commit()
        cursor.close()
        return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute('delete from register_master where id = {}'.format(id))
    cursor.connection.commit()
    cursor.close()
    return redirect('/')


if __name__ == '__main__':
    app.run()
