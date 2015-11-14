import unittest
from formu import register
from HTMLParser import HTMLParser

ini_html = 0
fin_html = 0
hay_css = 0
hay_form = 0
html_css = ""
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

class TestStringMethods(unittest.TestCase):
	
	def test_comprobarformu(self):
		global hay_form
		hay_form = 0
		parser = ComprobarEtiquetas()
		html_registro=register()
		parser.feed(html_registro)
		self.assertEqual(hay_form,1)


	# def test_comprobarHTML(self):
		# global ini_html
		# ini_html = 1
		# parser = ComprobarEtiquetas()
		# html_index = index()
		# parser.feed(html_index)
		# self.assertEqual(ini_html,1)

	def test_comprobarCSS(self):
		global hay_css
		global html_css
		hay_css = 1
		parser = ComprobarEtiquetas()
		html_css=register()
		parser.feed(html_css)
		self.assertEqual(hay_form,1)


if __name__ == '__main__':
    unittest.main()
