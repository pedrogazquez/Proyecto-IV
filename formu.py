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
def index():
	return render_template('index.html')
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	
