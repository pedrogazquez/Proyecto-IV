from wtforms import *
from flask import Flask, session, redirect, url_for, escape, request, render_template
import sys, pydoc
from HTMLParser import HTMLParser

app = Flask(__name__)

@app.route('/')
def index():
	form = RegistrationForm(request.form)
	return render_template('index.html', form=form)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)  # 0.0.0.0 para permitir conexiones desde cualquier sitio. Ojo, peligroso en modo debug

	
