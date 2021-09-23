![Python 2.7](https://img.shields.io/badge/python-2.7%2B-green)      ![cisco ios](https://img.shields.io/badge/cisco-ios-yellow)      ![Licence GPL-3.0](https://img.shields.io/badge/Licence-GPL%%3.0-red)

# cisco_host_config_backup
Ce script réalise le backup de la configuration de vos équipements CISCO; il est écrit en python 2.7

Représentation de l'infrastructure :

![Infra script backup cisco](https://user-images.githubusercontent.com/46109209/134438643-949ba2ee-628b-4adf-b86b-7f6d5bd26573.png)


## Compatibilité
 - :white_check_mark: Routeurs CISCO
 - :white_check_mark: Commutateurs CISCO (Layer 3)


## Pré-requis
Vous aurez besoin d'un accès Telnet sur les cibles, ainsi que d'un même "Username" sur chacun d'entre eux.

## Installation du système

Nous avons utilisé une machine linux Ubuntu 18.04. 
La version la plus récente de 'Python' au moment de la rédaction est la '3.8'.
Cependant, la version utilisée est "2.7"

Procédez comme suit pour l'installation:

![1](https://user-images.githubusercontent.com/46109209/134434702-354572fd-8239-4ff1-ab76-139ce1db18b9.png)

![2](https://user-images.githubusercontent.com/46109209/134434712-5545b39e-0073-490b-b021-dd3a80c3f963.png)


À présent, il faut déterminer l'emplacement du script et et des fichiers :
" /home/gns3/Scripts/Python-Scripts/ "

![3](https://user-images.githubusercontent.com/46109209/134435282-d4ee782a-5c9b-44bb-87f6-f8a4fbf1bcab.png)

En "1" et "2", créer les fichiers.

En "3", attribuer les droits 777 sur l'ensemble des fichiers. 

N.B. IL NE FAUT JAMAIS DONNER TOUS LES DROITS AUX UTILISATEURS DU SYSTÈME.

![4](https://user-images.githubusercontent.com/46109209/134436281-c71adb0e-f0f5-4a22-8e4c-e718dd15a89d.png)
 
Il est également possible de rendre le script exécutable avec la commande : " sudo chmod +x ./cisco_backup.py "

Avec, la commande suivante, lancez le script : " sudo ./cisco_backup.py "

![5](https://user-images.githubusercontent.com/46109209/134436693-836f6daf-782e-4f76-8fa8-9d83bba1b0bd.png)


## Déroulement de l'exécution du script :

Sur la machine Ubuntu:

![7](https://user-images.githubusercontent.com/46109209/134437064-78a0234e-98f2-40b4-a943-eacf932ef5be.png)

Sur le routeur:

![6](https://user-images.githubusercontent.com/46109209/134437621-b79b86ed-aa1e-4b97-a1b1-e4102d4a35db.png)

Emplacement des 'backup':

![8](https://user-images.githubusercontent.com/46109209/134438072-b11af136-e946-4bed-9618-ad429c5c2e2d.png)


