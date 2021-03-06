## Proyecto Infraestructura Virtual##
Pedro Gázquez Navarrete, repositorio creado para la realización del proyecto de Infraestructura Virtual el cual realizaré junto al de la asignatura DAI.

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://webgestion.herokuapp.com/)

[![Build Status](https://snap-ci.com/pedrogazquez/Proyecto-IV/branch/master/build_image)](https://snap-ci.com/pedrogazquez/Proyecto-IV/branch/master)

[![Build Status](https://travis-ci.org/pedrogazquez/Proyecto-IV.svg?branch=master)](https://travis-ci.org/pedrogazquez/Proyecto-IV)

##Descripción##
El proyecto ha realizar en esta asignatura será la de hacer la Infraestructura Virtual para el proyecto que voy a realizar en DAI ya que también tengo cursada esa asignatura. Este proyecto de DAI se realizará en el lenguaje de programación Python.
##Explicación##
Ya que aún no sé en que consistirá mi proyecto de DAI no puedo proporcionar la explicación de qué tipo de proyecto realizaré, no obstante, cuando sepa que hacer actualizaré este apartado pero dado que para DAI se realizará una aplicación web se necesitarán varios servidores y quizá un balanceador para dar soporte de infraestructura virtual a dicha aplicación.


# Integración Continua

[![Build Status](https://travis-ci.org/pedrogazquez/Proyecto-IV.svg?branch=master)](https://travis-ci.org/pedrogazquez/Proyecto-IV)

[Aquí el enlace a mi proyecto](https://github.com/pedrogazquez/Proyecto-IV). 


Para realizar los tests de mi proyecto he usado la libreria de unittest de python. Son tests flexibles y muy usados en este lenguaje. Los tests que he realizado los he integrado dentro de las herramientas de construcción, incluyendo un objetivo make test en [mi makefile](https://github.com/pedrogazquez/Proyecto-IV/blob/master/makefile). Para configurar el sistema de integración continua de forma que lance los tests automáticamente he usado Travis-CI y Shippable.

##Shippable
He creado mi archivo [shippable.yml](https://github.com/pedrogazquez/Proyecto-IV/blob/master/shippable.yml) una vez registrado en la página de Shippable y autorizado para que realicen los tests automáticamente. Como se puede ver en la siguiente imagen se realiza todo correctamente.
![shippable](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/ship_zpskdghgjx4.png)


##Travis
Como he hecho con el anterior he creado mi archivo [travis.yml](https://github.com/pedrogazquez/Proyecto-IV/blob/master/.travis.yml), igual que antes registrado con github previamente. Una vez hecho estó como se puede ver en la siguiente imagen el resultado de los tests es positivo:
![travis](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/trav_zpshehbyrb0.png)

# Despliegue de mi aplicación en un PaaS/SaaS: Heroku
He añadido varias funcionalidades a mi app, como base de datos con Mongo, formularios, sesiones para cada usuriao y varios templates distintos. Para desplegar mi app en Heroku, he tenido que definir mi archivo [Procfile](https://github.com/pedrogazquez/Proyecto-IV/blob/master/Procfile) y el que ya tenía que también es necesario de [requirements.txt](https://github.com/pedrogazquez/Proyecto-IV/blob/master/requirements.txt):

He subido la aplicación a Heroku, [la he llamado webgestion](https://webgestion.herokuapp.com/). Para ello lo que he hecho ha sido, primero registrarme en heroku, después he clonado mi repositorio donde guardo la aplicación. Lo proximo que hay que hacer es teclear las siguientes órdenes en el terminal dentro del repositorio de nuestra aplicación que hemos clonado:
```
heroku create
git push heroku master
```
Con heroku create, si no le indicamos nada, nos crea la app con un nombre aleatorio, que en mi caso ha sido [warm-sands-2560](https://warm-sands-2560.herokuapp.com/).
Lo proximo que he hecho ha sido crear un proceso de integración contínua junto al despliegue automático tanto en Heroku como en Snap CI. Para realizarlo en heroku, al conectarlo con GitHub debes aceptar la siguiente ventana emergente:

![heroku123](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20005315_zpssvdmjoei.png)

Una vez hecho esto, habilitamos que no despliegue hasta que no pase los tests para la IC:

![ic](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20005451_zpsca57kxdz.png)

Como se puede ver en la imagen el proceso de intregración continua está correctamente configurado.
Otra opción es hacerlo con Snap CI, en el cual debes conectarte con GitHub y aceptar las condiciones:

![snap](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20003846_zpspefwdnws.png)

Y por último, podemos comprobar que también está correctamente configurado el proceso de IC con Snap CI:

![snap1222](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20004423_zpsqfhzcdku.png)

# DOCKER: Entorno de pruebas.

Lo primero que he hecho para crear la imagen, es crear el fichero [Dockerfile](https://github.com/pedrogazquez/Proyecto-IV/blob/master/Dockerfile) el cual contiene lo siguiente:
```
FROM ubuntu:latest

#Autor
MAINTAINER Pedro Gazquez Navarrete <pedrogazqueznavarrete@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar app
RUN sudo apt-get install -y git
RUN git clone https://github.com/pedrogazquez/Proyecto-IV.git

#Instalar python
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y build-dep python-imaging --fix-missing
RUN sudo apt-get -y install libffi-dev
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo apt-get -y install python2.7
RUN sudo easy_install pip
RUN sudo easy_install Pillow
RUN sudo pip install --upgrade pip

#Instalar app
RUN cd Proyecto-IV && make install
```
He tenido un problema con la criptografía de python y tras mucho buscar e indagar lo he solucionado instalando el paquete **libffi-dev**.

Luego me he registrado en la web de [hub.docker](https://hub.docker.com/) y he autorizado a la aplicación para que se conecte a GitHub para así conectar el repositorio de mi proyecto para crear la imagen:

![imgAutoriza](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-12-05%20135317_zpsjamrchxm.png)

[Aqui esta mi imagen de docker](https://hub.docker.com/r/pedrogazquez/proyecto-iv/) y en la siguiente captura muestro la construcción automática de esta creando un "Automated Build" sobre el repositorio de mi proyecto de GitHub:

![DockerHub](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-12-10%20133939_zpsxdwwnyfs.png)

## Entorno de pruebas Docker en local

Para realizar esto en [mi makefile](https://github.com/pedrogazquez/Proyecto-IV/blob/master/Makefile) he añadido las ordenes necesarias para crear el entorno, estas se llevan a cabo mediante make docker, que contiene:

```
	sudo apt-get update
 	sudo apt-get install -y docker.io
 	sudo docker pull pedrogazquez/proyecto-iv
 	sudo docker run -t -i pedrogazquez/proyecto-iv /bin/bash
 	
```

En las siguientes capturas muestro como se lleva a cabo la ejecución de los dos últimos comandos y como se lleva a cabo la ejecución de la app desde el contenedor local de Docker:

![captu1](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-12-10%20143906_zpsyzjp3w8p.png)

![captu2](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-12-10%20143906_zpsyzjp3w8p.png)

En estas capturas la ejecución la he hecho mediante el comando python y la app pero también se puede llevar a cabo con make run.

##Inscripción en el certamen de Proyectos Libres de la UGR 2015-2016##
Aquí adjunto la imagen de la inscripción realizada correctamente en el Certamen:

![Inscripción](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/InscripcionUGR_zpsgkjszv6h.png)

