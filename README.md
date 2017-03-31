# TP-neurone
<p></p>

## Utilisation du script
le script s'exécute depuis le fichier "main.py" et prend en compte des paramètres. Un seul paramètre peut être utilisé à la fois:
- --creation : créer un neurone et l'enregistre dans un fichier .bak à la racine de l'exécution
 <pre>main.py --creation</pre>
- --apprentissage : affine le neurone pour se rapprocher du plus possible de la fonction
<pre>main.py --apprentissage</pre>
- --comparaison : génère un graphe sur lequel sont présentes 10 valeurs calculées par le neurone superposé à la fonction
<pre>main.py --comparaison</pre>

Si aucun paramètres n'est fourni, le script renverra une aide à l'utilisateur
<pre>############################
##   Début du traitement  ##
############################
    
<span style="color:yellow">Merci d'entrer l'un des paramètres suivants:
--creation = Créer un nouveau neurone
--apprentissage = Reutiliser le neurone de la dernière session afin de l'affiner
--comparaison = Génére un graphe représentant des points calculés par le neurone et la courbe de la fonction désirée</span>
    
############################
##   Fin du traitement    ##
############################</pre>
## Scénario
<p>Ce jeux de donnée met en évidence l'évolution d'un neurone</p>

### Création du neurone
La création d'un neurone va définir un biais et un poid aléatoirement compris entre -1 et 1 
<pre>>>>main.py --creation
    
############################
##   Début du traitement  ##
############################
    
Création d'un nouveau neurone
Biais : -0.6719747569826
Poids : 0.429503827620187
    
############################
##   Fin du traitement    ##
############################

Sauvegarde du neurone dans le fichier neurone.bak
</pre>

### Comparaison sans apprentissage
Le script va créer un graphe représentant 10 valeurs calculé par le neurone et la fonction à s'approcher le plus possible
```
>>>main.py --comparaison
    
############################
##   Début du traitement  ##
############################
    
Voici les récupérées :
Poids : 0.429503827620187
Biais : -0.6719747569826
Sauvegarde du neurone dans le fichier neurone.bak
Affichage de la comparaison sur un graphe
    
############################
##   Fin du traitement    ##
############################

Sauvegarde du neurone dans le fichier neurone.bak
```
 
La **ligne** **noir** correspond à la fonction qu'il faut trouver et les <span style="color:red">**points** **rouges**</span> correspondent aux valeurs calculées par le neurone

 ![ComparaisonSansApprentissage](https://github.com/fab37100/TP-neurone/blob/master/images/1.png "graphe sans apprentissage")

On peut voir que le neurone est plutôt loin de la fonction sans apprentissage.
### Apprentissage du neurone
Le neurone va modifier sont biais et son poids afin d'être le plus proche possible de la fonction
```
>>>main.py --apprentissage
    
############################
##   Début du traitement  ##
############################
    
Chargement de l'ancien neurone
Voici les récupérées :
Poids : 0.429503827620187
Biais : -0.6719747569826
Sauvegarde du neurone dans le fichier neurone.bak
    
Nouveau Biais : -0.2641461917035273   | Nouveau poids : 3.0672470043545905
    
############################
##   Fin du traitement    ##
############################

Sauvegarde du neurone dans le fichier neurone.bak
```

## Comparaison avec apprentissage
```
>>>main.py --comparaison
    
############################
##   Début du traitement  ##
############################
    
Voici les récupérées :
Poids : 3.0672470043545905
Biais : -0.2641461917035273
Sauvegarde du neurone dans le fichier neurone.bak
Affichage de la comparaison sur un graphe
    
############################
##   Fin du traitement    ##
############################

Sauvegarde du neurone dans le fichier neurone.bak
```
![ComparaisonAvecApprentissage](https://github.com/fab37100/TP-neurone/blob/master/images/2.png "graphe avec apprentissage")