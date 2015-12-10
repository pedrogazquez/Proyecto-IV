install:
	sudo apt-get update
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

test:
	cd appGestionWeb && python test.py
	
run:
	cd appGestionWeb && python webGestion.py
docker: 
	sudo apt-get update
 	sudo apt-get install -y docker.io
 	sudo docker pull pedrogazquez/proyecto-iv
 	sudo docker run -t -i pedrogazquez/proyecto-iv /bin/bash
