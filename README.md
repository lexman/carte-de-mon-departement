# Cartes des départements 

Ce projet extrait la cartes de chaque départements français depuis l'archive hebdomadaire d'Open Street Map, selon la [méthode proposée 
Maxime Résibois](http://www.portailsig.org/content/recuperer-des-donnees-openstreetmap-gdalogr)
 sur PortailSIG. 


# Contenu

Chaque département est livré sous forme d'une archive ZIP qui contient plusieurs couches cartographiques au fomat shapefile (le .doc de la cartographie) :
- places.shp : noms des villes ou des quartiers
- roads.shp : toutes les voies de passage de l'autoroute au chemin piéton
- buildings.shp : l'espace bâti
- raillways.shp : les voies ferrées
- waterways.shp :le réseau hydrolique
- points.shp : une liste de point d’intérêt
- natural.shp : zones vertes
- landuse.shp : occupation des sol
- admin-departement.shp : le département

Par ailleurs, un fichier projet [QGis](http://www.qgis.org/fr/site/) très sommaire est fourni dans l'archive, afin de visualiser la superposition des couches dans un outil libre.


# Installation et lancement

Ce projet nécessite [tuttle](https://github.com/lexman/tuttle), un système de build pour les données.
Une fois que vous avez installé tuttle en suivant les instructions pour votre système, vous pouvez lancer le traitement des données avec a commande :

    tuttle run


# Licence
Les sources de ce projet sont sous licence MIT.

Si vous lancez ce projet les cartes obtenues seront sous licence ODbL qui impose un partage à l'identique et la mention obligatoire d'attribution doit être "© les contributeurs d'OpenStreetMap sous licence ODbL" conformément à http://osm.org/copyright