FROM ubuntu:latest

#Autor
MAINTAINER Pedro Gazquez Navarrete <pedrogazqueznavarrete@gmail.com>


RUN sudo apt-get -y update
RUN sudo apt-get install -y git
RUN git clone https://github.com/pedrogazquez/Proyecto-IV.git

RUN sudo apt-get install libpython2.7-dev
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

RUN cd Proyecto-IV && make install
