FROM debian

RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential
RUN sudo git clone https://github.com/pedrogazquez/Proyecto-IV.git
RUN cd Proyecto-IV && git pull
RUN cd Proyecto-IV && make install
