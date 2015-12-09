FROM debian

RUN apt-get install -y git
RUN apt-get install -y build-essential
RUN git clone https://github.com/pedrogazquez/Proyecto-IV.git
RUN cd Proyecto-IV && git pull
RUN cd Proyecto-IV && make install
