import unittest
import os
import webGestion
from HTMLParser import HTMLParser
import tempfile
from html5lib.sanitizer import HTMLSanitizerMixin

eti_html = 0
img = 0

class ComprobarEtiquetas(HTMLParser):
    def handle_starttag(self, tag, attrs):
		global eti_html
		global img
		if tag=='html':
			eti_html = 1
		if tag=='img':
			img = 1
	
class TestMethods(unittest.TestCase):
	def setUp(self):
		self.db_fd, webGestion.app.config['DATABASE'] = tempfile.mkstemp()
		webGestion.app.config['TESTING'] = True
        	self.app = webGestion.app.test_client()

    	def tearDown(self):
        	os.close(self.db_fd)
        	os.unlink(webGestion.app.config['DATABASE'])
		
	def test_imagen(self):
		global img
		img = 0
		parser = ComprobarEtiquetas()
		archi_index= self.app.get('/index.html')
		assert 'html' in archi_index.data
	
	def test_htmlindex(self):
		global eti_html
		eti_html = 0
		parser = ComprobarEtiquetas()
		archi_index= self.app.get('/index.html')
		assert 'div' in archi_index.data

	def test_usuario(self):
		global img
		img = 0
		parser = ComprobarEtiquetas()
		archi_index= self.app.get('/index.html')
		assert 'h1' in archi_index.data

if __name__ == '__main__':
    unittest.main()

