from flask import Flask, session, redirect, url_for, escape, request
import sys, pydoc
from HTMLParser import HTMLParser
app = Flask(__name__)
""" Aplicacion con flask creada para la redireccion web segun la ruta escogida"""
pag_alu= '''
			<html>
				<head>
					<title>PAGINA DE ALUMNO</title>
				</head>

				<body>
					<h1>ALUMNO, hola PEDRO </h1>
					<img src="/static/pedro.jpg" height="42" width="42">
				</body>
			</html>
			'''
pag_profe= '''
			<html>
				<head>
					<title>PAGINA DE PROFESOR</title>
					<link href="/static/estilos.css" rel="stylesheet" type="text/css" />
				</head>
				<body>
					<h1>PROFESOR, hola PEPE </h1>
				</body>
			</html>
		'''
pag_usu= '''
			<html>
				<head>
					<title>PAGINA DE USUARIO SIN REGISTRAR</title>
				</head>
				<body>
					<h1>USUARIO SIN REGISTRAR, hola usuario anonimo </h1>
				</body>
			</html>
		'''

ini_html = 0
fin_html = 0
tipo_h1 = 0
hay_css = 0

class ComprobarEtiquetas(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global ini_html
		global tipo_h1
		global hay_css
		if tag=='html':
			ini_html = 1
		if tag=='h1':
			tipo_h1 += 1
		for attr in attrs:
			if (attr[0] == 'href' and attr[1] == '/static/estilos.css'):
				hay_css = 1
	def handle_endtag(self, tag):
		global fin_html
		global tipo_h1
		if tag=='html':
			fin_html = 1
		if tag=='h1':
			tipo_h1 += 1

@app.route('/user/<username>')
def mostrarPerfilUsuario(username):
    # Mostrar el perfil de usuario
	""" Esta funcion es la que depende del nombre de usuario especificado en la ruta, redirige a una pagina creada dependiendo si eres alumno, profesor o usuario sin registrar."""
	
	
	if username in ['pedro']:
		global ini_html
		ini_html = 0
		parser = ComprobarEtiquetas()
		parser.feed(pag_alu)
		assert (ini_html == 1 and fin_html == 1 and tipo_h1 == 2) 
		return pag_alu
	if username in ['pepe']:
		global hay_css
		hay_css = 0
		parser = ComprobarEtiquetas()
		parser.feed(pag_profe)
		assert hay_css == 1
		return pag_profe
	else:
		return pag_usu

@app.errorhandler(404)
def page_not_found(error):
    return '''
			<html>
				<head>
				<title>ERROR 404</title>
			</head>
			<body>
			<h1>ERROR INTRODUZCA UN NOMBRE DE USUARIO EN LA URL </h1>
			</body>
			</html>
		'''
		
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)  # 0.0.0.0 para permitir conexiones desde cualquier sitio. Ojo, peligroso en modo debug
