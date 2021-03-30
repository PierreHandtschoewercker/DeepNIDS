# PermaDeep
## Installation projet

Ce projet repose sur une image docker
La première étape est de construire cette image

Note : Le nom du compte peut être ce que vous voulez. Il en va de même pour le nom de l'image.


```
cd PermaDeep/4.Docker/
docker build -t [TAG_NAME] .
```

Une fois l'image construite il faut créer un container
```
docker run -d -p 8888:8888 -v /chemin/absolu/dossierprojet:/code nomducompte/nomdelimage
```
voilà l'image tourne maintenant sur votre machine

Pour lister les images il faut saisir la commande suivante:
```
docker images -a
```

pour commencer à développer il vous faut l'url du serveur jupyter
```
docker exec -it nomduconatainer bash
jupyter notebook list
```

vous pouvez utiliser l'url directement dans votre navigateur ou l'utiliser pour connecter **vscode** au serveur et développer depuis là bas

## Utilisation de l'image
une fois le container créer

Obtenir le nom du container : 
```
docker container ls -a
```

**Attention a bien prendre le nom du container et pas celui de l'image**

 Vous pouvez démarrer le container pour reprendre votre développement via 
 ```
 docker start nomducontainer
 ```
 
 Une fois le développement terminer vous pourrez stopper le container :
```
docker stop nomducontainer
```
