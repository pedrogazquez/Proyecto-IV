from flask import Flask, session, redirect, url_for, escape, request, render_template
import sys, pydoc, os

app = Flask(__name__)

listUsers = []

@app.route('/users')
def showUsers():
	return 'Esta es la lista de usuarios registrados: ' + ',\n'.join(map(str,listUsers))

@app.route('/add/<username>')
def	addUser(username):
	listUsers.append(username)
	return 'Usuario registrado. Pruebe /users para ver los usuarios'

@app.route('/')
def index1():
        return render_template('index.html')

@app.route('/index.html')
def index():
	return render_template('index.html')
@app.route('/sobre.html')
def sobre():
	return render_template('sobre.html')
@app.route('/productos.html')
def produ():
	return render_template('productos.html')
@app.route('/servicios.html')
def servi():
	return render_template('servicios.html')
@app.route('/contacto.html')
def contac():
	return render_template('contacto.html')
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	
