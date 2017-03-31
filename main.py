from random import uniform
import getopt
import pickle
import sys

a = 3
b = 4
nom_fichier = "neurone.bak"


# region Définition de la classe Neurone

class Neurone:
    # Initialisation du neurone en définissant son poids et son biais
    def __init__(self):
        self.poids = uniform(-1, 1)
        self.biais = uniform(-1, 1)

    # Enregistrement du neurone avant ça destruction
    def __del__(self):
        print("Sauvegarde du neurone dans le fichier " + str(nom_fichier))
        with open(nom_fichier, "wb") as f:
            pickle.dump(self, f, protocol=2)

    # Chargement du neurone depuis le fichier .bak
    def chargement(self):
        with open(nom_fichier, "wb") as f:
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
    resultat = []
    for i in range(0, 100):
        x = uniform(0, 100)
        y = a * x + b
        resultat.append([x, y])
        # print(resultat[i][1])


if __name__ == '__main__':
    main()
