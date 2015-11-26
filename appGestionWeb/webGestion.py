# -*- encoding: utf-8 -*-

from wtforms import *
from flask import Flask, session, redirect, url_for, escape, request, render_template
import sys, pydoc, datetime
from HTMLParser import HTMLParser
from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
#Expresion regular para que el numero de VISA sea corecto
regVISA='(\d\d\d\d)[ \-](\d\d\d\d)[ \-](\d\d\d\d)[ \-](\d\d\d\d)$'
listUsers = []
client = MongoClient('mongodb://localhost:27017/')


class RegistrationForm(Form):
	username= TextField('Nombre: ', [validators.Length(min=4, max=25)])
	userap = TextField('Apellidos: ', [validators.Length(min=4, max=50)])
	email = TextField('Correo electronico', [validators.Length(min=6, max=35),validators.Required(),validators.Email(message='El email es incorrecto')])
	visaNum = TextField('Numero de VISA', [validators.Length(min=6, max=35),validators.Required(),validators.Regexp(regVISA, flags=0, message='Numero de VISA incorrecto')])
	nacimiento = DateField('Fecha de nacimiento (year-month-day): ', format='%Y-%m-%d')
	direccion = TextField('Direccion: ', [validators.Length(min=6, max=60)])
	password = PasswordField('Contrasenia', [validators.Length(min=8, max=90), validators.Required(),validators.EqualTo('confirm', message='La contrasenia debe coincidir con la repeticion')])
	confirm = PasswordField('Repite la contrasenia')
	accept_tos = BooleanField('Acepto las condiciones', [validators.Required()])
	formaPago = SelectField(u'Forma de pago', choices=[('contra', 'Contra reembolso'), ('visa', 'Tarjeta VISA')])

	
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		masvisitadas('/register')
		session['username'] = request.form['username']
		nombrecillo = escape(session['username'])
		db = client['test-database'] 
		post = {"Nombre": form.username.data, 
				"Apellidos": form.userap.data, 
				"Email": form.email.data}
		posts = db.posts
		post_id = posts.insert(post)
		if 'link1' in session:
			lamas = escape(session['link1'])
		if'link2' in session:
			lamas2 = escape(session['link2'])
		if'link3' in session:
			lamas3 = escape(session['link3'])
		return render_template('index.html', nombrecillo = escape(session['username']), lamas = escape(session['link1']), lamas2 = escape(session['link2']), lamas3 = escape(session['link3']))
	return render_template('register.html',form=form)

@app.route('/verMongo')
def verMongo():
	username = request.args.get('username')
	db = client['test-database'] 
	posts = db.posts
	salida = ''
	for post in posts.find({"Nombre": username}):
		salida = 'Nombre: '+(post['Nombre']) + '  Apellidos: '+(post['Apellidos']) +'  Email: '+ (post['Email'])
	return "<html><body><h1>%s <a href='index.html'>Volver a Home</a></h1></body></html>" % (salida)

@app.route('/index.html')
def index():
	if'username' in session:
		masvisitadas('/index.html')
		nombrecillo = escape(session['username'])
		if 'link1' in session:
			lamas = escape(session['link1'])
		if'link2' in session:
			lamas2 = escape(session['link2'])
		if'link3' in session:
			lamas3 = escape(session['link3'])
		return render_template('index.html', nombrecillo = escape(session['username']), lamas = escape(session['link1']), lamas2 = escape(session['link2']), lamas3 = escape(session['link3']))
	return render_template('index.html')

@app.route('/masvisitadas')
def masvisitadas(pagVis):
	if('link3' in session) or ('link2' in session):
		session['link3'] = session['link2']
		session['link2'] = session['link1']
		session['link1'] = pagVis
	elif'link1' in session:
		session['link2'] = session['link1']
		session['link1'] = pagVis
		session['link3'] = 'ninguna'
	else:
		session['link1'] = pagVis
		session['link2'] = 'ninguna'
		session['link3'] = 'ninguna'
		
@app.route('/productos.html')
def produ():
	if'username' in session:
		masvisitadas('/productos.html')
		nombrecillo = escape(session['username'])
		if 'link1' in session:
			lamas = escape(session['link1'])
		if'link2' in session:
			lamas2 = escape(session['link2'])
		if'link3' in session:
			lamas3 = escape(session['link3'])
		return render_template('productos.html', nombrecillo = escape(session['username']), lamas = escape(session['link1']), lamas2 = escape(session['link2']), lamas3 = escape(session['link3']))
	return render_template('productos.html')

@app.route('/contacto.html')
def contac():
	if'username' in session:
		masvisitadas('/contacto.html')
		nombrecillo = escape(session['username'])
		if 'link1' in session:
			lamas = escape(session['link1'])
		if'link2' in session:
			lamas2 = escape(session['link2'])
		if'link3' in session:
			lamas3 = escape(session['link3'])
		return render_template('contacto.html', nombrecillo = escape(session['username']), lamas = escape(session['link1']), lamas2 = escape(session['link2']), lamas3 = escape(session['link3']))
	return render_template('contacto.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
		return '''
		<form action="" method="post">
			<p><input type="text" name="username"/></p>
			<p><input type="submit" value="Login"/></p>
		</form>
		'''

@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'	

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)  # 0.0.0.0 para permitir conexiones desde cualquier sitio. Ojo, peligroso en modo debug
