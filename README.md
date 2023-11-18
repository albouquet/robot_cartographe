# Projet : Robot cartographe

Ce projet a pour objectif de créer un robot permettant de modéliser la zone qu'il explore.
Celui-ci est commandé à distance et équipé d'une caméra embarquée et de capteurs de distance.

Le flux vidéo et les données de télémétrie permettront, grâce à un logiciel utilisant la bibliothéque VTK, de modéliser la zone en 3 dimensions.

## Principe de modélisation : 

Les images prises par la caméra seront analysées afin de detecter les contours de chaques éléments.

Deux capteurs télémetriques seront placés vers l'avant du robot, calibrés avec la caméra. 
Ceux-ci permettront de connaitre la distance à gauche et à droite de l'image (voir schéma).
Il y aura 2 données de télémetrie par image.

Toutes ces données (images + télémetries) permettront de reconstruire l'environnement en 3 dimensions.
La gestion des redondances de plan d'image est primordiale pour controler la justesse de la modélisation.

## Composition du robot

Le robot est une structure métallique comprenant deux motoreducteurs. Ceux-ci seront alimentés par une batterie 18650, a travers un transistor et un signal PWM.

Le système est principalement composé d'une Raspberry pi zero. Celle-ci transmettra les données vidéos et télémétriques par liaison WIFI à un ordinateur.

Deux capteurs télémetrique et une picaméra sont donc nécessaire.


