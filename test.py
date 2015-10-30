import unittest
import flask
from ej3 import mostrarPerfilUsuario
from HTMLParser import HTMLParser

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
class TestStringMethods(unittest.TestCase):

  def test_comprobarHTML(self):
		global ini_html
		ini_html = 1
		parser = ComprobarEtiquetas()
		mostrarPerfilUsuario('pedro')
		self.assertEqual(ini_html,1)

  def test_comprobarCSS(self):
		global hay_css
		hay_css = 1
		parser = ComprobarEtiquetas()
		mostrarPerfilUsuario('pepe')
		self.assertEqual(hay_css,1)

if __name__ == '__main__':
    unittest.main()
