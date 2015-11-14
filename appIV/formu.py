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

@app.route('/')
def index():
	form = RegistrationForm(request.form)
	return render_template('index.html', form=form)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)  # 0.0.0.0 para permitir conexiones desde cualquier sitio. Ojo, peligroso en modo debug

	
