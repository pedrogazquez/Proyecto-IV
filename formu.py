from wtforms import *
from flask import Flask, session, redirect, url_for, escape, request, render_template
import sys, pydoc
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
#Expresion regular para que el numero de VISA sea corecto
regVISA='(\d\d\d\d)[ \-](\d\d\d\d)[ \-](\d\d\d\d)[ \-](\d\d\d\d)$'
listUsers = []
listSurna = []

class ComprobarEtiquetas(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global ini_html
		global hay_css
		global hay_form
		if tag=='html':
			ini_html = 1
		for attr in attrs:
			if (attr[0] == 'href' and attr[1] == '/static/style.css'):
				hay_css = 1
		for attr in attrs:
			if (attr[0] == 'method' and attr[1] == 'post'):
				hay_form = 1
	def handle_endtag(self, tag):
		global fin_html
		if tag=='html':
			fin_html = 1

class RegistrationForm(Form):
	username = TextField('Nombre: ', [validators.Length(min=4, max=25)])
	userap = TextField('Apellidos: ', [validators.Length(min=4, max=50)])
	email = TextField('Correo electronico', [validators.Length(min=6, max=35),validators.Required(),validators.Email(message='El email es incorrecto')])
	visaNum = TextField('Numero de VISA', [validators.Length(min=6, max=35),validators.Required(),validators.Regexp(regVISA, flags=0, message='Numero de VISA incorrecto')])
	nacimiento = DateField('Fecha de nacimiento: ', format='%Y-%m-%d')
	direccion = TextField('Direccion: ', [validators.Length(min=6, max=60)])
	password = PasswordField('Contrasenia', [validators.Required(),validators.EqualTo('confirm', message='La contrasenia debe coincidir con la repeticion')])
	confirm = PasswordField('Repite la contrasenia')
	accept_tos = BooleanField('Acepto las condiciones', [validators.Required()])
	formaPago = SelectField(u'Forma de pago', choices=[('contra', 'Contra reembolso'), ('visa', 'Tarjeta VISA')])

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		return('Gracias %s por registrarte!' % form.username.data)
	return render_template('register.html', form=form)

@app.route('/users')
def showUsers():
	return 'Esta es la lista de usuarios registrados: ' + ',\n'.join(map(str,listUsers))

@app.route('/add/<username>')
def	addUser(username):
	listUsers.append(username)
	return 'Usuario registrado. Pruebe /users para ver los usuarios'

@app.route('/')
def index():
	form = RegistrationForm(request.form)
	return render_template('index.html', form=form)
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	
