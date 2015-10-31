install:
	sudo apt-get update && pip install -r requirements.txt

test:
	python test.py
