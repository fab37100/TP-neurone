from random import uniform, randrange
import getopt
import pickle
import sys
import matplotlib.pyplot as plt

# region Définition des variables
a = 3
b = 4
nom_fichier = "neurone.bak"


# endregion

# region Définition de la classe Neurone

class Neurone:
    # Initialisation du neurone en définissant son poids et son biais
    def __init__(self):
        self.poids = uniform(-1, 1)
        self.biais = uniform(-1, 1)

    # Enregistrement du neurone dans un fichier .bak avant la destruction de l'objet
    def __del__(self):
        print("Sauvegarde du neurone dans le fichier " + str(nom_fichier))
        with open(nom_fichier, "wb") as f:
            pickle.dump(self, f, protocol=2)
            # print("poids : " + str(self.poids) + " biais : " + str(self.biais))

    # Chargement du neurone depuis le fichier .bak
    def chargement(self):
        with open(nom_fichier, "rb") as f:
            # pickle.dump(self, f, protocol=2)
            contenu_fichier = pickle.load(f)
            self.poids = contenu_fichier.poids
            self.biais = contenu_fichier.biais
            print("Voici les récupérées :\nPoids : " + str(self.poids) + "\nBiais : " + str(self.biais))

    # Apprentissage du neurone
    # X correspond a une valeur aléatoire de la fonction et Y est son resultat
    def apprentissage(self, x, y):
        valeur = (x * self.poids) + self.biais
        self.poids += (y - valeur) * 0.01 * 0.01 * x
        self.biais += 0.01 * (y - valeur) * 0.05
        return valeur


# endregion

def main():
    print("""
############################
##   Début du traitement  ##
############################
    """)

    # Récupération des paramètres d'entrée
    opts, args = getopt.getopt(sys.argv, "hrl:ac", ["apprentissage", "creation", "comparaison"])

    # Partie d'apprentissage du neurone
    if "--apprentissage" in args:
        print("Chargement de l'ancien neurone")
        neurone = Neurone()
        neurone.chargement()


        for i in range(0, 40):
            x = uniform(0, 50)
            y = a * x + b
            # resultat.append([x, y])
            r = neurone.apprentissage(x, y)

            # Compare le resultat trouvé par le neurone et celui attendu
            if r == y:
                print("Nous l'avons fait !")
        print("\nNouveau Biais : " + str(neurone.biais) + "   | Nouveau poids : " + str(neurone.poids))

    # Génération d'un nouveau neurone
    elif "--creation" in args:
        print("Création d'un nouveau neurone")
        neurone = Neurone()
        print("Biais : " + str(neurone.biais) + "\nPoids : " + str(neurone.poids))

    # Compare 10 valeurs calculées par le neurone par rapport à la valeur exacte
    elif "--comparaison" in args:
        neurone = Neurone()

        # Charge le neurone stocké dans le fichier .bak
        neurone.chargement()
        xs = []
        ys = []
        resultat = []

        #Calcule pour 10 itération une valeur x calculer par le neurone
        for i in range(10):
            x = randrange(0, 50)
            xs.append(x)
            resultat.append(neurone.poids * x + neurone.biais)
            ys.append((a * x) + b)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(xs, ys, 'k')
        plt.plot(xs, resultat, 'ro')
        print('\033[92m' + "Affichage de la comparaison sur un graphe" + '\033[0m')
        plt.show()
    else:
        print('\033[93m' + """Merci d'entrer l'un des paramètres suivants:
--creation = Créer un nouveau neurone
--apprentissage = Reutiliser le neurone de la dernière session afin de l'affiner
--comparaison = Génére un graphe juxtaposant la courbe trouvé par le neurone et celle désirée""" + '\033[0m')

    print("""
############################
##   Fin du traitement    ##
############################
""")


if __name__ == '__main__':
    main()
