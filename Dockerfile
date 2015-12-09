FROM debian

#Autor
MAINTAINER Pedro Gazquez Navarrete <pedrogazqueznavarrete@gmail.com>

RUN sudo apt-get -y update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential
RUN git clone https://github.com/pedrogazquez/Proyecto-IV.git
RUN cd Proyecto-IV && git pull
RUN cd Proyecto-IV && make install
