# TP-neurone
<p></p>

## Utilisation du script
le script s'exécute depuis le fichier "main.py" et prend en compte des paramètres. Un seul paramètre peut être utilisé à la fois:
- --creation : créer un neurone et l'enregistre dans un fichier .bak à la racine de l'exécution
 <code>main.py --creation</code>
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
##Scénario
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
<pre>>>>main.py --comparaison
    
############################
##   Début du traitement  ##
############################
    
Voici les récupérées :
Poids : 0.429503827620187
Biais : -0.6719747569826
Sauvegarde du neurone dans le fichier neurone.bak
<span style="color:green">Affichage de la comparaison sur un graphe</span>
    
############################
##   Fin du traitement    ##
############################

Sauvegarde du neurone dans le fichier neurone.bak
 </pre>
 ![ComparaisonSansApprentissage](https://github.com/fab37100/TP-neurone/blob/master/images/1.png "graphe sans représentation")
