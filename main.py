from random import uniform
import getopt
import pickle
import sys

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

    # Enregistrement du neurone avant ça destruction
    def sauvegarde(self):
        print("Sauvegarde du neurone dans le fichier " + str(nom_fichier))
        with open(nom_fichier, "wb") as f:
            pickle.dump(self, f, protocol=2)
        print("poids : " + str(self.poids) + " biais : " + str(self.biais))

    # Chargement du neurone depuis le fichier .bak
    def chargement(self):
        with open(nom_fichier, "rb") as f:
            # pickle.dump(self, f, protocol=2)
            contenu_fichier = pickle.load(f)
            self.poids = contenu_fichier.poids
            self.biais = contenu_fichier.biais
            print("Voici les récupérées :\nPoids : " + str(self.poids) + "\nBiais : " + str(self.biais))

    # Apprentissage du neurone
    # X correspond a un valeur aléatoire de la fonction et Y est son resultat
    def apprentissage(self, x, y):
        valeur = (x * self.poids) + self.biais
        self.poids += (y - valeur) * 0.01 * 0.01 * x
        self.biais += 0.01 * (y - valeur) * 0.05
        return valeur


# endregion

def main():
    print('Démarrage du neurone')

    # Récupération des paramètres d'entrée
    opts, args = getopt.getopt(sys.argv, "hrl:ac", ["recharger", "comparaison"])

    if "--recharger" in args:
        print("Chargement de l'ancien neurone")
        neurone = Neurone()
        neurone.chargement()
        resultat = []
        for i in range(0, 1000):
            x = uniform(0, 50)
            y = a * x + b
            resultat.append([x, y])
            r = neurone.apprentissage(x, y)
            if r == y:
                print("Nous l'avons fait !")
        # print("Nouveau biais : " + str(neurone.biais) + "\nNouveau poids : " + str(neurone.poids))
        neurone.sauvegarde()
    else:
        print("Création d'un nouveau neurone")
        neurone = Neurone()
        print("Biais : " + str(neurone.biais) + "\nPoids : " + str(neurone.poids))
        neurone.sauvegarde()

if __name__ == '__main__':
    main()
