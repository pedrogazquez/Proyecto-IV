## Proyecto Infraestructura Virtual##
Pedro Gázquez Navarrete, repositorio creado para la realización del proyecto de Infraestructura Virtual el cual realizaré junto al de la asignatura DAI.

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://warm-sands-2560.herokuapp.com/)

[![Build Status](https://travis-ci.org/pedrogazquez/Proyecto-IV.svg?branch=master)](https://travis-ci.org/pedrogazquez/Proyecto-IV)

##Descripción##
El proyecto ha realizar en esta asignatura será la de hacer la Infraestructura Virtual para el proyecto que voy a realizar en DAI ya que también tengo cursada esa asignatura. Este proyecto de DAI se realizará en el lenguaje de programación Python.
##Explicación##
Ya que aún no sé en que consistirá mi proyecto de DAI no puedo proporcionar la explicación de qué tipo de proyecto realizaré, no obstante, cuando sepa que hacer actualizaré este apartado pero dado que para DAI se realizará una aplicación web se necesitarán varios servidores y quizá un balanceador para dar soporte de infraestructura virtual a dicha aplicación.

##Inscripción en el certamen de Proyectos Libres de la UGR 2015-2016##
Aquí adjunto la imagen de la inscripción realizada correctamente en el Certamen:

![Inscripción](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/InscripcionUGR_zpsgkjszv6h.png)


## Segundo Hito

[![Build Status](https://travis-ci.org/pedrogazquez/Proyecto-IV.svg?branch=master)](https://travis-ci.org/pedrogazquez/Proyecto-IV)

[Aquí el enlace a mi proyecto](https://github.com/pedrogazquez/Proyecto-IV). 

Revisión 2: arreglado enlace a Travis y pequeños cambios en la aplicación.

Para realizar los tests de mi proyecto he usado la libreria de unittest de python. Son tests flexibles y muy usados en este lenguaje. Los tests que he realizado los he integrado dentro de las herramientas de construcción, incluyendo un objetivo make test en [mi makefile](https://github.com/pedrogazquez/Proyecto-IV/blob/master/makefile). Para configurar el sistema de integración continua de forma que lance los tests automáticamente he usado Travis-CI y Shippable.

#Shippable
He creado mi archivo [shippable.yml](https://github.com/pedrogazquez/Proyecto-IV/blob/master/shippable.yml) una vez registrado en la página de Shippable y autorizado para que realicen los tests automáticamente. Como se puede ver en la siguiente imagen se realiza todo correctamente.
![shippable](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/ship_zpskdghgjx4.png)


#Travis
Como he hecho con el anterior he creado mi archivo [travis.yml](https://github.com/pedrogazquez/Proyecto-IV/blob/master/.travis.yml), igual que antes registrado con github previamente. Una vez hecho estó como se puede ver en la siguiente imagen el resultado de los tests es positivo:
![travis](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/trav_zpshehbyrb0.png)
