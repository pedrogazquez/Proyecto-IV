install:
	sudo apt-get update && pip install -r requirements.txt

test:
	cd appGestionWeb && python test.py
