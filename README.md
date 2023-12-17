# Projet : Robot cartographe

Ce projet a pour objectif de créer un robot permettant de modéliser la zone qu'il explore.
Celui-ci est commandé à distance et équipé d'une caméra embarquée et des capteurs de distance.

Le flux vidéo et les données de télémétrie permettront, grâce à un logiciel utilisant la bibliothéque VTK, de modéliser la zone en 3 dimensions.

## Principe de modélisation : 

Les images prises par la caméra seront analysées afin de detecter les contours de chaques éléments.

Deux capteurs télémetriques seront placés vers l'avant droit et gauche du robot (4 capteurs au total), calibrés avec la caméra. 
Ceux-ci permettront de connaitre la distance à gauche et à droite de l'image (voir schéma).
![Schéma capteur télémetrique](images/exemple_capt.jpg)

Il y aura 4 données de télémetries par image.
*Avec 4 capteurs seulement, le nombre d'éléments ayant une distance dans une image s'élève donc à 4. C'est assez peu. L'objectif ici est de voir si ce système donne des résultats satisfaisants, ou non, pour le mapping 3D.
Dans le cas contraire, je rajouterai soit plus de capteurs, soit deux servomoteurs afin de "balayer" les surfaces avec les capteurs télémetriques.*

La technique de mapping est la suivante pour chaque image (pour un seul coté) :
* Réalisation d'une détéction de contours (+ détection de zone) sur l'image.
* Récupération des deux distances et association avec leur "zone".
* Les zones "non associées à une distance" seront associées soit à un zone précédente (si c'est le même type de zone), ou alors ne seront pas interprétées.
* Modélisation (création de points) sur le modèle 3D en prenant en compte les contours formant les zones, les distances de celles-ci, et la position du robot.


Toutes ces données (images + distance) permettront de réaliser un mapping en 3 dimensions de l'environnement dans lequel évolue le robot.
La gestion des redondances de plan d'image est primordiale pour controler la justesse de la modélisation.

## Composition du robot

Le robot est une structure métallique comprenant deux motoreducteurs. Ceux-ci seront alimentés par une batterie 18650, a travers deux transistors et deux signaux PWM.

Le système est principalement composé d'une Raspberry pi zero. Celle-ci transmettra les données vidéos et télémétriques par liaison WIFI à un ordinateur.

Quatres capteurs télémetriques et une picaméra sont nécessaires.


## Mise à jour 
* 12/11/2023 : Création du projet.
* 19/11/2023 : Actualisation du principe de modélisation et de la composition du robot.
* 26/11/2023 : Test des capteurs vl53l0x (en I2C) et TfMini (UART).
* 17/12/2023 : Test de transmission et reception vidéo


