# OC Projet 2 : Utilisez les bases de Python pour l'analyse de marché

# Introduction 
Pour ce projet j'ai créer des scripts python capable d'extraire des information du site de vente de livre https://books.toscrape.com/ 
J'ai créer 3 script qui sont les suivants : 

Le premiéer fichier one_book.py extrait les information d'un seul livre que j'ai aléatoirement choisi (vous pouvais par la suite changer le livre en modifiant le lien)
ensuite ces informations sont stocké dans un fichier CSV

Le second fichier one_category.py extrait les information de toutes les livres d'une seule catégorie que j'ai aléatoirement choisi en prenant en compte le faite qu'il y'est ou non des pages additionels (vous pouvais par la suite changer la catégorie en modifiant le lien)
ensuite ces informations sont stocké dans un fichier CSV

Le dernier fichier Allbooks.py extrait les information de toutes les livres par catégorie,télécharge l'image de chaque page produit et enregistre ces information dans des fichiers CSV (Le nom de chaque fichier CSV corresponds a celui de la catégorie)  


# Installation 

Installer Python sur votre systéme

``` Télécharger python pour Windows : https://www.python.org/downloads/```
```Télécharger python pour Mac : https://www.python.org/downloads/macos/```
```Télécharger python pour Linux : https://docs.python.org/3/using/unix.html```


Ensuite vous devez créer votre environment virtuel j'utilise Pycharm comme IDE : 
```https://www.jetbrains.com/pycharm/```

Pour créer un environment virtuel il faut suivre les étapes suivantes : 
1- Ovrir Pycharm 
2 - Cliquer sur fichier, Nouveau Projet 
3 - Séléctionner Nouvelle environment en utilisant "Virtualenv"
4 - Cliquer sur créer 

Vous devez maintenant installer les packages nécessaire exécuter cette commande dans le terminal pycharm   
```pip install -r requirements.txt```

Vous étes maintenant prés a utiliser les scripts avec cette commande : 
```python3 "name of the file".py```


