from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'jainish'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskmysql'
mysql = MySQL(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('Select * from MyUsers')
    result = cursor.fetchall()
    session['results'] = result
    cursor.close()

    # return render_template('index.html', results=result)
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit_form():

    # firstname = request.args.get('first_name')
    # lastname = request.args.get('last_name')

    firstname = request.forms['firstname']
    lastname = request.forms['lastname']

    cursor = mysql.connection.cursor()
    cursor.execute('Insert into MyUsers values("{}","{}")'.format(firstname, lastname))
    cursor.connection.commit()
    cursor.close()
    return redirect('/')


if __name__ == '__main__':
    app.run()
