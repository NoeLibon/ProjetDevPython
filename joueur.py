from grille import Grille
from terrain_ennemi import Terrain_ennemi
from bateau import Bateau
import os

class Joueur:

    navires = {"Porte-avions": 5, "Croiseur": 4, "Contre-torpilleur": 3, "Sous-marin": 2}

    def __init__(self, nom):
        self.grille = Grille()
        self.terrain_ennemi = Terrain_ennemi()
        self.nom = nom
        self.flotte = []

    def placement_flotte(self):
        print("Choisissez une coordonnées entre 0 et 9 pour atribuer une ligne et une colonne à votre bateau ")
        print("Les bateux sont placés en partant de la droite et de haut en bas.")
        for bateau, taille in self.navires.items():

            drapeau = True
            while drapeau:
                self.apercu_ocean()
                try:
                    print("Veuillez placer votre %s" % (bateau))
                    ligne = int(input("Choisissez une ligne -----> "))
                    col = int(input("Choisissez une colonne -----> "))
                    orientation = str(input("Verical ou horizontal (tapez v pour vertical ou h pour horizontal -----> "))

                    if orientation in ["v", "V"]:
                        if self.grille.placement_valide_ligne(ligne, col, taille):
                            self.grille.placement_bateau_ligne(ligne, col, taille)
                            bateau = Bateau(bateau, taille)
                            bateau.positionnement_vertical(ligne, col)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            input("Deux bateaux ne peuvent pas occuper la même case, réessayez!")

                    elif orientation in ["h", "H"]:
                        if self.grille.placement_valide_col(ligne, col, taille):
                            self.grille.placement_bateau_col(ligne, col, taille)
                            bateau = Bateau(bateau, taille)
                            bateau.positionnement_horizontal(ligne, col)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            input("Deux bateaux ne peuvent pas occuper la même case, réessayez!")

                    else:
                        continue

                    self.apercu_ocean()
                    input()
                    os.system('cls')

                except ValueError:
                    print("Entrez un numéro...\n")

    def apercu_ocean(self):
        self.terrain_ennemi.aprecu_terrain_ennemi()
        print("|                 |")
        self.grille.apercu_grille()

    def coup_enregistre(self, ligne, col):
        for bateau in self.flotte:
            if (ligne, col) in bateau.coo:
                bateau.coo.remove((ligne, col))
                if bateau.verif_etat():
                    self.flotte.remove(bateau)
                    print("le %s de %s a été coulé!" % (bateau.modele, self.nom))

    def tir(self, cible):
        self.apercu_ocean()
        try:
            print("\n%s Entrez les coordonnées à cibler..." % (self.nom))
            ligne = int(input("Choisissez une ligne -----> "))
            col = int(input("Choisissez une colonne -----> "))

            if self.grille.verif_ligne(ligne) and self.grille.verif_col(col):
                if cible.grille[ligne, col] == "B":
                    print("Touché!!!")
                    cible.grille[ligne, col] = "X"
                    cible.coup_enregistre(ligne, col)
                    self.terrain_ennemi[ligne, col] = "X"

                else:
                    if self.terrain_ennemi.terrain_ennemi[ligne][col] == "O":
                        print("Coordonnées déjà ciblées....Regardez votre carte!")
                        self.tir(cible)
                    else:
                        print("Manqué...")
                        self.terrain_ennemi.terrain_ennemi[ligne][col] = "O"

            else:
                print("Ne visez pas le Lune, entrez des coordonnées valides...")
                self.tir(cible)

        except ValueError:
            print("Vous devez entrer des coordonnées....\n")
            self.tir(cible)
        input()
        os.system('cls')
