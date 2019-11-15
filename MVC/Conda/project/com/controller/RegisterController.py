from project import app, render_template, request, redirect
from project.com.dao.RegisterDAO import RegisterDAO


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_user():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']
    password = request.form['password']
    register_dao_obj = RegisterDAO()
    register_dao_obj.insert_data(firstname, lastname, username, password)
    return redirect('/')


@app.route('/search', methods=['GET'])
def display_user():
    register_dao_obj = RegisterDAO()
    return_data = register_dao_obj.search_data()
    return render_template('index.html', result=return_data)


@app.route('/update/<int:id>',methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'GET':
        register_dao_obj = RegisterDAO()
        return_data = register_dao_obj.search_data(id)
        return render_template('update.html', result=return_data)

    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        register_dao_obj = RegisterDAO()
        register_dao_obj.update_data(firstname, lastname, username, password, id)
        return redirect('/search')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    pass
